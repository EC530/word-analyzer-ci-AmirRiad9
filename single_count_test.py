from main import single_word_count
from main import filename

if filename == 'text1.txt':
    output = ({'Test': 5, 'Hello': 1, 'This': 1, 'File': 1, 'Has': 1, 'How': 1, 'Many': 1, 'Words': 1})
elif filename == 'text2.txt':
    output = (
        {'cross': 3, 'farm': 3, 'hard': 3, 'start': 3, 'might': 3, 'story': 3, 'saw': 3, 'far': 3, 'sea': 3, 'draw': 3,
         'left': 3, 'late': 3, 'run': 3, "don't": 3, 'while': 3, 'press': 3, 'close': 3, 'night': 3, 'real': 3,
         'life': 3,
         'few': 3, 'north': 3, 'open': 3, 'seem': 3, 'together': 3, 'next': 3, 'white': 3, 'children': 3, 'begin': 3,
         'got': 3, 'walk': 3, 'example': 3, 'ease': 3, 'paper': 3, 'group': 3, 'always': 3, 'music': 3, 'those': 3,
         'both': 3, 'mark': 3, 'often': 3, 'letter': 3, 'until': 3, 'mile': 3, 'river': 3, 'car': 3, 'feet': 3,
         'care': 3,
         'second': 3, 'book': 3, 'carry': 3, 'took': 3, 'science': 3, 'eat': 3, 'room': 3, 'friend': 3, 'began': 3,
         'idea': 3, 'fish': 3, 'mountain': 3, 'stop': 3, 'once': 3, 'base': 3, 'hear': 3, 'horse': 3, 'cut': 3,
         'sure': 3,
         'watch': 3, 'color': 3, 'face': 3, 'wood': 3, 'main': 3, 'enough': 3, 'plain': 3, 'girl': 3, 'usual': 3,
         'young': 3, 'ready': 3, 'above': 3, 'ever': 3, 'red': 3, 'list': 3, 'though': 3, 'feel': 3, 'talk': 3,
         'bird': 3,
         'soon': 3, 'body': 3, 'dog': 3, 'family': 3, 'direct': 3, 'pose': 3, 'leave': 3, 'of': 1, 'to': 1, 'and': 1,
         'a': 1, 'in': 1, 'is': 1, 'it': 1, 'you': 1, 'that': 1, 'he': 1, 'was': 1, 'for': 1, 'on': 1, 'are': 1,
         'with': 1,
         'as': 1, 'I': 1, 'his': 1, 'they': 1, 'be': 1, 'at': 1, 'one': 1, 'have': 1, 'this': 1, 'from': 1, 'or': 1,
         'had': 1, 'by': 1, 'not': 1, 'word': 1, 'but': 1, 'what': 1, 'some': 1, 'we': 1, 'can': 1, 'out': 1,
         'other': 1,
         'were': 1, 'all': 1, 'there': 1, 'when': 1, 'up': 1, 'use': 1, 'your': 1, 'how': 1, 'said': 1, 'an': 1,
         'each': 1,
         'she': 1, 'which': 1, 'do': 1, 'their': 1, 'time': 1, 'if': 1, 'will': 1, 'way': 1, 'about': 1, 'many': 1,
         'then': 1, 'them': 1, 'write': 1, 'would': 1, 'like': 1, 'so': 1, 'these': 1, 'her': 1, 'long': 1, 'make': 1,
         'thing': 1, 'see': 1, 'him': 1, 'two': 1, 'has': 1, 'look': 1, 'more': 1, 'day': 1, 'could': 1, 'go': 1,
         'come': 1,
         'did': 1, 'number': 1, 'sound': 1, 'no': 1, 'most': 1, 'people': 1, 'my': 1, 'over': 1, 'know': 1, 'water': 1,
         'than': 1, 'call': 1, 'first': 1, 'who': 1, 'may': 1, 'down': 1, 'side': 1, 'been': 1, 'now': 1, 'find': 1,
         'any': 1, 'new': 1, 'work': 1, 'part': 1, 'take': 1, 'get': 1, 'place': 1, 'made': 1, 'live': 1, 'where': 1,
         'after': 1, 'back': 1, 'little': 1, 'only': 1, 'round': 1, 'man': 1, 'year': 1, 'came': 1, 'show': 1,
         'every': 1,
         'good': 1, 'me': 1, 'give': 1, 'our': 1, 'under': 1, 'name': 1, 'very': 1, 'through': 1, 'just': 1, 'form': 1,
         'sentence': 1, 'great': 1, 'think': 1, 'say': 1, 'help': 1, 'low': 1, 'line': 1, 'differ': 1, 'turn': 1,
         'cause': 1, 'much': 1, 'mean': 1, 'before': 1, 'move': 1, 'right': 1, 'boy': 1, 'old': 1, 'too': 1, 'same': 1,
         'tell': 1, 'does': 1, 'set': 1, 'three': 1, 'want': 1, 'air': 1, 'well': 1, 'also': 1, 'play': 1, 'small': 1,
         'end': 1, 'put': 1, 'home': 1, 'read': 1, 'hand': 1, 'port': 1, 'large': 1, 'spell': 1, 'add': 1, 'even': 1,
         'land': 1, 'here': 1, 'must': 1, 'big': 1, 'high': 1, 'such': 1, 'follow': 1, 'act': 1, 'why': 1, 'ask': 1,
         'men': 1, 'change': 1, 'went': 1, 'light': 1, 'kind': 1, 'off': 1, 'need': 1, 'house': 1, 'picture': 1,
         'try': 1,
         'us': 1, 'again': 1, 'animal': 1, 'point': 1, 'mother': 1, 'world': 1, 'near': 1, 'build': 1, 'self': 1,
         'earth': 1, 'father': 1, 'head': 1, 'stand': 1, 'own': 1, 'page': 1, 'should': 1, 'country': 1, 'found': 1,
         'answer': 1, 'school': 1, 'grow': 1, 'study': 1, 'still': 1, 'learn': 1, 'plant': 1, 'cover': 1, 'food': 1,
         'sun': 1, 'four': 1, 'between': 1, 'state': 1, 'keep': 1, 'eye': 1, 'never': 1, 'last': 1, 'let': 1,
         'thought': 1,
         'city': 1, 'tree': 1})


def single_test():
    check = single_word_count(filename)

    assert check == output
