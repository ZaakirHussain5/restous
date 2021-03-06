from django.shortcuts import render
from rest_framework import viewsets
from .models import restraunt_standards,restraunt
from .serializers import restrauntSerializer,restraunt_standardsSerializer

class restrauntViewSet(viewsets.ModelViewSet):
    serializer_class = restrauntSerializer
    queryset = restraunt.objects.all()

class restraunt_standardsViewSet(viewsets.ModelViewSet):
    serializer_class = restraunt_standardsSerializer

    def get_queryset(self):
        queryset = restraunt_standards.objects.all()
        rest_id = self.request.query_params.get('restraunt',None)
        if rest_id is not None:
            queryset = restraunt_standards.objects.filter(restraunt_id=rest_id)
        return queryset


