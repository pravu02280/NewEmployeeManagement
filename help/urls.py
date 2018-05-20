from django.urls import path
from . import views

app_name = 'help'
urlpatterns = [
    path('help/', views.HelpView.as_view(), name='help'),
]
