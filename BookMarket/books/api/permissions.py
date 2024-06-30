from rest_framework import permissions
from pprint import pprint 


#!* Kullanıcı admın ise tüm yetkilere sahip ya da okuma işlemlerine sahip
class IsAdminUserOrReadOnly(permissions.IsAdminUser):
     def has_permission(self, request, view):
        is_admin = super().has_permission(request,view)
        return request.method in permissions.SAFE_METHODS or is_admin
        
    
pprint(dir(IsAdminUserOrReadOnly))