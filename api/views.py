from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BookSerializer
from .models import Book


class BooksCreateListView(APIView):
    """ This is a view to create a book record and list all books in the database. """

    def get(self, request, *args, **kwargs):
        books_qs = Book.objects.all()
        serializer = BookSerializer(books_qs, many=True)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetailVieworDeleteBookView(APIView):
    """ This is a view to get a record of a book, update a book record or delete a book record using its ID. """
    

    def get(self, request, bookID, *args, **kwargs):
        try:
            book = Book.objects.get(id=bookID)
        except Book.DoesNotExist:
            return Response({"error": "Book not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, bookID, *args, **kwargs):
        try:
            book = Book.objects.get(id=bookID)
        except Book.DoesNotExist:
            return Response({"error": "Book not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        

    def delete(self, request, bookID):
        try:
            book = Book.objects.get(id=bookID)
        except Book.DoesNotExist:
            return Response({"error": "Book not found!"}, status=status.HTTP_404_NOT_FOUND)
        
        book.delete()
        return Response({"You deleted this book!"}, status=status.HTTP_204_NO_CONTENT)
