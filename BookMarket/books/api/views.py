from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import ListModelMixin,CreateModelMixin

from rest_framework import generics

from books.api.serializers import BookSerializer,CommentSerializer,AuthorSerializer
from books.models import Book,Author




class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer # serializer_class özniteliğini 


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer # serializer_class özniteliğini 
    
class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer # serializer_class özniteliğini 
    



#! Generic API VIEW ILE OLUSTURULDU
# class BookListCreateAPIView(ListModelMixin,CreateModelMixin, GenericAPIView):
#     # Queryset ve serializer_class değerlerini verdik
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer # serializer_class özniteliğini tanımladık
    
    
#     # Listelemek 
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     # Yeni Kitap Yaratak
#     def post(self, request, *args, **kwargs):
#         return self.create(request,*args,**kwargs)