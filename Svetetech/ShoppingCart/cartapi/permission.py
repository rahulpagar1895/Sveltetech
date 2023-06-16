from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['user']).exist()


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['super-admin']).exist()


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name__in=['admin']).exist()

