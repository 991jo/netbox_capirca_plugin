import django_filters

from .models import ACL, ACLInterfaceAssignment


class ACLFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    static_definitions_dir = django_filters.CharFilter(lookup_expr="icontains")
    policy_template_path = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = ACL

        fields = ["name", "description", "static_definitions_dir",
                  "policy_template_path"]

class ACLInterfaceAssignmentFilter(django_filters.FilterSet):

    class Meta:
        model = ACLInterfaceAssignment

        fields = ["interface_id", "ingress", "egress"]
