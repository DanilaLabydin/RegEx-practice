import re


def main():
    print(re.search(r'[a-zA-Z]{5}', 'a ghost'))
    print(re.search(r'[a-zA-Z]{5}', 'a  scary ghost appeared'))
    print(re.findall(r'[a-zA-Z]{5}', 'a  scary ghost appeared'))
    print(re.findall(r'\b[a-zA-Z]{5}\b', 'a scary ghost appeared'))
    print(re.findall(r'\w{5,12}', 'I really like strawberries'))

    pattern = r'(i|e){2}'

    print(re.findall(r'\b([aeiou]){3,}\b', 'Life is beautiful'))
    print()
    print()
    pattern = r'\ba|e{3}\b'
    print(re.findall(pattern, 'Life is ee beeeautiful '))
    pattern = r'/+'
    print(re.search(pattern, '//'))
    pattern = r'.+'
    print(re.search(pattern, '/'))


if __name__ == '__main__':
    main()
