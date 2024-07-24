calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (int(len(string)), string.upper(), string.lower())
def is_conteins(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower():
            return(True)
    return(False)
print(string_info('Other'))
print(string_info('Armageddon'))
print(string_info('Want'))
print(is_conteins('one', ['foR', 'haVe', 'somE']))
print(is_conteins('Other', ['out', 'tell', 'oTHer', 'Want']))
print(is_conteins('will', ['such', 'aCt', 'format']))
print(calls)








