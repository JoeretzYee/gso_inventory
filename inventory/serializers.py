from rest_framework import serializers
from .models import LguEquipment, Classification

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'  # This will return all fields in GET request

class LguEquipmentSerializer(serializers.ModelSerializer):
    classification = serializers.PrimaryKeyRelatedField(
        queryset=Classification.objects.all(),  # Accept only ID in POST
        write_only=True  # Prevent classification ID from appearing in GET response
    )

    classification_details = ClassificationSerializer(source="classification", read_only=True)  # Include full classification details in GET

    class Meta:
        model = LguEquipment
        fields = [
            "id",
            "article",
            "description",
            "property_number",
            "cost",
            "location",
            "condition",
            "remarks",
            "classification",  # Used in POST (ID only)
            "classification_details"  # Used in GET (Full object)
        ]
