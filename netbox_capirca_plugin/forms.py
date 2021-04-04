from django import forms
from utilities.forms import BootstrapMixin

from .models import ACL, ACLInterfaceAssignment
from .exceptions import UnsupportedTarget


class ACLFilterForm(BootstrapMixin, forms.ModelForm):

    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    static_definitions_dir = forms.CharField(required=False)
    policy_template_path = forms.CharField(required=False)

    class Meta:
        model = ACL
        fields = []

class ACLForm(BootstrapMixin, forms.ModelForm):

    static_definitions_dir = forms.CharField()
    policy_template_path = forms.CharField()

    class Meta:
        model = ACL
        fields = ["name", "description", "static_definitions_dir", "policy_template_path", "networks", "services", "terms"]

class ACLRenderForm(BootstrapMixin, forms.Form):

    target = forms.CharField(required=True)

    def __init__(self, acl, *args, **kwargs):
        super(forms.Form, self).__init__(*args, **kwargs)
        self.acl = acl

    def clean(self):
        super().clean()
        try:
            self.acl.get_render_function(self.cleaned_data["target"])
        except UnsupportedTarget:
            self.add_error("target", f"target { self.cleaned_data['target'] } is not supported")

    class Meta:
        fields = ["target"]

class ACLInterfaceAssignmentForm(BootstrapMixin, forms.ModelForm):

    class Meta:
        model = ACLInterfaceAssignment
        fields = ["interface", "ingress", "egress"]
