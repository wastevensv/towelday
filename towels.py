import markovify
import sqlite3

def addcount():
    con = sqlite3.connect("counter.db")
    c = con.cursor()
    try:
        c.execute("UPDATE counter SET int = int + 1")
    except sqlite3.Error as er:
        print(er)
    con.commit()
    con.close()

def generate(s=2, corpus="full"):
    with open('corpus/'+corpus+'.txt') as f:
        text = f.read()
    model = markovify.Text(text)
    gen = ''
    for i in range(s):
        sentence = model.make_sentence()
        if sentence != None:
            gen += sentence
    addcount()
    return gen

def generate_sentence(char=140, corpus="full"):
    with open('corpus/'+corpus+'.txt') as f:
        text = f.read()
    model = markovify.Text(text)
    addcount()
    sentence = model.make_short_sentence(char, tries=10)
    return sentence

if __name__ == '__main__':
    print(generate())
