from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.home_page, name = "home"),
    path("<int:page>", views.home_page, name = "home_paginate"),

    path('tags/', views.TagListView.as_view(), name = 'tags'),
    path('tags/add/', views.AddTagView.as_view(), name = 'add_tag'),
    path('tags/<int:tag_id>/', views.EditTagView.as_view(), name = 'edit_tag'),

    path('quotes/<int:quote_id>/', views.QuoteFormList.as_view(), name = 'quote'),
    path('quotes/add/', views.QuoteFormView.as_view(), name = 'quote_add'),
    path('quotes/edit/<int:quote_id>/', views.QuoteFormView.as_view(), name = 'quote_update'),
    path('quotes/delete/<int:quote_id>/', views.QuoteDeleteView.as_view(), name='quote_delete'),

    path('authors/<int:author_id>', views.AuthorListView.as_view(), name = 'author'),
    path('authors/add/', views.AuthorFormView.as_view(), name = 'author_add'),
    path('authors/<int:author_id>/', views.AuthorFormView.as_view(), name = 'author_update'),
    path('authors/delete/<int:author_id>/', views.AuthorDeleteView.as_view(), name = 'author_delete'),

    path('tuning/', views.TuningView.as_view(), name = 'tuning'),
    path('tuning/scraping', views.ScrapingView.as_view(), name = 'scraping'),
    path('tuning/gptchat', views.GPTChatView.as_view(), name = 'gptchat'),

]
