from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from django.conf import settings

from .tables import ACLTable
from .forms import (ACLFilterForm, ACLForm, ACLRenderForm,
                    ACLInterfaceAssignmentForm)
from .filters import ACLFilter
from .models import ACL, ACLInterfaceAssignment


class ACLListView(View):

    queryset = ACL.objects.all()
    filterset = ACLFilter
    filterset_form = ACLFilterForm

    def get(self, request):

        self.queryset = self.filterset(request.GET, self.queryset).qs

        table = ACLTable(self.queryset)
        RequestConfig(request).configure(table)

        return render(request,
                      "netbox_capirca_plugin/acl_list.html",
                      {"table": table,
                       "filter_form": self.filterset_form(request.GET)})


class ACLView(View):

    queryset = ACL.objects.all()

    def get(self, request, pk):
        acl_object = get_object_or_404(self.queryset, pk=pk)

        return render(request,
                      "netbox_capirca_plugin/acl.html",
                      {"object": acl_object})


class ACLCreateView(CreateView):
    form_class = ACLForm
    template_name = "netbox_capirca_plugin/acl_edit.html"

    def get_initial(self):
        config = settings.PLUGINS_CONFIG["netbox_capirca_plugin"]
        return {'static_definitions_dir': config["default_definitions_path"],
                'policy_template_path': config["default_policy_template"]}


class ACLEditView(UpdateView):
    model = ACL
    form_class = ACLForm
    template_name = "netbox_capirca_plugin/acl_edit.html"


class ACLDeleteView(DeleteView):
    model = ACL
    success_url = reverse_lazy("plugins:netbox_capirca_plugin:acl_list")
    template_name = "netbox_capirca_plugin/acl_delete.html"


class ACLRenderView(View):

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


class ACLInterfaceAssignmentCreateView(CreateView):
    form_class = ACLInterfaceAssignmentForm
    template_name = "netbox_capirca_plugin/acl_interface_assignment_edit.html"

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


class ACLInterfaceAssignmentEditView(UpdateView):
    model = ACLInterfaceAssignment
    form_class = ACLInterfaceAssignmentForm
    template_name = "netbox_capirca_plugin/acl_interface_assignment_edit.html"

    def form_valid(self, form):
        interface = form.cleaned_data["interface"]
        self.success_url = reverse_lazy("dcim:interface", kwargs={"pk": interface.pk})

        return super().form_valid(form)
