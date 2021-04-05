from rest_framework.viewsets import ModelViewSet
from netbox_capirca_plugin.models import ACL, ACLInterfaceAssignment
from .serializers import ACLSerializer, ACLInterfaceAssignmentSerializer
from netbox_capirca_plugin import filters


class ACLViewSet(ModelViewSet):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer
    filterset_class = filters.ACLFilter

class ACLInterfaceAssignmentViewSet(ModelViewSet):
    queryset = ACLInterfaceAssignment.objects.all()
    serializer_class = ACLInterfaceAssignmentSerializer
