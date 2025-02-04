import requests

def get_ip_info(ip=""):
    url = f"http://ipinfo.io/{ip}/json"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        return {"error": str(e)}

# Example Usage:
ip_address = input("Enter IP address (leave blank for your own IP): ")
info = get_ip_info(ip_address)

for key, value in info.items():
    print(f"{key}: {value}")