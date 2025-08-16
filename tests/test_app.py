import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_movie_list(client):
    """영화 목록 페이지가 정상적으로 로드되는지 테스트"""
    response = client.get('/movies/')
    assert response.status_code == 200
    assert '인셉션'.encode('utf-8') in response.data

def test_movie_detail(client):
    """영화 상세 페이지가 정상적으로 로드되는지 테스트"""
    response = client.get('/movie/1')
    assert response.status_code == 200
    assert '인셉션'.encode('utf-8') in response.data
    assert '코브는 생각을 훔치는'.encode('utf-8') in response.data

def test_movie_not_found(client):
    """존재하지 않는 영화 페이지에 접근 시 404 오류를 테스트"""
    response = client.get('/movie/999')
    assert response.status_code == 404