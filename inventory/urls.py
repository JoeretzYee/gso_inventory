from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import LguEquipmentViewSet,ClassificationViewSet


router = DefaultRouter()
router.register(r'equipments',LguEquipmentViewSet,basename='equipments')
router.register(r'classification',ClassificationViewSet,basename='classification')

urlpatterns = [
    path('',include(router.urls))
]