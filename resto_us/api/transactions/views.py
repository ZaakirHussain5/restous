from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializers import transactionSerializer,transactionsListSerializer,DealSubscriptionSerializer
from .models import transaction,UserDealSubscription
from api.restraunt.models import restraunt,restraunt_standards
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

class userDealAPI(generics.RetrieveAPIView):
    serializer_class = DealSubscriptionSerializer

    def get_object(self):
        userId = self.request.query_params('id',None)
        return UserDealSubscription.objects.get(users_id=userId)


@csrf_exempt
def activateDeal(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error":"Not Logged In"})
    if not request.method == 'POST':
        return JsonResponse({"error":"Method "+request.method + " Not allowed."})
    code = request.POST["code"]
    deal_id = request.POST["deal_id"]
    try:
        deal = restraunt_standards.objects.get(id=deal_id)
        resto = restraunt.objects.get(id=deal.restraunt_id.id)
        if resto.rest_code == code:
            UserDealSubscription.objects.create(users_id=request.user,subscription=deal,meals_remaining=deal.no_of_meals)
            return JsonResponse({"success":"Deal Subscription Activated"})
        else:
            return JsonResponse({"error": "Invalid Restraunt Code."})
    except restraunt_standards.DoesNotExist:
        return JsonResponse({"error":"Invalid Deal ID"})

