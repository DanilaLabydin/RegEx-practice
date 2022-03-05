##
# intro of regular expressions
#
import re


def compare_verb(user_input, verb_v2, verb_v3):
    """The function compares user's input with certain verb"""
    return bool(re.search(r'^' + verb_v2 + ' *' + verb_v3 + '$', user_input.lower()))


def main():
    log = "July 31 05 02:45:13 [d]mycomputer [12345] bad_process: erroe"
    regex = r"\[(\d*)\]"
    result = re.search(regex, log)
    print(result[1])
    result = re.split(r'[.?!]', 'One sentence. Another one! Yes?')
    print(result)

    print(compare_verb('DID   s  done', 'did', 'done'))
    a = {[1,2,3], 'ff'}
    print(a)


if __name__ == '__main__':
    main()
