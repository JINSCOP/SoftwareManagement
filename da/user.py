# 目前可能没有python3的mysql-python包，所以这个代码可能没有用
from flask import Flask, jsonify

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey


app = Flask(__name__)


@app.route('/')
def hello_world():
    engine = create_engine(
        "mysql://root:****@localhost:3306/test?charset=utf8", encoding="utf-8", echo=True)
    metadata = MetaData()
    user = Table('user', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String(20)),
                 Column('fullname', String(40)),
                 )

    address = Table('address', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('user_id', None, ForeignKey('user.id')),
                    Column('email', String(60), nullable=False)
                    )
    metadata.create_all(engine)
    conn = engine.connect()

    conn.execute("SELECT * FROM user")
    i = user.insert()
    u = dict(name='jack', fullname='jack Jone')
    r = conn.execute(i, **u)

    return jsonify({'task': str(r.rowcount)})  # str(r.rowcount)


if __name__ == '__main__':
    app.run()
