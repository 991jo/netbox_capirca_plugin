from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

menu_items = (
        PluginMenuItem(
            link="plugins:netbox_capirca_plugin:acl_list",
            link_text="ACLs",
            buttons=(
                PluginMenuButton("plugins:netbox_capirca_plugin:acl_add",
                                 "Add",
                                 "mdi mdi-plus-thick",
                                 ButtonColorChoices.GREEN),
                )
            ),
        )
