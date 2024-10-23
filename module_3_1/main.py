
calls = 0
str = ()
def count_calls():
    global calls
    calls += 1
def string_info(string):
    tuple_1 = (len(string), string.upper(), string.lower())
    count_calls()
    print(tuple_1)
def is_contains(string_1, str):
    string_1 = string_1.lower()
    for i in range(len(str)):
        str[i] = str[i].lower()

    if string_1 in str:
        print('True')
        count_calls()
    else:
        print('False')
        count_calls()

string_info('ForTune')
string_info('MEdiTation')
string_info('heSItaTIon')
string_info('LuXury')

is_contains('CYCLe', ['recycling', 'cycling', 'cyclic'])
is_contains('uRbAn', ['ban', 'BaNaN', 'urBAN'])
print(calls)

