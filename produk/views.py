from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Kategori, Produk, Status
from .forms import ProdukForm

def produk_list(request):
    produk = Produk.objects.filter(
        status__nama_status__iexact='bisa dijual'
    ).select_related('kategori', 'status')
    context = {
        'produk': produk
    }
    return render(request, 'produk/list.html', context)

def produk_create(request):
    kategori_list = Kategori.objects.all()
    status_list = Status.objects.all()
    if request.method == "POST":
        nama_produk = request.POST.get("nama_produk")
        harga = request.POST.get("harga")
        kategori_id = request.POST.get("kategori")
        status_id = request.POST.get("status")
        if not nama_produk:
            messages.error(request, "Nama produk wajib diisi")
        elif not harga.isdigit():
            messages.error(request, "Harga harus angka")
        else:
            Produk.objects.create(
                nama_produk=nama_produk,
                harga=int(harga),
                kategori_id=kategori_id,
                status_id=status_id
            )
            return redirect("produk_list")
    return render(request, "produk/form.html", {
        "kategori_list": kategori_list,
        "status_list": status_list,
        "title": "Tambah Produk"
    })


def produk_edit(request, id):
    produk = Produk.objects.get(id=id)
    kategori_list = Kategori.objects.all()
    status_list = Status.objects.all()
    if request.method == "POST":
        nama_produk = request.POST.get("nama_produk")
        harga = request.POST.get("harga")
        kategori_id = request.POST.get("kategori")
        status_id = request.POST.get("status")
        if not nama_produk:
            messages.error(request, "Nama produk wajib diisi")
        elif not harga.isdigit():
            messages.error(request, "Harga harus angka")
        else:
            produk.nama_produk = nama_produk
            produk.harga = int(harga)
            produk.kategori_id = kategori_id
            produk.status_id = status_id
            produk.save()
            return redirect("produk_list")
    return render(request, "produk/form.html", {
        "produk": produk,
        "kategori_list": kategori_list,
        "status_list": status_list,
        "title": "Edit Produk"
    })

def produk_delete(request, id):
    produk = get_object_or_404(Produk, id=id)
    if request.method == "POST":
        produk.delete()
    return redirect("produk_list")

