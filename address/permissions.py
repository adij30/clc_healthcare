from rest_framework.permissions import BasePermission, SAFE_METHODS


class MyReadOnly(BasePermission):
    def has_permission(self, request, view):
        print('method type is: ', request.method)
        if request.method == 'GET':
            print('user is - ', request.user.__dict__)
            return True
        else:
            return False