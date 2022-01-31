from main import count
from main import single_word_count

check = 8


def test_count():
    final = count(single_word_count('text1.txt'))

    assert final == check


