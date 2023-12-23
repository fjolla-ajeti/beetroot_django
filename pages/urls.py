from django.urls import path
from .views import HomePageView
from .views import AboutPageView

urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('aboutPage/', AboutPageView.as_view(), name='about_page'),
]