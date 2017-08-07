from collections import Counter

def bag_of_words(text):
    # TODO: Implement bag of words
    output = Counter()
    output.update(text.split(' '))
    return output

test_text = 'the quick brown fox jumps over the lazy dog'

print(bag_of_words(test_text))
