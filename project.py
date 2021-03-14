from flask import Flask
from flask import render_template
app = Flask(__name__)

#  Database part
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import psycopg2

#  conecting database 
engine = db.create_engine('postgresql+psycopg2://postgres:pwd123@127.0.0.1:5432/dbms_project')
connection = engine.connect()
metadata = db.MetaData()
fake = db.Table('fake', metadata, autoload=True, autoload_with=engine)
# creating session
Session = sessionmaker(bind = engine)
session = Session()



# main funtion
@app.route('/')
def hello_world():
    # entry1 = fake.insert().values(id=310, name = "john")
    # session.execute(entry1)
    session.commit()
    result = session.query(fake).first()
    print(result) 
    return render_template("index.html", result=result)



if __name__ == "__main__":
    app.run()
