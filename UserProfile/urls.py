
from django.contrib import admin
from django.urls import path
from UserProfile.views import registrations, login, index, logout_view, user_profile

app_name='UserProfile'

urlpatterns = [
    path('', index, name='index'),
    path('registrations/', registrations, name='registrations'),
    path('login/', login, name='login'),
    path('User/<str:username>', user_profile, name='user_profile'),
    path('logout/', logout_view, name='logout'),
    # path('otp/', gootp, name='gootp'),
]