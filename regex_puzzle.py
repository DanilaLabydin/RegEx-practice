import re


def main():
    pattern = r'(AN|FE|BE)'
    print(re.search(pattern, 'BE'))
    pattern = r'(AB|OE|SK)'
    print(re.search(pattern, 'OE'))
    pattern = r'(A|B|C)\1'
    print(re.search(pattern, 'AB'))
    pattern = r'.*M?O.*'
    print(re.search(pattern, 'BO'))


if __name__ == '__main__':
    main()
