import requests

API_KEY = "INSERT_YOUR_API_KEY_HERE"

def main():
    response = requests.get(
        "https://healthchecks.io/api/v1/checks/",
        headers={"X-Api-Key":API_KEY},
        params={},
        timeout=5,
    )
    
    for check in response.json()['checks']:
        if check['status'] == 'down':
            print('down')
            break
    print('up')

if __name__ == '__main__':
    try:
        main()
    except:
        # specify what to do if there is an error
        # generally lack of internet connection
        print('up')
        # print('down')
