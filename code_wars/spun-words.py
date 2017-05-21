def spin_words(sentence):
    def spin(word):
        if len(word) >= 5:
            return reduce(lambda x,y: x + y, reversed(word), "")
        else:
            return word
    return ' '.join(map(spin, sentence.split()))

    