from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import ListModelMixin,CreateModelMixin

from rest_framework import generics
from rest_framework.generics import get_object_or_404

from books.api.serializers import BookSerializer,CommentSerializer,AuthorSerializer
from books.models import Book,Author,Comment



#! Concreta View İle 

#? Kitap Listeleme ve Olusturma 
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer # serializer_class özniteliğini 

#? Kitap detaylarına gitme
class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer # serializer_class özniteliğini 
    
#? Yazar olusturma ve listeleme
class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

#? Yazar detaylarına gitme
class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer # serializer_class özniteliğini 
    
#? Yorum olusturma 
class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        # 'book_pk' URL parametresini al
        book_pk = self.kwargs.get('book_pk')
        # 'book_pk' parametresinin eksik olup olmadığını kontrol et
        if book_pk is None:
            raise ValidationError("Book primary key is required.")
        
        # 'book_pk' ile kitap objesini getir, eğer yoksa 404 hatası döndür
        book = get_object_or_404(Book, pk=book_pk)
        
        # Yorumun kaydedilmesi sırasında kitap objesini ilişkilendir
        serializer.save(book=book)

#? Yorum güncelleme silme
class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    
    
    
    
    
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