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

Create directories for your capirca network and service definitions and
policy templates.

# Configuration

Add the plugin to the netbox config.
```
PLUGINS = ["netbox_capirca_plugin"]
```

This plugin has there configuration parameters:

* `policy_base_path` - The directory in which the policies are
* `definitions_base_path` - The directory where the definitions are
* `default_definitions_path` - The default path for static network and service
  definitions (relative to `definitions_base_path`)
* `default_policy_template` - The default template for policies (relative to
  `policy_base_path`)

In the configuration this looks e.g. like this

```
PLUGINS_CONFIG = {
    'netbox_capirca_plugin': {
        'default_definitions_path': 'defs/',
        'default_policy_template': 'main.pol.j2',
        'policy_base_path': '/opt/capirca/policies/',
        'definitions_base_path': '/opt/capirca/',
    }
}
```

# Policy-Templates

The policy templates are Jinja2 Templates that are rendered into capirca policy
files.
The ACL object can be accessed as `acl` in the template.
A simple template looks like this:

```
header {
	comment:: "{{ acl.description }}"
	target:: cisco {{ acl.name }} mixed
	target:: ciscoxr {{ acl.name }} mixed
}
{{ acl.terms }}
```

# API

ACLs and ACLInterfaceAssignments can also be managed via the API. The API docs
can be found where the regular Netbox API docs of your installation are. 
