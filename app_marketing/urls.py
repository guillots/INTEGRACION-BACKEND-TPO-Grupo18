from django.contrib import admin
from django.urls import path
from .views import UserSignup, UserLogin, PersonCreate, PersonList, PersonDetail, PersonUpdate, PersonDelete
from django.contrib.auth.views import LogoutView
from .views import User



# from .views import      ClientesListView   \
#                     ,   ClientesDetailView \
#                     ,   ClientesCreateView \
#                     ,   ClientesUpdateView \
#                     ,   ClientesDeleteView

# app_name = "app_marketing"

urlpatterns = [
    path('signup/', UserSignup.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('person-create/', PersonCreate.as_view(), name ='personcreate'),
    path('', PersonList.as_view(), name='personlist'),
    path('person-detail/pk=<int:pk>', PersonDetail.as_view(), name='persondetail'),
    path('person-update/pk=<int:pk>', PersonUpdate.as_view(), name='personupdate'),
    path('person-delete/pk=<int:pk>', PersonDelete.as_view(), name='persondelete'),

]