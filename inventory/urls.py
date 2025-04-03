from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LguEquipmentViewSet


router = DefaultRouter()
router.register(r'equipments',LguEquipmentViewSet,basename='equipments')

urlpatterns = [
    path('',include(router.urls))
]