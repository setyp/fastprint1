import requests
import hashlib
import datetime
import re

def get_produk_api():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

    try:
        r1 = requests.get(url, timeout=10)
        raw_username = r1.headers.get("X-Credentials-Username")
        username = raw_username.split(" ")[0].strip()
        username = re.sub(r"[^a-zA-Z0-9]", "", username)

        if not username:
            return {
                "error": 1,
                "ket": "Username tidak ditemukan di response header"
            }

        today = datetime.date.today()
        raw_password = f"bisacoding-{today.day:02d}-{today.month:02d}-{str(today.year)[-2:]}"
        password = hashlib.md5(raw_password.encode()).hexdigest()

        payload = {
            "username": username,
            "password": password
        }

        r2 = requests.post(
            url,
            data=payload,
            timeout=10
        )
        return r2.json()

    except Exception as e:
        return {
            "error": 1,
            "ket": str(e)
        }
