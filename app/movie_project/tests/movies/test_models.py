import pytest
from movies.models import Movie


@pytest.mark.django_db
def test_movie_model():
    movie = Movie(title='Test Movie', genre="Comedy", year='2003')
    movie.save()

    assert movie.title == "Test Movie"
    assert movie.genre == "Comedy"
    assert movie.year == "2003"
    assert movie.created_date
    assert movie.updated_date
    assert str(movie) == movie.title
