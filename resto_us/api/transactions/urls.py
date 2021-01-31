from rest_framework.routers import DefaultRouter
from .views import transactionViewSet,transactionsListViewSet

router = DefaultRouter()
router.register('data',transactionViewSet,'TransactionViewSet')
router.register('list',transactionsListViewSet,'transactionsListViewSet')

urlpatterns = router.urls
