calls = 0


def count_calls(calls):
    return (calls)


def string_info(string):
    global calls
    calls += 1
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    global calls
    calls += 1
    for i in range(len(list_to_search)):
        if list_to_search[i].upper() == string.upper():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
