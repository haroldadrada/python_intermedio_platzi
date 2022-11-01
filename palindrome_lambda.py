"""
Dos formas de programar un Palindromo
"""

from email.policy import strict


def run():
    # Primera forma: Con funciones
    def palindrome(string):
        return string == string[::-1]
    
    print(palindrome("ana"))

    # Segunda forma: con lambda (Función anónima)
    palindrome_lambda = lambda string: string == string[::-1]

    print(palindrome_lambda("ana"))


if __name__ == '__main__':
    run()