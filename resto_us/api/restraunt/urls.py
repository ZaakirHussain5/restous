from rest_framework import routers
from .views import restrauntViewSet,restraunt_standardsViewSet
from django.urls import path,include

router = routers.DefaultRouter()
router.register('data',restrauntViewSet,'restrauntViewSet')
router.register('deals',restraunt_standardsViewSet,'restraunt_standardsViewSet')

urlpatterns = [
    path('',include(router.urls))
]
 