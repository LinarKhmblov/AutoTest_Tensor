# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код


input_file = "test_file/task1_data.txt"
output_file = "test_file/task1_answer.txt"

with open(input_file, 'r', encoding='utf-8') as file:
    text = file.read()

text_without_digits = (''.join(i for i in text if not i.isdigit()))

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(text_without_digits)

print("Текст без цифр успешно записан в файл task1_answer.txt.")

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')