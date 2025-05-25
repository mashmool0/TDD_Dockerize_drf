import pytest
from movies.models import Movie


@pytest.fixture
def add_movie():
    def _add_movie(title, genre, year):
        return Movie.objects.create(title=title, genre=genre, year=year)
    return _add_movie
