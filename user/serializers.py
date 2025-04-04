from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(required=False)  # Add this line

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']  # Include 'username'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Generate username from email
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user