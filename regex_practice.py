import re
import string


def main():
    # simple example
    result = re.match('You', 'Young Frankenstein')
    print(result)

    # match - maps only in the beginning of the source
    # search - maps a first match
    # findall - returns a list of all matches if there are
    # split - split a source for matches and returns it
    # sub - takes an argument for replacing all matching parts of a source
    source = 'Young Frankenstein'
    m = re.findall('n.', source)
    print(m)

    m = re.findall('n.?', source)
    print(m)

    m = re.split('n', source)
    print(m)

    m = re.sub('n', '!', source)
    print(m)

    # special symbols
    printable = string.printable
    print(len(printable))
    print(f'{printable[:50]}\n{printable[50:]}')

    pattern = r'\d'
    print(f"any digital symbol: {re.findall(pattern, printable)}\n")
    pattern = r'\D'
    print(f"any non digital symbol: {re.findall(pattern, printable)}\n")

    pattern = r'\w'
    print(f"any word or digit or underscore symbol: {re.findall(pattern, printable)}\n")
    pattern = r'\W'
    print(f"any non word or digit or punctuation symbol: {re.findall(pattern, printable)}\n")

    pattern = r'\s'
    print(f"any space symbol: {re.findall(pattern, printable)}\n")
    pattern = r'\S'
    print(f"any non space symbol: {re.findall(pattern, printable)}\n")

    pattern = r'\b'
    print(f"a word border: {re.findall(pattern, printable)}\n")
    pattern = r'\B'
    print(f"a non border: {re.findall(pattern, printable)}\n")

    source = '''I wish I may, I wish I might Have a dish of fish tonight'''

    # find 'wish'
    print(re.findall('wish', source))

    # find 'fish' or 'wish'
    print(re.findall('fish|wish', source))

    # find 'wish' on the beginning
    print(re.findall('^wish', source))

    # find 'I wish' on the beginning
    print(re.findall('^I wish', source))

    # find 'fish' in the end
    print(re.findall('fish$', source))

    # find 'fish tonight' on the beginning
    print(re.findall('fish tonight$', source))



if __name__ == '__main__':
    main()
