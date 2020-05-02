import requests

def main():
    res = requests.get("https://fixer-fixer-currency-v1.p.rapidapi.com/latest")
    print(res.status_code)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
