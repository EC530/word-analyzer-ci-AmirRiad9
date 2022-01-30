import collections
import matplotlib.pyplot as plt


def main(name):
    #initialuze array to be used
    words = []
    #open file and access data
    with open(name, 'r') as f:
        for line in f:
            for word in line.split():
                #add words to array 
                words.append(word)
    #create another varaiable for counter           
    word_count = Counter(words)
    #plot into a histogram
    plt.bar(word_count.keys(), word_count.values())
    plt.show()

if __name__ == '__main__':
    main('text1.txt')


