from flask_pymongo import PyMongo
import flask
import parse
from flask import *

# connecting mongoDB compass to flask
app = flask.Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/webAPIs"
mongodb_client = PyMongo(app)
db = mongodb_client.db


@app.route('/', methods=["GET", "POST"])
def query1():
    # appending those queries to the pipeline which are being filtered
    if request.method == "POST":
        pipeline = []
        year = request.form.get("year")
        protocol = request.form.get("pro")
        rg = request.form.get("rateg")
        rl = request.form.get("ratel")
        rate = request.form.get("rate")
        tag = request.form.get("tag")
        category = request.form.get('cat')
        if year != "":
            query = {'$match': {'updated': {'$regex': year}}}
            pipeline.append(query)
        if protocol != "":
            query = {'$match': {'protocols': protocol}}
            pipeline.append(query)
        if tag != "":
            tags = tag.split()
            query = {'$match': {'Tags': {'$in': tags}}}
            pipeline.append(query)
        if category != "":
            query = {'$match': {'category': category}}
            pipeline.append(query)
        # if rating equals to is provided
        if rate != "":
            query = {'$match': {'rating': {'$eq': float(rate)}}}
            pipeline.append(query)
        # if rating equals to is not provided but, greater than or less than are provided
        if rate == "":
            # if rating greater than and rating less than fields are provided
            if rg != "" and rl != "":
                query = {'$match': {'rating': {'$gt': float(rg), '$lt': float(rl)}}}
                pipeline.append(query)
            # if rating greater than field is provided
            elif rg != "" and rl == "":
                query = {'$match': {'rating': {'$gt': float(rg)}}}
                pipeline.append(query)
            # if rating less than field is provided
            elif rl != "" and rg == "":
                query = {'$match': {'rating': {'$lt': float(rl)}}}
                pipeline.append(query)
        query = {'$project': {'_id': 0}}
        pipeline.append(query)

        x = db.apiData.aggregate(pipeline)

        return render_template('home.html', x=x)

    return render_template("index.html")


@app.route('/ff', methods=["GET", "POST"])
def query2():
    # appending those queries to the pipeline which are being filtered
    if request.method == "POST":
        pipeline = []
        tag = request.form.get("tag")
        year = request.form.get("year")
        api = request.form.get("api")
        if year != "":
            query = {'$match': {'updated': {'$regex': year}}}
            pipeline.append(query)
        if tag != "":
            tags = tag.split()
            query = {'$match': {'tags': {'$in': tags}}}
            pipeline.append(query)
        if api != "":
            apis = api.split()
            query = {'$match': {'APIs': {'$in': apis}}}
            pipeline.append(query)

        query = {'$project': {'_id': 0}}
        pipeline.append(query)
        x = db.mashupData.aggregate(pipeline)

        return render_template('home.html', x=x)

    return render_template("index.html")


@app.route('/pg', methods=["GET", "POST"])
def query3():
    # appending those queries to the pipeline which are being filtered
    if request.method == "POST":
        pipeline = []
        keyword = request.form.get("key")
        if keyword != "":
            keywords = keyword.split()
            # each keyword is being checked if it is present in at least one of the fields
            for new_word in keywords:
                query = {'$match': {'$or': [{'description': {'$regex': new_word, '$options': 'i'}},
                                            {'title': {'$regex': new_word, '$options': 'i'}},
                                            {'summary': {'$regex': new_word, '$options': 'i'}}]}}
                pipeline.append(query)
            query = {'$project': {'_id': 0}}
            pipeline.append(query)
            x = db.apiData.aggregate(pipeline)

        return render_template('home.html', x=x)

    return render_template("index.html")


@app.route('/hg', methods=["GET", "POST"])
def query4():
    # appending those queries to the pipeline which are being filtered
    if request.method == "POST":
        pipeline = []
        keyword = request.form.get("key")
        if keyword != "":
            keywords = keyword.split()
            # each keyword is being checked if it is present in at least one of the fields
            for new_word in keywords:
                query = {'$match': {'$or': [{'description': {'$regex': new_word, '$options': 'i'}},
                                            {'title': {'$regex': new_word, '$options': 'i'}},
                                            {'summary': {'$regex': new_word, '$options': 'i'}}]}}
                pipeline.append(query)
            query = {'$project': {'_id': 0}}
            pipeline.append(query)
            x = db.mashupData.aggregate(pipeline)

        return render_template('home.html', x=x)

    return render_template("index.html")


if __name__ == '__main__':
    # parsing the data into the database created by calling parse.py
    api_data, mashup_data = parse.main()
    # dropping the collection to avoid redundancy
    db.apiData.drop()
    db.mashupData.drop()
    # loading the data into the database
    db.apiData.insert_many(api_data)
    db.mashupData.insert_many(mashup_data)
    # running the application
    app.run()
