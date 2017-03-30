import markovify
import codecs

def generate(s=2, corpus="full"):
    with codecs.open('corpus/'+corpus+'.txt', 'r', 'utf-8') as f:
        text = f.read()
    model = markovify.NewlineText(text)
    gen = ''
    for i in range(s):
        sentence = model.make_sentence()
        if sentence != None:
            gen += sentence + '\n'
    return gen

def generate_sentence(char=140, corpus="full"):
    with codecs.open('corpus/'+corpus+'.txt', 'r', 'utf-8') as f:
        text = f.read()
    model = markovify.NewlineText(text)
    sentence = model.make_short_sentence(char, tries=10)
    return sentence

if __name__ == '__main__':
    print(generate_sentence())
