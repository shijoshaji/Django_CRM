
from django.urls import path, include
from . import views

urlpatterns = [

    #NOTE: CBV
    path('', views.LeadListView.as_view(), name='leadList'),
    path('<int:pk>/', views.LeadDetailView.as_view(), name='leadDetail'),
    path('create/', views.LeadCreateView.as_view(), name='leadCreate'),
    path('<int:pk>/update/', views.LeadUpdateView.as_view(), name='leadUpdate'),
    path('<int:pk>/delete/', views.LeadDeleteView.as_view(), name='leadDelete'),
    

    # NOTE: FBV
    # path('', views.lead_list, name='leadList'),
    # path('<int:pk>/', views.lead_detail, name='leadDetail'),
    # path('<int:pk>/update/', views.lead_update, name='leadUpdate'),
    # path('<int:pk>/delete/', views.lead_delete, name='leadDelete'),
    # path('create/', views.lead_create, name='leadCreate'),
]
