import requests

API_KEY = "INSERT_YOUR_API_KEY_HERE"

def main():
    response = requests.get(
        "https://healthchecks.io/api/v1/checks/",
        headers={"X-Api-Key":API_KEY},
        params={},
        timeout=5,
    )

    for i in response.json()['checks']:
        if i['status'] == 'down':
            print('down')
            break
    print('up')

if __name__ == '__main__':
    main()