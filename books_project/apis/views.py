from django.shortcuts import render
from rest_framework import generics
from books.models import Book
from apis.serializer import BookSerializer
# Create your views here.

class ApiListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer