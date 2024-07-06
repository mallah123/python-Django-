from django.db import models

# Create your models here.



# # api/models.py

# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     full_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=10)

#     def __str__(self):
#         return self.username

# class ContentItem(models.Model):
#     title = models.CharField(max_length=30)
#     body = models.TextField(max_length=300)
#     summary = models.TextField()
#     categories = models.ManyToManyField('Category')

#     def __str__(self):
#         return self.title

# class Category(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name




# api/models.py

# api/models.py

# from # api/models.py

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class GroupMembership(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'group')

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.email

    # Define many-to-many relationships with intermediate models
    groups = models.ManyToManyField(Group, through=GroupMembership, related_name='users', blank=True)
    user_permissions = models.ManyToManyField(Permission, through='UserPermission', related_name='users', blank=True)

class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'permission')



# api/models.py

from django.db import models

class ContentItem(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=300)
    summary = models.TextField()
    # Other fields as per your requirements
    
    def __str__(self):
        return self.title


# api/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
