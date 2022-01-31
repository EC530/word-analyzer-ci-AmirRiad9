from main import count
from main import single_word_count

input = ({'Test': 5, 'Hello': 1, 'This': 1, 'File': 1, 'Has': 1, 'How': 1, 'Many': 1, 'Words': 1})
check = sum(input.values())


def test_count():
    final = count(single_word_count('text1.txt'))

    assert final == check
