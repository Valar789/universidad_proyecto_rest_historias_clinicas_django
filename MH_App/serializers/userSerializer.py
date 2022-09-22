from rest_framework import serializers
from MH_App.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'occupation', 'name', 'email']

    def create(self, validated_data):
        UserInstance = User.objects.create(**validated_data)
        return UserInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            'id': user.id, 'username': user.username,  'occupation': user.occupation, 'name': user.name, 'email': user.email
        }
