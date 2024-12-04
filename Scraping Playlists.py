import requests

year = input("\nEntrez une année ")
response = requests.get(f"https://www.frequenceplus.fr/top/hits-{year}")
print(response.raise_for_status())

with open('index.html', 'w', encoding="utf-8") as f:
    f.write(response.text)