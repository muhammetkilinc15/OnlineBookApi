import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kitap_pazari.settings')

import django
django.setup()
### Modellerimize ve django içeriklerine erişmek için yukarıdaki gibi ayarlamaları yapmamız lazım
### SIRALAMA ÇOK ÖNEMLİ

from django.contrib.auth.models import User

from faker import Faker

import requests

from  books.api.serializers import BookSerializer
from books.models import Book,Author


def set_user(fakegen=None):
    if fakegen is None:
        fakegen = Faker(['en_US'])

    f_name = fakegen.first_name()
    l_name = fakegen.last_name()
    u_name = f_name.lower() + '_' + l_name.lower()
    email = f'{u_name}@{fakegen.domain_name()}'

    user_check = User.objects.filter(username=u_name)
	##### BÖYLE BİR USERNAME VARSA HATA ALACAĞIZ BUNUN İÇİN BİR VALIDATION YAPIYORUZ
    while user_check.exists():
        print(f'Böyle bir kullanıcı var zaten: {u_name}')
        u_name = f_name + '_' + l_name + str(random.randrange(1, 999))
        user_check = User.objects.filter(username=u_name)


    user = User(
        username =  u_name,
        first_name =  f_name,
        last_name = l_name,
        email =  email,
    )

    user.set_password('testing123')
    user.save()

    user_check = User.objects.filter(username=u_name)[0]
    print(f'Kullanici {user_check.username}, {user_check.id} id numarası ile kaydedildi. ')
  

from pprint import pprint  
def add_book(subject=None):
    fake = Faker(['en_US'])
    url = 'http://openlibrary.org/search.json'
    payload = {'q': subject}
    response = requests.get(url, params=payload)
 
    if response.status_code != 200:
        print('Hatalı istek yapıldı', response.status_code)
        return
    jsn = response.json()
    books = jsn.get('docs')
    author = Author.objects.get(pk=1)
    for book in books:
        book_name = book.get('title')
        data = dict(
            name = book_name,
            author = author.id,  
            description = book.get('text'),
            published_date = fake.date_time_between(start_date='-10y', end_date='now', tzinfo=None)
        )
        serializer= BookSerializer
        if serializer.is_valid():
            serializer.save()
            print('kitap kaydedildi: ', kitap_adi)
        else:
            continue
    pprint(data)