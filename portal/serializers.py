from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Fish


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'groups']
        
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            password = make_password(validated_data['password'])
        )
        return user


class FishSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Fish
        fields = ['owner', 'fish_id', 'fish_size', 'fish_price', 'status', 'createdDate', 'modifiedDate']