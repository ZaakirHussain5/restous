from rest_framework import routers
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('add',views.userViewSet,'UserView')
router.register('list',views.userListViewSet,'UserView')

urlpatterns = [
    path('login/',views.signIn,name='signIn'),
    path('a-login/',views.adminSignIn,name='signIn'),
    path('logout/<int:id>/',views.signout,name='Logout'),
    path('',include(router.urls))
]