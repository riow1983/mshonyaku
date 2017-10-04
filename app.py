from flask import Flask, render_template, request
#from mstranslator import Translator
#translator = Translator("319660f0d6164c5fb8f91e2cb54101f5")
from mshonyaku import translate, add_translate
import sqlite3 as sql

app = Flask(__name__)


"""
# translate
textToTranslate = "Will you check the name please?"
fromLangCode = "en"
toLangCode = "ja"

translate(textToTranslate=textToTranslate, fromLangCode=fromLangCode, toLangCode=toLangCode)
"""

"""
# add_translate
originalText = textToTranslate
translatedText = "You dropped your wallet."
fromLangCode = "ja"
toLangCode = "en"

add_translate(originalText=originalText, translatedText=translatedText, 
              fromLangCode=fromLangCode, toLangCode=toLangCode)
"""


@app.route('/')
def translator_home():
    return render_template("translator.html")


@app.route('/forward/', methods = ['POST'])
def addrec():
    conn = sql.connect("database.db")
    cur = conn.cursor()
    if request.form['tl']=="英語に翻訳する":
        original = request.form['inputform']
        translated = translate(textToTranslate=original, fromLangCode='ja', toLangCode='en')
        japanese = original
        english = translated
        cur.execute("INSERT INTO db (日本語,English) VALUES (?,?)", (japanese,english))
        conn.commit()
        conn.close()
        return render_template("translator.html", original=original, translated=translated)
    elif request.form['tl']=="Translate to Japanese":
        original = request.form['inputform']
        translated = translate(textToTranslate=original, fromLangCode='en', toLangCode='ja')
        english = original
        japanese = translated
        cur.execute("INSERT INTO db (日本語,English) VALUES (?,?)", (japanese,english))
        conn.commit()
        conn.close()
        return render_template("translator.html", original=original, translated=translated)
    else:
        pass

@app.route('/db')
def db():
    conn = sql.connect("database.db")
    conn.row_factory = sql.Row

    cur = conn.cursor()
    cur.execute("SELECT * FROM db")

    rows = cur.fetchall();    
    return render_template("db.html", rows=rows)
    conn.close()


if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0')
