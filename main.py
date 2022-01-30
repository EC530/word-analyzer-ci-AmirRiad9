# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections



def main(name):
    words = []
    with open(name, 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word)
    word_count = Counter(words)
    plt.bar(word_count.keys(), word_count.values())
    plt.show()

if __name__ == '__main__':
    main('text1.txt')


