import re


def main():
    mad_text = open('mad_text.txt', 'r')
    text = mad_text.read()
    content = re.split('(\W+)', text)

    for i in content:
        if i == 'NOUN':
            content.insert(content.index('NOUN'), input('Enter a ' +
                                                        i.lower() + ': '))
            content.remove('NOUN')
        elif i == 'VERB':
            content.insert(content.index('VERB'), input('Enter a ' +
                                                        i.lower() + ': '))
            content.remove('VERB')
        elif i == 'ADJECTIVE':
            content.insert(content.index('ADJECTIVE'), input('Enter an ' +
                                                             i.lower() + ': '))
            content.remove('ADJECTIVE')

    content = ''.join(content)
    print(content)
    mad_libs = open('mad_text2.txt', 'w')
    mad_libs.write(content)
    mad_libs.close()


if __name__ == "__main__":
    main()
