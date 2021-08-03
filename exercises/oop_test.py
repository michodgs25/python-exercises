import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
      "make a class named %%% that is-a %%%. ",

    "class %%%(object):\n\tdef *** __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** params."

    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function *** that takes self and @@@ params.",

    "*** = %%%():"
      "set *** to an instance of class %%%. ",

    "***.***(@@@)":
      "from *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
      "from *** get the *** attribute and set it to '***'."
}
