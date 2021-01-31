from django.shortcuts import render
from rest_framework import viewsets
from .serializers import transactionSerializer,transactionsListSerializer
from .models import transaction

class transactionViewSet(viewsets.ModelViewSet):
    queryset = transaction.objects.all()
    serializer_class = transactionSerializer

class transactionsListViewSet(viewsets.ModelViewSet):
    serializer_class = transactionsListSerializer

    def get_queryset(self):
        queryset = transaction.objects.all()
        rest_id = self.request.query_params.get('restraunt_id',None)
        user_id = self.request.query_params.get('user_id',None)
        if rest_id is not None:
            queryset = transaction.objects.filter(restraunt_id=res_id)
        if user_id is not None:
            queryset = transaction.objects.filter(users_id=user_id)
        return queryset
