from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import date, datetime  # datetime modülünü import ettik
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    birthDate = models.DateField()

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthDate.year - ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))

    def __str__(self):
        return f"{self.name} - {self.surname}"
    
        
    
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books',null=True)
    description = models.TextField(blank=True,null=True,max_length=3000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} -  {self.author}"
    

class Comment(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="comments")
    commenter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usercomments',null=True)
    comment = models.TextField(blank=True,null=True,max_length=3000)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)],)
    
    def __str__(self):
        return f"{self.commenter} - {self.book.name} {self.rating}"
    
