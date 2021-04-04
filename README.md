# Netbox ACL Plugin

This plugin tries to implement a simple abstraction for Access Control Lists
(ACLs) in netbox by leveraging the capirca ACL abstraction.

ACLs are generated from multiple data sources.

- directories that contain static network and service definitions
- jinja2 templates for policies
- per ACL network and service definitions
- terms that are put into the policy template

ACLs can either exist on their own or can be assigned to interfaces, either as
ingress or egress ACL.
ACLs can be rendered with the capirca generators. Currently only Cisco IOS and
IOS XR are supported. If you need more, just add an issue. Supporting an other
generator is relativly easy.

# Installation

Install the package in your netbox environment. How to do this depends on
the way you habe build your netbox environment.

Create a directories for your capirca network and service definitions and
policy templates.

# Configuration

Add the plugin to the netbox config.
```
PLUGINS = ["netbox_capirca_plugin"]
```

This plugin has currently 2 configuration parameters:

* `default_definitions_path` - The default path for static network and service
  definitions
* `default_policy_template` - The default template for policies

In the configuration this looks e.g. like this

```
PLUGINS_CONFIG = {
    'netbox_capirca_plugin': {
        'default_definitions_path': '/opt/capirca/defs/',
        'default_policy_template': '/opt/capirca/policies/main.pol.j2'
    }
}
```
