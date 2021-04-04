from django.contrib import admin
from .models import ACL, ACLInterfaceAssignment


@admin.register(ACL)
class ACLAdmin(admin.ModelAdmin):
    list_display = ("name", "description",)

@admin.register(ACLInterfaceAssignment)
class ACLAdmin(admin.ModelAdmin):
    list_display = ("interface", "ingress", "egress")
