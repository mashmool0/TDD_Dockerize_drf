import json
import pytest
from movies.models import Movie


@pytest.mark.django_db
def test_add_movie(client):
    # given
    movies = Movie.objects.all()
    assert len(movies) == 0

    # When
    resp = client.post(
        "/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        },
        content_type="application/json"
    )

    # Then

    assert resp.status_code == 201
    assert resp.data['title'] == "The Big Lebowski"
    movies = Movie.objects.all()
    assert len(movies) == 1


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/movies/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_movie_invalid_json_keys(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
        },
        content_type="application/json"
    )
    assert resp.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_get_single_movie(client):
    movies = Movie.objects.create(
        title="test", genre='test genre', year='1999')

    resp = client.get(f'/api/movies/{movies.id}/')
    assert resp.status_code == 200
    assert resp.data['title'] == 'test'


@pytest.mark.django_db
def test_get_single_movie_incorrect_id(client):
    resp = client.get("api/movies/foo/")
    assert resp.status_code == 404
