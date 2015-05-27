__author__ = 'Saelind'


def palindrom():
    palin_list = []

    for i in range(100, 999):
        for s in range(100, 999):
            product = i * s
            product_string = str(product)
            product_string_reverse = product_string[::-1]
            if product_string == product_string_reverse:
                if product_string not in palin_list:
                    palin_list.append(product)
    return max(palin_list)


def main():
    palin = palindrom()
    print(palin)


if __name__ == '__main__':
    main()
