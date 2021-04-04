from .exceptions import UnsupportedTarget
from django.core.exceptions import ValidationError


class ACLRenderOptionValidator:

    def __init__(self, acl):
        self.acl = acl

    def __call__(self, target):
        try:
            self.acl.get_render_function()
        except UnsupportedTarget:
            raise ValidationError(f"target { target } is not supported by ACL { self.acl }.")
