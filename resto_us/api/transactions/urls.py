from django.urls import include,path
from rest_framework.routers import DefaultRouter
from .views import transactionViewSet,transactionsListViewSet,activateDeal

router = DefaultRouter()
router.register('data',transactionViewSet,'TransactionViewSet')
router.register('list',transactionsListViewSet,'transactionsListViewSet')

urlpatterns = [
    path('',include(router.urls)),
    path('activateSubscription',activateDeal,name="activateDeal")
]
