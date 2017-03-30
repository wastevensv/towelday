from flask import Flask, request, send_from_directory
import towels
app = Flask(__name__)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>/')
def index(path):
    return send_from_directory('pages', path)

@app.route('/gen/', defaults={'num': 3, 'corpus': 'full'})
@app.route('/gen/<int:num>/', defaults={'corpus': 'full'})
@app.route('/gen/<int:num>/<string:corpus>/')
def generate(num, corpus):
    if num > 42:
        return 'Sentence limit exceeded.'
    return towels.generate(num, corpus)

@app.route('/gen/s/', defaults={'char': 140, 'corpus': 'full'})
@app.route('/gen/s/<int:char>/', defaults={'corpus': 'full'})
@app.route('/gen/s/<int:char>/<string:corpus>/')
def generate_sentence(char, corpus):
    if char > 420:
        return 'Character limit exceeded.'
    sentence = towels.generate_sentence(char, corpus)
    if sentence is None:
        return ''
    return sentence

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=22109)

