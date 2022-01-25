import psycopg2 as ps
from data_base.config import host, user, password, db_name


def pga_start():
    global base, cur
    base = ps.connect(user=user,
                      password=password,
                      host=host)
    cur = base.cursor()
    if base:
        print('Database connected OK!')
    cur.execute('CREATE TABLE IF NOT EXISTS cars(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT);')
    base.commit()


async def data_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO cars VALUES({0},{1},{2},{3})').format(data[0], data[1], data[2], data[3])
        base.commit()