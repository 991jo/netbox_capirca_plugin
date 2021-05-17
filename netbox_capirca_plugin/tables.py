from utilities.tables import BaseTable, ToggleColumn

import django_tables2 as tables


from .models import ACL


class ACLTable(BaseTable):

    pk = ToggleColumn()
    name = tables.LinkColumn()


    class Meta(BaseTable.Meta):
        model = ACL
        fields = ["pk",
                  "name",
                  "description",
                  "policy_template_path"]
