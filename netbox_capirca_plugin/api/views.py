from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from netbox_capirca_plugin.models import ACL, ACLInterfaceAssignment
from .serializers import ACLSerializer, ACLInterfaceAssignmentSerializer
from netbox_capirca_plugin import filters
from django.shortcuts import get_object_or_404

from netbox_capirca_plugin.exceptions import UnsupportedTarget


class ACLViewSet(ModelViewSet):
    queryset = ACL.objects.all()
    serializer_class = ACLSerializer
    filterset_class = filters.ACLFilter

    @action(detail=True, methods=["get"])
    def render(self, request, pk=None):
        acl = get_object_or_404(self.queryset, pk=pk)

        target = request.GET.get("target", None)
        options = request.GET.get("options", "")
        if target is None:
            return Response("required parameter 'target' is missing.",
                            status.HTTP_400_BAD_REQUEST)

        try:
            result = str(acl.render(target, options))
        except UnsupportedTarget:
            return Response(f"target { target } is not supported",
                            status.HTTP_400_BAD_REQUEST)

        return Response(result, status.HTTP_200_OK)


class ACLInterfaceAssignmentViewSet(ModelViewSet):
    queryset = ACLInterfaceAssignment.objects.all()
    serializer_class = ACLInterfaceAssignmentSerializer
    filterset_class = filters.ACLInterfaceAssignmentFilter
