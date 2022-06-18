def file_format():
    first, second, third = open('1.txt', encoding='utf=8'), open('2.txt', encoding='utf-8'), open('3.txt', encoding='utf-8')
    count_first = 0
    count_second = 0
    count_third = 0
    reader1 = first.read()
    reader2 = second.read()
    reader3 = third.read()

    for row in reader1.split('\n'):
        count_first += 1
    for row in reader2.split('\n'):
        count_second += 1
    for row in reader3.split('\n'):
        count_third += 1
    text_first = f'1.txt\nДлина файла - {count_first}\n{reader1}\n'
    text_second = f'2.txt\nДлина файла - {count_second}\n{reader2}\n'
    text_third = f'2.txt\nДлина файла - {count_third}\n{reader3}\n'

    with open('4.txt', 'w', encoding='utf-8') as end_file:
        if (count_first > count_second < count_third):
            if count_first < count_third:
                main_text = f'{text_second}\n{text_first}\n{text_third}'
                end_file.write(main_text)
            else:
                main_text = f'{text_second}\n{text_third}\n{text_first}'
                end_file.write(main_text)
        elif (count_second > count_first < count_third):
            if count_second < count_third:
                main_text = f'{text_first}\n{text_second}\n{text_third}'
                end_file.write(main_text)
            else:
                main_text = f'{text_first}\n{text_third}\n{text_first}'
                end_file.write(main_text)
        elif (count_first > count_third < count_second):
            if count_first < count_second:
                main_text = f'{text_third}\n{text_first}\n{text_second}'
                end_file.write(main_text)
            else:
                main_text = f'{text_third}\n{text_second}\n{text_first}'
                end_file.write(main_text)




file_format()

