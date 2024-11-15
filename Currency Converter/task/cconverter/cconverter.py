import requests

code = input()

response = requests.get(f'http://www.floatrates.com/daily/{code.lower()}.json')
data = response.json()

cache: dict[str, float] = {
    'USD': data['usd']['rate'] if code.upper() != 'USD' else 1,
    'EUR': data['eur']['rate'] if code.upper() != 'EUR' else 1
}


def get_rate(curr: str) -> float:
    print('Checking the cache...')
    if curr.upper() in cache:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache[curr.upper()] = data[curr.lower()]['rate']
    return cache[curr.upper()]


while True:
    currency = input()
    if not currency:
        break
    value = float(input())
    print(f'You received {value*get_rate(currency):.2f} {currency}.')
