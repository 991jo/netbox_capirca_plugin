from rest_framework.serializers import ModelSerializer
from netbox_capirca_plugin.models import ACL, ACLInterfaceAssignment

from netbox.api import WritableNestedSerializer

from dcim.api.nested_serializers import NestedInterfaceSerializer


class ACLSerializer(ModelSerializer):

    class Meta:
        model = ACL
        fields = ("id", "name", "description", "networks", "services",
                  "terms", "policy_template_path")


class NestedACLSerializer(WritableNestedSerializer):

    class Meta:
        model = ACL
        fields = ['id', 'name', 'description']


class ACLInterfaceAssignmentSerializer(ModelSerializer):
    ingress = NestedACLSerializer()
    egress = NestedACLSerializer()
    interface = NestedInterfaceSerializer()

    class Meta:
        model = ACLInterfaceAssignment
        fields = ("id", "interface", "ingress", "egress")
