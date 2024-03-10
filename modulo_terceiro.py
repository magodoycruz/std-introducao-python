# pip3 install requests
# Importação e uso de módulo terceiro

import requests

url = "https://www.example.com"
response = requests.get(url)
print(response.status_code)

# Pacotes de terceiros: https://pypi.org/