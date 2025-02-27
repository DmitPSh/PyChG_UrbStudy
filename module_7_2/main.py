def custom_write(file_name, strings):
    strings_positions = {}


    file = open(file_name, 'w', encoding='utf-8')

    for line_number, string in enumerate(strings, start=1):
        byte_position = file.tell()
        file.write(string + '\n')
        strings_positions[(line_number, byte_position)] = string


    return strings_positions
    file.close()


info = [
'Text for tell.',
'Используйте кодировку utf-8.',
'Because there are 2 languages!',
'Спасибо!'
]

result = custom_write(    'text.txt', info)
for elem in result.items():
    print(elem)
