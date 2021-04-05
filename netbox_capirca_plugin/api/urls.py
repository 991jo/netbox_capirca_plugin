from rest_framework import routers
from .views import ACLViewSet, ACLInterfaceAssignmentViewSet

router = routers.DefaultRouter()
router.register("acls", ACLViewSet)
router.register("acls-interfacea-assignments", ACLInterfaceAssignmentViewSet)
urlpatterns = router.urls
