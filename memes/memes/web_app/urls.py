from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'home', views.homeView,name='home'),
    url(r'^login', views.login_request, name='login'),
    url(r'^user-profile', views.user_profile, name='user_profile'),
    url(r'^user-data', views.user_data, name='user_data'),
    url(r'^logout', views.logout_request, name='logout'),
]
