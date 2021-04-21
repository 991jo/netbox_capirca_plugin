from rest_framework import routers
from .views import ACLViewSet, ACLInterfaceAssignmentViewSet

router = routers.DefaultRouter()
router.register("acls", ACLViewSet)
router.register("acls-interface-assignments", ACLInterfaceAssignmentViewSet)
urlpatterns = router.urls
