from django.urls import path
from .import views
urlpatterns = [
    path('home/',views.home.as_view(),name = 'Home'),
    # path('about/',views.about.as_view(),name = 'about')
]
