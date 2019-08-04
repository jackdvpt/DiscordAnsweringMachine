from gtts import gTTS
from playsound import playsound
import os
import time
from time import gmtime, strftime
from googletrans import Translator
import random
import talk
from gtts.lang import tts_langs


lang = {'de': 'german', 'uk': 'ukrainian', 'si': 'sinhala', 'vi': 'vietnamese', 'sq': 'albanian', 'km': 'khmer', 'mk': 'macedonian', 'pl': 'polish', 'la': 'latin', 'nl': 'dutch', 'lv': 'latvian', 'is': 'icelandic', 'el': 'greek', 'bs': 'bosnian', 'eo': 'esperanto', 'ca': 'catalan', 'en': 'english', 'ro': 'romanian', 'cs': 'czech', 'pt': 'portuguese',
        'zh-cn': 'chinese (simplified)', 'ko': 'korean', 'su': 'sundanese', 'fr': 'french', 'sr': 'serbian', 'hi': 'hindi', 'da': 'danish', 'af': 'afrikaans', 'te': 'telugu', 'ta': 'tamil', 'cy': 'welsh', 'sk': 'slovak', 'no': 'norwegian', 'hu': 'hungarian', 'id': 'indonesian', 'tr': 'turkish', 'th': 'thai', 'sw': 'swahili', 'es': 'spanish', 'ja': 'japanese', 'my': 'myanmar (burmese)', 'tl': 'filipino', 'et': 'estonian', 'fi': 'finnish', 'zh-tw': 'chinese (traditional)', 'it': 'italian', 'ru': 'russian', 'ar': 'arabic', 'hy': 'armenian', 'sv': 'swedish', 'hr': 'croatian', 'mr': 'marathi', 'bn': 'bengali', 'ne': 'nepali', 'ml': 'malayalam', 'jw': 'javanese'}

def randomise(string, who):
    language = random.choice(list(lang))
    translator = Translator()
    print(lang[language])
    play(translator.translate(string, dest=language).text,who, language)


def roundtranslate(string, who):
    langs = set()
    print(len(lang))
    while len(langs) < 30:
        langs.add(random.choice(list(lang)))
    translator = Translator()
    words = string
    print("Starting String", words)
    for language in langs:
        words = translator.translate(string, dest=language).text
        print(lang[language], words)

    talk.play(translator.translate(words, dest="en").text, who)


def translate(string, who):
    translator = Translator()
    language = random.choice(list(lang))
    translated = translator.translate(string, dest=language).text
    talk.play(translated, who)


if __name__ == '__main__':
    roundtranslate("Whats up my homies", "Jack")
    # for i in range(0,10):
    #translate("hello bitches")
    #print("end string", roundtranslate("The quick brown fox jumps over the lazy dog"))
    # print(gtts.gTTS.LANGUAGES)
    #play("Hello Bitches", "Jack")
