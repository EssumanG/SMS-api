from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.
import uuid
import bcrypt




class UserManager(BaseUserManager):
    def create_user(self, username, email, password, **other_fields):
        print("Create user from user manager!")
        if not email:
                raise ValueError("Users must have an email address")
        if not username:
                raise ValueError("Users must have an email address")
        # print("username", other_fields.get("username"))
        user = self.model(
            email = self.normalize_email(email), password=None, username=username, *other_fields
            )
        if not user:
            raise ValueError("No user was created")
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        if other_fields.get("is_staff") is not True:
            raise ValueError("is staff must be true for admin user")
        user = self.create_user(username, email, password, **other_fields)
        # user.save(using=self._db)
        return user

class AuthUser(AbstractBaseUser,  PermissionsMixin):
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=True)

    objects = UserManager()

    class Meta:
        db_table= "user_account"
    
    USERNAME_FIELD = "username"

    REQUIRED_FIELDS = ["email", "password"]

    def set_password(self, raw_password:str):
        self.password = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, raw_password):
        return bcrypt.checkpw(raw_password.encode('utf-8'), self.password.encode('utf-8'))