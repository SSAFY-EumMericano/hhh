from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from .views import DiningStoreViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"Dining/Stores", DiningStoreViewSet, basename="dining_stores")

urlpatterns = router.urls
