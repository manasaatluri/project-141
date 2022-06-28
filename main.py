from flask import Flask,jsonify,request
import csv 

all_articles = []

with open("articles.csv",encoding="utf8") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_articles = data[1:]


liked_article = []
unliked_article = []


app = Flask(__name__)

@app.route("/get-article")
def get_movies():
    return jsonify({
        "data":all_articles[0],
        "status": "success"
        })

@app.route("/unliked-article",methods = ["POST"])
def unliked_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    unliked_article.append(movie)
    return jsonify({
        "status":"success"
    }),201

@app.route("/liked-article",methods=["POST"])
def like_movie():
    movie = all_articles[0]
    all_articles = all_articles[1:]
    liked_article.append(movie)
    return jsonify({
        "status":"success"
    }),201


if __name__ == "__main__" :
    app.run()