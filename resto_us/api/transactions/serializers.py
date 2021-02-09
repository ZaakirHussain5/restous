from rest_framework import serializers
from api.restraunt.serializers import restrauntSerializer,restraunt_standardsSerializer
from api.user.serializers import resto_user_serailazer
from .models import transaction,UserDealSubscription

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = '__all__'

class DealSubscriptionSerializer(serializers.ModelSerializer):
    users_id = resto_user_serailazer()
    restraunt_id = restraunt_standardsSerializer()
    class Meta:
        model = UserDealSubscription
        fields = '__all__'

class transactionsListSerializer(serializers.ModelSerializer):
    users_id = resto_user_serailazer()
    restraunt_id = restrauntSerializer()
    class Meta:
        model = transaction
        fields = '__all__'




