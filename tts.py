#Description: This program takes text from an online article and converts it to speech

#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the article

article = Article('https://hackernoon.com/future-of-python-language-bright-or-dull-uv41u3xwx')

article.download()
article.parse()
#DOWNLOAD ONCE ONLY
#nltk.download('punkt')
article.nlp()

#Get the articles text
mytext = article.text

language = 'ar' #English

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save("read_article1.mp3")

# Playing the converted file
os.system("start read_article1.mp3")
print("Done")