import datetime
from flask import Blueprint,g, render_template, redirect, url_for, request
from flaskr.db import get_db#, close_db
from flaskr.getData import getData
main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():

    return "hello"

@main.route('/test')
def test():
    try:
        data = getData()
        print(data)
    
        lol = "Temperatur : {:.2f} und Feuchtigkeit: {:.2f}".format(data[0],data[1])
        #lol = f"Temperatur: {data[0]} und Feuchtigkeit: {data[1]}"
        return lol
    except:
        return "miese Briese"


@main.route('/test2')
def test2():
    try:
        db = get_db()
        getQuery = "SELECT Temperature, Humidity, Datum FROM BoxData;"

        result = list( db.execute(getQuery).fetchmany(5)  )
        TempListe = []
        HumidListe = []
        DateListe = []
        for x in result:
            
            a = x[0]# erste spalte
            b = x[1]# zweite spalte
            c = x[2]#dritte spalte
            
            print(a)
            print(b)
            print(c)

            TempListe += a
            Humidliste += b
            DateListe += c
        
        return [TempListe,HumidListe,DateListe]
    except Exception as error:
        error = str(error)
        return error
    finally:
        #g.db.close_db()
        pass
