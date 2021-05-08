products = {
    'candy': 10,
    'juice': 5,
    'pen': 50
}


def check(product, num):
    return product in products and products[product] >= num
