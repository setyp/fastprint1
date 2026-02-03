from django.urls import path
from produk.views_api import produk_api_list
from .views import produk_list, produk_create, produk_edit, produk_delete

urlpatterns = [
    path("", produk_list, name="produk_list"),
    path("tambah/", produk_create, name="produk_create"),
    path("edit/<int:id>/", produk_edit, name="produk_edit"),
    path("hapus/<int:id>/", produk_delete, name="produk_delete"),
    path('api/produk/', produk_api_list, name='produk_api'),
]
