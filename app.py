from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    courses = course()
    dollar = {'ccy': courses[0]['Ccy'], 'rate': courses[0]['Rate'], 'date': courses[0]['Date']}
    euro = {'ccy': courses[1]['Ccy'], 'rate': courses[1]['Rate'], 'date': courses[1]['Date']}
    ruble = {'ccy': courses[2]['Ccy'], 'rate': courses[2]['Rate'], 'date': courses[2]['Date']}
    return render_template('index.html', dollar=dollar, euro=euro, ruble=ruble)


def course() -> list:
    res = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
    res = res.json()
    dollar = res[0]
    euro = res[1]
    ruble = res[2]
    return [dollar, euro, ruble]


if __name__ == '__main__':
    app.run()
