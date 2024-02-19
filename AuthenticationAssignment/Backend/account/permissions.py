from rest_framework.permissions import BasePermission



class isTeacherUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_teacher)
    
class isStudentUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_student)