from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register, name="reg"),
    path('profile/',views.profile,name='pro'),
    path('logout/',views.logout,name='logo'),  
    path('sendotp/',views.send_otp,name='sdo'),
    path('resetpwd/<int:id>/',views.resetpwd,name='reset'),  
    path('',views.login, name='logi'),
]