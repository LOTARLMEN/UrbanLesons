from types import NoneType

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    if string != str:
        string = str(string)
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = str(list_to_search).lower()
    is_or_no = NoneType
    if list_to_search.find(string) == -1:
        is_or_no = False
    else:
        is_or_no = True
    return is_or_no

print(string_info('Улумулу'))
print(string_info('Генокрад'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)