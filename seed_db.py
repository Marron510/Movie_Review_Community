import os
from pymongo import MongoClient

# MongoDB 설정
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client.movie_community_db # 데이터베이스 이름
movies_collection = db.movies # 컬렉션 이름

# 초기 영화 데이터 (app.py에서 가져온 데이터)
dummy_movies = [
    {
        'id': 1,
        'title': '인셉션',
        'year': 2010,
        'description': '코브는 생각을 훔치는 특수 범죄자이다. 그는 머릿속의 정보를 훔치는 것이 아니라, 반대로 생각을 심는 \'인셉션\' 작전을 계획한다.'
    },
    {
        'id': 2,
        'title': '인터스텔라',
        'year': 2014,
        'description': '세계 각국의 정부와 경제가 완전히 붕괴된 미래가 다가온다. 인류는 더 이상 희망이 없다고 생각하며, 마지막 희망을 걸고 우주로 떠난다.'
    },
    {
        'id': 3,
        'title': '다크 나이트',
        'year': 2008,
        'description': '배트맨은 고담시의 범죄를 소탕하기 위해 새로운 동맹, 제임스 고든과 하비 덴트와 함께한다. 하지만 그들 앞에 조커라는 최악의 악당이 나타난다.'
    },
    {
        'id': 4,
        'title': '매트릭스',
        'year': 1999,
        'description': '인간의 기억마저 AI에 의해 입력되고 삭제되는 세상, 진짜보다 더 진짜 같은 가상현실 ‘매트릭스’. 그 속에서 진정한 현실을 찾아 나서는 인간들의 이야기.'
    }
]

def seed_data():
    print("기존 'movies' 컬렉션 삭제 중...")
    movies_collection.drop() # 기존 컬렉션 삭제 (클린 시드를 위해)
    print("'movies' 컬렉션 삭제 완료.")

    print("새로운 영화 데이터 삽입 중...")
    movies_collection.insert_many(dummy_movies)
    print(f"{len(dummy_movies)}개의 영화 데이터 삽입 완료.")
    print("데이터베이스 시딩 완료!")

if __name__ == '__main__':
    seed_data()
