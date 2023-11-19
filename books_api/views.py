from django.shortcuts import render;
from books_api.models import Book;
from rest_framework.response import Response;
from rest_framework.decorators import api_view;
from rest_framework import status
from books_api.serializer import BookSerializer;

###################################
# GET BOOKS
###################################
@api_view(['GET'])
def getAllBooks(request):
    try: 
        # Get all books but this is complex data
        books = Book.objects.all();
        # Convert this to python data structures with serializers
        serializer = BookSerializer(books, many=True);
        # send response
        return Response({
            'statusCode': 200,
            'message': 'Get all books query was successful',
            'books': serializer.data
        }, status=status.HTTP_200_OK);
    except:
        return Response({
            'statusCode': 500,
            'message': 'Get all books query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR);



###################################
# CREATE BOOK
###################################
@api_view(['POST'])
def createBook(request):
    try:
        # Get request body data but complex data
        data = request.data;
        # Create data structure according to python
        serializer = BookSerializer(data = data);
        if serializer.is_valid():
            serializer.save();
            return Response({
                'statusCode': 201,
                'message': 'Create books query was successful',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED);
        else:
            return Response({
                'statusCode': 400,
                'message': 'Create books query was failed',
                'error': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST);
    except:
        return Response({
            'statusCode': 500,
            'message': 'Create book query internal server error',
            'error': serializer.errors
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR);



###################################
# GET BOOK
###################################
@api_view(['GET'])
def getSingleBook(request, pk):
    try:
        if request.method == 'GET':
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)
            return Response({
                'statusCode': 200,
                'message': 'Get book query was successful',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Get book query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Get book query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


###################################
# UPDATE BOOK
###################################
@api_view(['PUT'])
def updateBook(request, pk):
    try:
        data = request.data;

        if request.method == 'PUT':
            book = Book.objects.get(pk=pk);
            serializer = BookSerializer(book, data);
            if serializer.is_valid():
                serializer.save();
                return Response({
                    'statusCode': 200,
                    'message': 'Update book query was successful',
                    'data': serializer.data
                });
            else:
                return Response({
                    'statusCode': 400,
                    'message': 'Update book query was failed',
                    'error': serializer.errors
                });
    except Book.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Update book query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Update book query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR);


###################################
# DELETE BOOK
###################################
@api_view(['DELETE'])
def deleteBook(request, pk):
    try:
        if request.method == 'DELETE':
            book = Book.objects.get(pk=pk);
            book.delete();
            return Response({
                'statusCode': 200,
                'message': 'Delete book query was successful',
                'deleted': True
            });
    except Book.DoesNotExist:
        return Response({
            'statusCode': 404,
            'message': 'Delete book query was failed. No book was found',
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            'statusCode': 500,
            'message': 'Delete book query internal server error',
            'error': str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR);