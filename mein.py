import requests


def weather_london():
    url = 'https://wttr.in/london?nTqu&lang=en'
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


def weather_svo():
    url = 'https://wttr.in/svo?nTqu&lang=en'
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


def weather_cherepovets():
    url = 'https://wttr.in/Череповец?nTqMm&lang=ru'
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)


def main():
    weather_london()
    weather_svo()
    weather_cherepovets()


if __name__ == '__main__':
    main()
