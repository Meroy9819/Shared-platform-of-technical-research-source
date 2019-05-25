from rest_framework import routers
from django.conf.urls import url, include
from .views import NormalUserViewSet, ExpertViewSet, AdministratorViewSet

router = routers.DefaultRouter()
router.register('Expert', ExpertViewSet)
router.register('Administrator', AdministratorViewSet)
router.register('User', NormalUserViewSet)

urlpatterns = router.urls 