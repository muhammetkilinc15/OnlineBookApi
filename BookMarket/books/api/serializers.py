from rest_framework import serializers
from books.models import Book,Comment,Author


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        #fields = '__all__'
        exclude = ('book',) # kitap dısındakiler gelecek
 
 
     
# read-only diyerek bir kitap girilecen de yorum girilmesini beklemicek   
class BookSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Book
        fields = ['id','comments', 'name', 'description', 'created_date', 'updated_date', 'published_date',]
        

    
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Use 'books' to match the related_name in the Book model

    class Meta:
        model = Author
        fields = ['id', 'name', 'surname', 'birthDate', 'age', 'books']