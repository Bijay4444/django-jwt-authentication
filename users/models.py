from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    #Add feilds for Name, Email, Phone number, and Photo
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='user_photo/', blank=True, null=True)
    
    # This is require to specify the field used for username (for authentication)
    REQUIRED_FIELDS = ['name', 'phone_number']
    
    #setting related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', 
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.', 
    )
    
    
    def __str__(self):
        return self.email

class CustomUserManager(models.Manager):
    #this class is used for adding custom methods for maning users here if needed 
    pass

#Assigning the CustomUserManager to the CustomUser model    
CustomUser.objects = CustomUserManager()