from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .import views
urlpatterns = [

    path('login/',views.LoginView.as_view()),
    path('register/',views.RegisterView.as_view())

]