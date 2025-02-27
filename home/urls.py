from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('inicio_sesion/', views.LogIn.as_view(), name='LogIn'),
    path('logout/', views.LogOut.as_view(), name="LogOut"),
    path("about/", views.about.as_view(), name="about")
]
