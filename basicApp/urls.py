from django.urls import path
from . import views

app_name = 'basicApp'
urlpatterns = [
    path('', views.schoolListView.as_view(), name='list'),
    path('<int:pk>/', views.schoolDetailView.as_view(), name='detail'),
    path('create/', views.schoolCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.schoolUpdateView.as_view(), name='update'),
]
