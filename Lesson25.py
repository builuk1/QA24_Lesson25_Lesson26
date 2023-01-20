import pytest


def hello(name):
    return f'Hello, my name is {name}'


def test_hello_positive():
    assert hello("Sten") == 'Hello, my name is Sten'


def test_hello_empty():
    assert hello("") == 'Hello, my name is '


def test_hello_John():
    assert hello('John') == 'Hello, my name is John'


def test_hello_name_surname():
    assert hello('Bob Smith') == 'Hello, my name is Bob Smith'


def test_hello_cyrillic():
    assert hello('Боб Смит') == 'Hello, my name is Боб Смит'


def years(age):
    return f"Your age is {age}"


def test_years_positive():
    assert years("20") == "Your age is 20"


def test_years_empty():
    assert years("") == "Your age is "


def place(city):
    return f"Your city is {city}"


def test_place_positive():
    assert place("Odesa") == "Your city is Odesa"


def test_place_empty():
    assert place("") == "Your city is "

def hello(name):
    return f'Hello, my name is {name}'


def test_hello_positive():
    assert hello('Stene') == 'Hello, my name is Stene'


def test_hello_empty():
    assert hello('') == 'Hello, my name is '


def test_hello_numbers():
    assert hello('12345') == 'Hello, my name is 12345'


def test_hello_symbols():
    assert hello('*%&@') == 'Hello, my name is *%&@'


def test_hello_upper():
    assert hello('BEN') == 'Hello, my name is BEN'

def test_hello_number():
    assert hello(123) == "Hello, my name is 123"

def test_hello_symbol():
    assert hello("$$$$$") == "Hello, my name is $$$$$"
