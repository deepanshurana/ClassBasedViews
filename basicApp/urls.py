from django.urls import path
from . import views

app_name = 'basicApp'
urlpatterns = [
    path('', views.schoolListView.as_view(), name='list'),
]
