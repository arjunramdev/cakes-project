from django.urls import path

from .import views


urlpatterns = [

path('cakes/',views.CakeListCreateView.as_view()),

path('cakes/<int:id>/',views.CakeRetrieveUpdateDestroyView.as_view())


]