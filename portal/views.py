from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status, permissions
from .serializers import UserSerializer, FishSerializer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .models import Fish
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
    # permission_classes = [permissions.IsAuthenticated]

class fishList(APIView):

    def get(self, request, format=None):
        fishes = Fish.objects.all()
        serializer = FishSerializer(fishes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FishSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)