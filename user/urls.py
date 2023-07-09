from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .auths import register, login


urlpatterns = [
    path('login/', login.login_user, name='login'),
    path('register/', register.register, name='register'),
    # path('logout/', logout.signout, name='logout'),


]
