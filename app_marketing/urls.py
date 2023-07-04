from django.contrib import admin
from django.urls import path , include


from .views import      ClientesListView   \
                    ,   ClientesDetailView \
                    ,   ClientesCreateView \
                    ,   ClientesUpdateView \
                    ,   ClientesDeleteView

app_name = "clientes"

urlpatterns = [
    path("", ClientesListView.as_view(), name="all"),
    path("create/", ClientesCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", ClientesDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", ClientesUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", ClientesDeleteView.as_view(), name="delete")

]