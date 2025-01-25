from django.urls import path, include
from .views import Get_Users,Get_User,Create_User,Update_User,Delete_User

urlpatterns = [
   
    path('users/',Get_Users,name="get_users"),
    path('user/',Get_User, name='get_user'),
    path('createuser',Create_User, name='create_user'),
    path('updateuser/<int:pk>/',Update_User, name='update_user'),
    path('deleteuser/<int:pk>/',Delete_User, name='delete_user'),
    
]