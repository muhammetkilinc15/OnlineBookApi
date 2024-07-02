from rest_framework import permissions
from pprint import pprint 


#!* Kullanıcı admın ise tüm yetkilere sahip ya da okuma işlemlerine sahip
class IsAdminUserOrReadOnly(permissions.IsAdminUser):
     def has_permission(self, request, view):
        is_admin = super().has_permission(request,view)
        return request.method in permissions.SAFE_METHODS or is_admin
        
    
class IsCommenterOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
                if request.method in permissions.SAFE_METHODS:
                        return True
                return request.user == obj.commenter
                  
                