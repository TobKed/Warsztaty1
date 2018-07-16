#!/usr/bin/python3
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    html = """<h1>think number between 1 - 1000 and I will guess it in 10 moves !!!</h1>
    <a href="/game"><h2>Play a Game</h2></a>"""
    return html


@app.route("/game", methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return get_form(guess=guess_number())
    elif request.method == 'POST':
        min = int(request.form.get('min'))
        max = int(request.form.get('max'))
        counter = int(request.form.get('counter'))
        user_input = request.form.get('button')
        if user_input == "GOT IT":
            return get_form(guess_number(min, max), counter=counter, got_it=True)
        elif user_input == "TO MUCH":
            max = guess_number(min, max)
        elif user_input == "NOT ENOUGH":
            min = guess_number(min, max)
        return get_form(guess_number(min, max), min, max, counter+1)


def get_form(guess, min=0, max=1001, counter=0, got_it=False):
    if not got_it:
        return f"""<h2>think number between 1 - 1000 and I will guess it in 10 moves !!!</h2>
                <h3> My guess is {guess}</h3>
                <form action="/game" method="POST">
                      <input name="min" value={min} type="hidden">
                      <input name="max" value={max} type="hidden">
                      <input name="counter" value={counter} type="hidden">
                  <input type="submit" name="button" value="TO MUCH">
                  <input type="submit" name="button" value="NOT ENOUGH">
                  <input type="submit" name="button" value="GOT IT">
                </form>"""  #
    return f"""<h2> I GOT IT</h2>
            <h3> it's {guess} </h3>
            <h4> it took me {counter} moves </h4>
            <a href="/"><p>back to main page </p></a>"""


def guess_number(min=0, max=1001):
    return int((max - min) / 2) + min


if __name__ == '__main__':
    app.run(debug=True)
