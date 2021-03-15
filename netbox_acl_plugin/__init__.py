__version__ = "0.1.0"

from extras.plugins import PluginConfig


class NetboxACLPluginConfig(PluginConfig):
    name = 'netbox_acl_plugin'
    verbose_name = 'netbox ACL Plugin'
    description = 'A plugin for ACL management in netbox',
    version = __version__
    author = 'Johannes Erwerle'
    author_email = 'erwerle@belwue.de'
    required_settings = []
    base_url = "netbox-acl-plugin"
    default_settings = {
        'loud': False
    }


config = NetboxACLPluginConfig
