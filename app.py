from flask import Flask, render_template, redirect, url_for, abort
from pymongo import MongoClient
from bson.objectid import ObjectId # To handle MongoDB's _id

app = Flask(__name__)

# MongoDB 설정
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client.movie_community_db # 데이터베이스 이름
movies_collection = db.movies # 컬렉션 이름



@app.route('/')
def index():
    return redirect(url_for('movie_list'))

@app.route('/movies/')
def movie_list():
    # MongoDB에서 모든 영화 가져오기
    movies = []
    for movie in movies_collection.find():
        movie['id'] = str(movie['_id']) # ObjectId를 문자열로 변환
        movies.append(movie)
    return render_template('movies.html', movies=movies)

# 영화 상세 페이지를 위한 동적 라우트
@app.route('/movie/<movie_id>') # movie_id는 ObjectId 문자열이므로 int가 아님
def movie_detail(movie_id):
    # MongoDB에서 특정 영화 가져오기
    try:
        movie = movies_collection.find_one({'_id': ObjectId(movie_id)})
    except:
        abort(404)

    if movie is None:
        abort(404) # 영화가 없으면 404 Not Found 오류 발생

    movie['id'] = str(movie['_id']) # ObjectId를 문자열로 변환
    return render_template('movie_detail.html', movie=movie)

if __name__ == '__main__':
    app.run(debug=True)
