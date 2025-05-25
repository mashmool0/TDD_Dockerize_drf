from django.http import Http404
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse
from rest_framework.views import APIView
from movies.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from movies.models import Movie
# Create your views here.


def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)


class MovieList(APIView):
    def post(self, request, format=None):
        ser = MovieSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data, status=status.HTTP_201_CREATED)
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, format=None):
    #     movies = Movie.objects.all()
    #     ser = MovieSerializer(data=movies, many=True)
    #     if ser.is_valid():
    #         return Response(ser.data, status.HTTP_200_OK)
    #     return Response(ser.errors, status.HTTP_400_BAD_REQUEST)


class MovieDetail(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(id=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk=pk)
        ser = MovieSerializer(item)
        return Response(ser.data)
