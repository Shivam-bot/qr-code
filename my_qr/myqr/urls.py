from django.urls import path
from .views import home_view,user_form
urlpatterns = [
    
    path('',home_view,name='home-view'),
    path('register',user_form,name='user-register'),
    
]