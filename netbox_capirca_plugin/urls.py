from django.urls import path

from .views import (ACLListView, ACLView, ACLEditView, ACLCreateView,
                    ACLDeleteView, ACLRenderView,
                    ACLInterfaceAssignmentCreateView,
                    ACLInterfaceAssignmentEditView)


urlpatterns = [
    path("acl/", ACLListView.as_view(), name="acl_list"),
    path("acl/add/", ACLCreateView.as_view(), name="acl_add"),
    path("acl/<int:pk>/", ACLView.as_view(), name="acl"),
    path("acl/<int:pk>/edit", ACLEditView.as_view(), name="acl_edit"),
    path("acl/<int:pk>/delete", ACLDeleteView.as_view(), name="acl_delete"),
    path("acl/<int:pk>/render/", ACLRenderView.as_view(), name="acl_render"),
    path("acl-interface-assignment/add/",
         ACLInterfaceAssignmentCreateView.as_view(),
         name="acl_interface_assignment_add"),
    path("acl-interface-assignment/<int:pk>/edit/",
         ACLInterfaceAssignmentEditView.as_view(),
         name="acl_interface_assignment_edit"),
    ]
