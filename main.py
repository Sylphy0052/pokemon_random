from numpy.random import rand
import csv
import os
import sqlite3

DB_NAME = 'pokemon.sqlite'


def create_db():
    print('create_db')
    with open('pokemon.csv') as f:
        reader = csv.reader(f)
        pokemon_list = [row for row in reader]
    pokemon_list = [(l[0], l[1]) for l in pokemon_list]
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('create table pokemons(id integer, name text)')
    c.executemany('insert into pokemons values (?, ?)', pokemon_list)
    conn.commit()
    conn.close()


def get_rand(n):
    ret = []
    while len(ret) < 6:
        i = int(rand() * 400 + 1)
        if i not in ret:
            ret.append(i)
    ret.sort()
    return ret


def print_pokemon(n):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    query = 'select * from pokemons where id in({})'.format(
        ', '.join(':{}'.format(i) for i in range(len(n))))
    params = ({str(i): p for i, p in enumerate(n)})

    for row in c.execute(query, params):
        print('{}: {}'.format(row[0], row[1]))
    conn.commit()
    conn.close()


def main():
    numbers = get_rand(6)
    if not os.path.exists(DB_NAME):
        create_db()
    print_pokemon(numbers)


if __name__ == '__main__':
    main()
