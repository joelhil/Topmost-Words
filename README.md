# Topmost-Words
Finds the top x most used words in a txt or from a gutenberg https. Made for assignment in Summer python course on Gothenburg University 2020.

How to run
python3 topmost.py <arg1> <arg2> <arg3>\
arg1 is list of stopwords, arg2 is file or website with text in txt utf8-format and arg3 is how many of the topwords to print\
(eng_stopwords.txt is included)

Example of how to run program:\
$ python3 topmost.py eng_stopwords.txt bravenewworld.txt 15\
Line above will print out the 15 most used words in brave new world that is not included in the file eng_stopwords.
  
Alternatively:\
$ python3 topmost.py eng_stopwords.txt https://www.gutenberg.org/cache/epub/69823/pg69823.txt 15\
for an example of a website.
