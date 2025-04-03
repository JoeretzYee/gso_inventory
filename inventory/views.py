from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import LguEquipment
from .serializers import LguEquipmentSerializer

class LguEquipmentViewSet(ModelViewSet):
    queryset = LguEquipment.objects.all()
    serializer_class = LguEquipmentSerializer
    authentication_classes = [JWTAuthentication, SessionAuthentication]  # ✅ Ensure proper authentication
    permission_classes = [IsAuthenticated]  # ✅ Require authentication
