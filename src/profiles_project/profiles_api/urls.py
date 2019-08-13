from django.conf.urls import url, include
from . import views

from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login') # Necesitamos el base_name porque no es una modelviewset de django, por lo que django necesita saber cómo llamar a la ruta
router.register('feed', views.UserProfileFeedViewSet) # No es necesario poner base_name ya que es una modelviewswt

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls)),

]
