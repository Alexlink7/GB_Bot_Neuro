import requests


def fox():
    url = 'https://randomfox.ca/floof'

    response = requests.get(url)
    # response.raise_for_status()

    return response.json().get('image')


if __name__ == '__main__':
    print(fox())