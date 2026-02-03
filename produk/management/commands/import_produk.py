from django.core.management.base import BaseCommand
from produk.models import Produk, Kategori, Status
from produk.getdata import get_produk_api


class Command(BaseCommand):
    help = "Import data produk dari API Fastprint"

    def handle(self, *args, **kwargs):
        result = get_produk_api()

        if result.get("error") != 0:
            self.stderr.write(
                self.style.ERROR(f"Gagal ambil data API: {result.get('ket')}")
            )
            return

        data = result.get("data", [])

        for item in data:
            kategori, _ = Kategori.objects.get_or_create(
                nama_kategori=item["kategori"]
            )

            status, _ = Status.objects.get_or_create(
                nama_status=item["status"]
            )

            Produk.objects.update_or_create(
                nama_produk=item["nama_produk"],
                defaults={
                    "harga": item["harga"],
                    "kategori": kategori,
                    "status": status
                }
            )

        self.stdout.write(
            self.style.SUCCESS("Data produk berhasil diimport")
        )
