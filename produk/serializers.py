from rest_framework import serializers
from .models import Produk
class ProdukSerializer(serializers.ModelSerializer):
    kategori = serializers.CharField(source='kategori.nama_kategori')
    status = serializers.CharField(source='status.nama_status')
    class Meta:
        model = Produk
        fields = ['id', 'nama_produk', 'harga', 'kategori', 'status']
