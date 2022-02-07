__version__ = "1.0.9"

from extras.plugins import PluginConfig


class NetboxACLPluginConfig(PluginConfig):
    name = 'netbox_capirca_plugin'
    verbose_name = 'netbox Capirca Plugin'
    description = 'A plugin for ACL management with capirca',
    version = __version__
    author = 'Johannes Erwerle'
    author_email = 'erwerle@belwue.de'
    required_settings = []
    base_url = "netbox_capirca_plugin"
    min_version = '3.0'
    default_settings = {}
    required_settings = ["default_policy_template",
                         "definitions_path",
                         "policy_base_path"]


# try:
#     from importlib.metadata import metadata
# except ModuleNotFoundError:
#     from importlib_metadata import metadata
# 
# plugin = metadata('netbox_plugin_extensions')
# 
# 
# class NetboxPluginExtensions(PluginConfig):
#     name = plugin.get('Name').replace('-', '_')
#     verbose_name = plugin.get('Summary')
#     description = plugin.get('Description')
#     version = plugin.get('Version')
#     author = plugin.get('Author')
#     author_email = plugin.get('Author-email')
#     base_url = 'netbox-plugin-extensions'
#     min_version = '3.0'
#     required_settings = []
#     caching_config = {}
#     default_settings = {}
# 
# 
# config = NetboxPluginExtensions

config = NetboxACLPluginConfig
