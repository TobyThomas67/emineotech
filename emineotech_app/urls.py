from django.urls import path

from . import views


urlpatterns = [
    path('',views.home_page,name="home_page"),
    path('contact_page',views.contact_page,name="contact_page"),
    path('about_page',views.about_page,name="about_page"),
    path('carousel/', views.carousel_view, name='carousel'),
    path('services_page/', views.services_page, name='services_page'),
]
