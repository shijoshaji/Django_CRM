
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.lead_list, name='leadList'),
    path('<int:pk>/', views.lead_detail, name='leadDetail'),
    path('create/', views.lead_create, name='leadCreate'),
]
