from django import forms
from produk.models import Produk


class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = ['nama_produk', 'harga', 'kategori', 'status']

    def clean_nama_produk(self):
        nama = self.cleaned_data['nama_produk']
        if not nama:
            raise forms.ValidationError("Nama produk wajib diisi")
        return nama
