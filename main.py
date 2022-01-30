# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def main(name):
    words = []

    with open(name, 'r') as f:
        for line in f:
            for word in line.split():
                words.append(word)


    print(words)
    print(len(words))

    word_count = collections.Counter(words)
    print(word_count)

if __name__ == '__main__':
    main('text1.txt')


