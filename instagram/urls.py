from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns=[
    path('',views.indexView,name="home"),
    path('dashbord/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_url"),
    path('register/',views.registerView,name="register_url"),
    path('logout/',LogoutView.as_view(next_page='dashboard'),name="logout"),
    path('like',views.like_api,name="like"),
    path('unlike',views.unlike_api,name="unlike"),
    path('home',views.homeView,name="home"),
    path('editprofile',views.editView,name="edit"),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)