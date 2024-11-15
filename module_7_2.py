def custom_write(file_name: str, strings):
    tuple_ = {}
    number = 0
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        a = file.seek(file.tell())
        file.write(str(i + '\n'))
        number += 1
        b = (number, a)
        tuple_[b] = str(i)
    file.close()
    return tuple_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
