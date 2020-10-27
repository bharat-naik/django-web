from django.urls import path,include
from . import views


urlpatterns = [
    path('' ,views.index , name='index' ),
    path('chat' ,views.chat , name='chat' ),
    path('accounts/' , include('django.contrib.auth.urls')),
    path('register' ,views.register , name='register' ),
]