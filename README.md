# TowelDay
A system for generating sentences similar to those from the hitchhikers series of books. Based on the emojipasta.club service.

# How it works
TowelDay uses [Markovify](https://github.com/jsvine/markovify) to generate a text model from a corpus of text from the Hitchhikers novels by Douglas Adams.

# How to get The Guide
A version of the text with punctuation removed, and one sentence per line is available in the corpus subdirectory of this repository. It was obtained by copying [this text](http://www.induceddyslexia.com/douglasadams.htm) into a plain text file,
followed by [this file](http://www.textfiles.com/stories/hitch2.txt) and [this file](http://www.textfiles.com/stories/hitch3.txt).

Sadly, I have only found the first three books in the trilogy. If anyone knows where to find plaintext version of the others, I'll add them to the corpus, and link to them above.

# API
TowelDay exposes two RESTful API endpoints, at `http://towel.wasv.me/gen/` and `http://towel.wasv.me/gen/s/` respectively.

#### /gen/
`/gen/<int:num>/<string:corpus>/` produces a block of text of the specified sentence length. If no length is provided, the default length of 2 is used.

#### /gen/s/
`/gen/s/<int:char>/<string:corpus>/` produces a sentence of the specified maximum character length. If no length is provided, the default length of 140 is used.
