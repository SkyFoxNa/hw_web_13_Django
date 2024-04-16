from django.urls import path

from . import views

app_name = "tuning"

urlpatterns = [
    path('tuning/', views.TuningView.as_view(), name = 'tuning'),
    path('tuning/scraping', views.ScrapingView.as_view(), name = 'scraping'),
    path('tuning/gptchat', views.GPTChatView.as_view(), name = 'gptchat'),
]
