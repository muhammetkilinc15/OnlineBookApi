# OnlineBookApi
## Kurulum

```bash
 python -m venv myenv
```
* Kurulumdan sonra activate.bat çalıştırıyoruz. 

```bash
 py myenv/scripts/activate.bat
```
* Django Kurulum
```bash
 pip install django
```

* Django Rest Api Framework Kurulum
```bash
 pip install djangorestframework
```


** Biz ekstra
```bash
 pip install django_extensions
```
# Yükleme

* Kurulum işlemleri bittikten sonra django projemizi oluşturuyoruz

```bash
 django-admin startproject onlineBookApi
```

* Rest Framework ve extension yüklemiştik. Onları settings.py içerisine ekliyoruz
```bash
 pip install djangorestframework


 # settings.py
INSTALLED_APPS = [
    ...

    'rest_framework',
    'django_extensions',
]
