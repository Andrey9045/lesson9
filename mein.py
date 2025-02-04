import requests


LOCATION = [
    'london',
    'svo',
    'Череповец',
]
PAYLOAD = {
    'n': '',
    'T': '',
    'q': '',
    'M': '',
    'm': '',
    'lang': 'ru',
}


def main():
    for a in LOCATION:
        url = 'https://wttr.in/{}'.format(a)
        response = requests.get(url, params=PAYLOAD)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
