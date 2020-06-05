from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home_page'),
    path('message/',views.message,name='message_page')

]