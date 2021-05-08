import Productcheck as p


def buy(product, num, price):
    if p.check(product, num):
        print('You bought', product, 'and spent', num * price)
    else:
        print('Sorry! We are out of this product')


def main():
    buy('pen', 10, 4)
    buy('p', 10, 4)
    buy('pen', 10, 60)


if __name__ == "__main__":
    main()