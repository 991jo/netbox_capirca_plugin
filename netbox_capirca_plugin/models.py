from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.validators import validate_slug
from django.urls import reverse


from typing import Callable
from pathlib import Path

from .utils import NamingWrapper, combine_paths_checked, cisco_acl_cleanup
from .exceptions import UnsupportedTarget
from capirca.lib.policy import ParsePolicy
from capirca.lib.cisco import Cisco
from capirca.lib.ciscoxr import CiscoXR
from jinja2 import Template

try:
    from netbox.models import ChangeLoggedModel
except ModuleNotFoundError:
    from extras.models import ChangeLoggedModel

from dcim.models import Interface


class ACL(ChangeLoggedModel):

    networks = models.TextField(blank=True)
    services = models.TextField(blank=True)
    terms = models.TextField(blank=True)

    policy_template_path = models.TextField()

    name = models.CharField(max_length=255, unique=True, validators=[validate_slug])

    description = models.CharField(max_length=255, blank=True)

    def clean(self):
        super().clean()

        errors = dict()

        naming = NamingWrapper(settings.PLUGINS_CONFIG["netbox_capirca_plugin"]["definitions_path"])

        # check that adding the network definitions works
        try:
            naming.add_definitions(self.networks, "networks")
        except Exception as e:
            errors["networks"] = f"Could not verify the network definitions { e }"
            raise ValidationError(errors)

        # check that adding the network definitions works
        try:
            naming.add_definitions(self.services, "services")
        except Exception as e:
            errors["services"] = f"Could not verify the network definitions { e }"
            raise ValidationError(errors)

        # check the policy template
        try:
            with open(self.get_full_policy_template_path()) as f:
                template_text = f.read()
            template = Template(template_text)
            policy_text = template.render(acl=self)
        except Exception as e:
            errors["policy_template_path"] = f"Error while loading policy template from { self.policy_template_path }: { e }"
            raise ValidationError(errors)

        try:
            base_dir = settings.PLUGINS_CONFIG["netbox_capirca_plugin"]["policy_base_path"]
            ParsePolicy(policy_text, naming, base_dir=base_dir)
        except Exception as e:
            errors["terms"] = f"Error while parsing policy: { e }"
            raise ValidationError(errors)

    def get_full_policy_template_path(self) -> str:
        """
        Returns the complete policy template path consisting of the base
        path and the appropriate extension.

        Raises an BasePathEscapeError when the path tries to leave the base
        path.
        """

        base_path = Path(settings.PLUGINS_CONFIG["netbox_capirca_plugin"]["policy_base_path"])

        return combine_paths_checked(base_path, Path(self.policy_template_path))

    def render(self, target: str = None, options: str = "") -> str:
        """
        Renders the ACL.

        target: the name of the capirca target
        """

        naming = NamingWrapper(settings.PLUGINS_CONFIG["netbox_capirca_plugin"]["definitions_path"])
        naming.add_definitions(self.networks, "networks")
        naming.add_definitions(self.services, "services")

        with open(self.get_full_policy_template_path()) as f:
            template_text = f.read()
        template = Template(template_text)
        policy_text = template.render(acl=self, target=target, options=options)

        base_dir = settings.PLUGINS_CONFIG["netbox_capirca_plugin"]["policy_base_path"]
        policy = ParsePolicy(policy_text, naming, base_dir=base_dir)

        render_function = self.get_render_function(target)
        return render_function(policy)

    def get_render_function(self, target) -> Callable:
        render_function = getattr(self, f"_render_{ target }", None)
        if render_function is None:
            raise UnsupportedTarget(f"Target { target } is not supported.")
        return render_function

    def _render_cisco(self, policy) -> str:
        return cisco_acl_cleanup(str(Cisco(policy, 1)))

    def _render_ciscoxr(self, policy) -> str:
        return cisco_acl_cleanup(str(CiscoXR(policy, 1)))

    def get_absolute_url(self):
        return reverse("plugins:netbox_capirca_plugin:acl",
                       kwargs={"pk": self.pk})

    def __str__(self):
        return f"ACL { self.name }"


class ACLInterfaceAssignment(ChangeLoggedModel):

    interface = models.OneToOneField(Interface, on_delete=models.CASCADE)
    ingress = models.ForeignKey(ACL,
                                on_delete=models.PROTECT,
                                related_name="%(class)s_ingress",
                                blank=True,
                                null=True)
    egress = models.ForeignKey(ACL,
                               on_delete=models.PROTECT,
                               related_name="%(class)s_egress",
                               blank=True,
                               null=True)
