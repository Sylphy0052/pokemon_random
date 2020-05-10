import csv
import sqlite3
from numpy.random import rand

DB_NAME = "resources/pokemon.sqlite"


def create_db():
    with open('resources/pokemon.csv') as f:
        reader = csv.reader(f)
        pokemon_list = [row for row in reader]
    pokemon_list = [(l[0], l[1], l[2], l[3], l[4], l[5]) for l in pokemon_list]
    pokemon_list = pokemon_list[1:]
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        'create table pokemons(id integer primary key, no integer, name text, type1 text, type2 text, version1 text, version2 text)')
    c.executemany(
        'insert into pokemons(no, name, type1, type2, version1, version2) values (?, ?, ?, ?, ?, ?)', pokemon_list)
    conn.commit()
    conn.close()


def get_one_data():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    no = int(rand() * 403 + 1)
    c.execute('select * from pokemons where id={}'.format(no))
    datas = c.fetchone()
    conn.commit()
    conn.close()
    return datas
