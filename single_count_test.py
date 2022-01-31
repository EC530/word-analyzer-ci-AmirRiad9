from main import single_word_count

input_file= 'text1.txt'
output = ({'Test': 5, 'Hello': 1, 'This': 1, 'File': 1, 'Has': 1, 'How': 1, 'Many': 1, 'Words': 1})

def single_test():
    check = single_word_count(input_file)

    assert check == output
