__version__ = "0.1.0"

from extras.plugins import PluginConfig


class NetboxACLPluginConfig(PluginConfig):
    name = 'netbox_capirca_plugin'
    verbose_name = 'netbox Capirca Plugin'
    description = 'A plugin for ACL management with capirca',
    version = __version__
    author = 'Johannes Erwerle'
    author_email = 'erwerle@belwue.de'
    required_settings = []
    base_url = "netbox-capirca-plugin"
    default_settings = {}
    required_settings = ["default_definitions_path",
                         "default_policy_template",
                         "definitions_base_path",
                         "policy_base_path"]


config = NetboxACLPluginConfig
