from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin

from .tables import ACLTable
from .forms import (ACLFilterForm, ACLForm, ACLRenderForm,
                    ACLInterfaceAssignmentForm)
from .filters import ACLFilter
from .models import ACL, ACLInterfaceAssignment

from netbox_plugin_extensions.views import generic


class ACLListView(generic.PluginObjectListView):

    queryset = ACL.objects.all()
    filterset = ACLFilter
    filterset_form = ACLFilterForm
    table = ACLTable
    action_buttons = ('add')


class ACLView(generic.PluginObjectView):

    queryset = ACL.objects.all()


class ACLCreateView(generic.PluginObjectEditView):
    queryset = ACL.objects.all()
    model_form = ACLForm
    form_class = ACLForm
    template_name = "netbox_capirca_plugin/acl_edit.html"

    def get_initial(self):
        config = settings.PLUGINS_CONFIG["netbox_capirca_plugin"]
        return {'policy_template_path': config["default_policy_template"]}


class ACLEditView(generic.PluginObjectEditView):
    model_form = ACLForm
    queryset = ACL.objects.all()
    template_name = "netbox_capirca_plugin/acl_edit.html"


class ACLDeleteView(generic.PluginObjectDeleteView):
    queryset = ACL.objects.all()


class ACLRenderView(View, PermissionRequiredMixin):

    permission_requiered = "netbox_capirca_plugin.view_acl"

    queryset = ACL.objects.all()

    def get(self, request, pk):
        acl_object = get_object_or_404(self.queryset, pk=pk)

        form = ACLRenderForm(acl_object)

        return render(request,
                      "netbox_capirca_plugin/acl_render.html",
                      {"object": acl_object, "form": form})

    def post(self, request, pk):
        acl_object = get_object_or_404(self.queryset, pk=pk)

        form = ACLRenderForm(acl_object, request.POST)
        if form.is_valid():
            acl_text = acl_object.render(form.cleaned_data["target"], form.cleaned_data["options"])

            return render(request,
                          "netbox_capirca_plugin/acl_render_response.html",
                          {"object": acl_object, "acl_text": acl_text})

        return render(request,
                      "netbox_capirca_plugin/acl_render.html",
                      {"object": acl_object, "form": form})


class ACLInterfaceAssignmentCreateView(generic.PluginObjectEditView):
    model_form = ACLInterfaceAssignmentForm
    queryset = ACLInterfaceAssignment.objects.all()
    #template_name = "netbox_capirca_plugin/acl_interface_assignment_edit.html"

    def get_interface_id(self):
        interface_id = self.request.GET.get("interface_id", None)
        if interface_id is not None:
            interface_id = int(interface_id)
        return interface_id

    def get_initial(self):
        interface_id = self.get_interface_id()
        result = {}
        if interface_id is not None:
            result["interface"] = interface_id
        return result

    def form_valid(self, form):
        interface = form.cleaned_data["interface"]
        self.success_url = reverse_lazy("dcim:interface", kwargs={"pk": interface.pk})

        return super().form_valid(form)


class ACLInterfaceAssignmentEditView(generic.PluginObjectEditView):
    form_class = ACLInterfaceAssignmentForm
    queryset = ACLInterfaceAssignment.objects.all()
    #template_name = "netbox_capirca_plugin/acl_interface_assignment_edit.html"
    template_name = "generic/object_edit.html"

    def form_valid(self, form):
        interface = form.cleaned_data["interface"]
        print(interface)
        self.success_url = reverse_lazy("dcim:interface", kwargs={"pk": interface.pk})

        return super().form_valid(form)
