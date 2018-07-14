#!/usr/bin/python3
from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    html = """
    <h1>think number between 1 - 1000 and I will guess it in 10 moves !!!</h1>
    <a href="/game"><h2>Play a Game</h2></a>
    """
    return html


@app.route("/game", methods=['GET', 'POST'])
def game():
    if request.method == 'GET':
        return get_form(**guess_number(start=True))
    elif request.method == 'POST':
        min = int(request.form.get('min'))
        max = int(request.form.get('max'))
        user_input = request.form.get('button')
        return get_form(**guess_number(min=min, max=max, user_input=user_input))


def get_form(guess=500, min=0, max=1001, found=False):
    if found:
        form = f"""<h2> I GOT IT</h2>
        <h3> it's {guess} </h3>
        <a href="/"><p>back to main page </p></a>
        """
    else:
        form  = f"""
            <h2>think number between 1 - 1000 and I will guess it in 10 moves !!!</h2>
            <h3> My guess is {guess}</h3>
            <form action="/game" method="POST">
                  <input type="hidden" name="min" value={min}>
                  <input type="hidden" name="max" value={max}>
              <input type="submit" name="button" value="TO MUCH">
              <input type="submit" name="button" value="NOT ENOUGH">
              <input type="submit" name="button" value="GOT IT">
            </form>
            """
    return form


def guess_number(min=0, max=1001, user_input=None, found=None, start=False):
    guess = int((max - min) / 2) + min
    if user_input == "GOT IT":
        found = True
    elif user_input == "TO MUCH":
        max = guess
    elif user_input == "NOT ENOUGH":
        min = guess
    if not start:
        guess = int((max - min) / 2) + min
    return {"guess": guess, "min": min, "max": max, "found": found}


if __name__ == '__main__':
    app.run(debug=True)
