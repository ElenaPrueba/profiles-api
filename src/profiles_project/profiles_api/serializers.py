from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serializers"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Un serializer para nuestro (objeto) perfil de usuario"""

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {'password': {'write_only': True}} #La cobntraseña no puede ser leída

    def create(self, validated_data):
        """Crear y devolver un nuevo usuario"""

        user = models.UserProfile(
            email= validated_data['email'],
            name=validated_data['name']
            )

        user.set_password(validated_data['password'])
        user.save()

        return user
