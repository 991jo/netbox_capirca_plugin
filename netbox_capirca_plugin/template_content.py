from extras.plugins import PluginTemplateExtension

from .models import ACLInterfaceAssignment

class InterfaceACL(PluginTemplateExtension):
    model = "dcim.interface"

    def right_page(self):

        acl = ACLInterfaceAssignment.objects.filter(interface=self.context["object"]).first()

        return self.render("netbox_capirca_plugin/interface_acl.html",
                           {"interface_acl": acl,
                            "interface": self.context["object"]})

template_extensions = [InterfaceACL]
