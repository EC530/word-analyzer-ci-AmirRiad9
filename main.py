from collections import Counter
import matplotlib.pyplot as plt


def single_word_count(name):
    # initialize array to be used
    words = []

    # open file and access data
    with open(name, 'r') as f:
        for line in f:
            for word in line.split():
                # add words to array
                words.append(word)
    # create another variable for counter
    word_count = Counter(words)
    print(word_count)
    return word_count


def count(word_count):
    sum_of = sum(word_count.values())
    print(sum_of)
    return sum_of


def plot_hist(word_count):
    # plot into a histogram
    plt.bar(word_count.keys(), word_count.values())
    plt.show()


if __name__ == '__main__':
    count(single_word_count('text1.txt'))
    plot_hist(single_word_count('text1.txt'))
