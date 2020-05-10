from flask import Flask, render_template, request
from numpy.random import rand
import os
from src.db_controller import DB_NAME, create_db, get_one_data
from src.pokemon_selector import Pokemon, get_pokemon

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('poke.html', title='Pokemon Selector', pokemons=[])


@app.route('/', methods=['POST'])
def select_pokemon():
    if not os.path.exists(DB_NAME):
        create_db()

    options = []
    number = 6
    if 'type' in request.form.keys():
        options.append('type')
    if 'version1' in request.form.keys():
        options.append('sword')
    if 'version2' in request.form.keys():
        if 'sword' in options:
            options.remove('sword')
        else:
            options.append('shield')
    if 'first' in request.form.keys():
        options.append('first')
    if 'legend' in request.form.keys():
        options.append('legend')
    if 'gallant' in request.form.keys():
        options.append('gallant')
    if 'number' in request.form.keys():
        try:
            number = int(request.form['number'])
            if number < 1 or number > 10:
                number = 6
        except Exception:
            number = 6

    print(number)
    pokemons = get_pokemon(number, options)
    return render_template('poke.html', title='Pokemon Selector', pokemons=pokemons)


if __name__ == '__main__':
    app.run(debug=True, port=8888, threaded=True)
