# from django.db import models
# from django.contrib.auth.models import AbstractUser, PermissionsMixin
# from django.utils.translation import gettext_lazy as _
# from django import utils
#
#
# class User(AbstractUser, PermissionsMixin):
#     first_name = models.CharField(_("first name"), max_length=30, blank=True)
#     last_name = models.CharField(_("last name"), max_length=30, blank=True)
#     username = models.EmailField(
#         _("username"),
#         unique=True,
#         error_messages={"unique": _("A user with that email address already exists.")},
#     )
#
#     email = models.EmailField(_("email address"), blank=True)
#     is_staff = models.BooleanField(
#         _("staff status"),
#         default=False,
#         help_text=_("Designates whether the user can log into this admin " "site."),
#     )
#     date_joined = models.DateTimeField(_("date joined"), default=utils.timezone.now)
#     phone_number = models.CharField(max_length=15, null=True)
#     alternate_phone_number = models.CharField(max_length=15, null=True)
#     name = models.CharField(_("User Role"), blank=True, max_length=255)
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]
#
#     class Meta:
#         verbose_name = _("user")
#         verbose_name_plural = _("users")
#
#
#
#     @property
#     def user_full_name(self):
#         return self.get_full_name()
#
#     def get_full_name(self):
#         """
#         Returns the first_name plus the last_name, with a space in between.
#         """
#         full_name = "%s %s" % (self.first_name, self.last_name)
#         return full_name.strip()
#     #
#     def get_role(self):
#         if self.groups.filter(name__in=('user')):
#             return 'user'
#         elif self.groups.filter(name__in=('super-admin')):
#             return 'super-admin'
#         elif self.groups.filter(name__in=('admin')):
#             return 'admin'
#
#     def __str__(self):
#         return self.username
#
#
#     def is_super_admin(self):
#         return (
#             True
#             if self.groups.filter(name__in=["agency-super-admin"]).exists()
#             else False
#         )
