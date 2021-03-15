from django.shortcuts import render
from .models import Pizza
from .serializers import PizzaSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PizzaViewSet(viewsets.ModelViewSet):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
