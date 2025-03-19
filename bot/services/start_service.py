import requests
from config.setting import BASE_URL

API = f"{BASE_URL}/api/data"

async def post_data(payload: dict):
    try:
        response = requests.post(API, json=payload)

        if response.status_code in [200, 201]:
            return True, "Data berhasil terkirim!"
        else:
            return False, f"Data gagal terkirim, {response.status_code} & {response.text}"
        
    except Exception as e:
        return False, f"Terjadi error: {str(e)}"