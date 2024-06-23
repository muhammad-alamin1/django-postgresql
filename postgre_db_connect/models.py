from django.db import models

# Create your models here.
class ConnectDB(models.Model):
    DEFAULT_USER_VALUE = "user"
    USER_ROLE = {
        "ADMIN": "admin",
        "USER": "user",    
    }
    
    user_id = models.PositiveBigIntegerField(primary_key=True, unique=True)
    user_name = models.CharField(max_length=25, unique=True)
    user_role = models.CharField(choices=USER_ROLE, default=DEFAULT_USER_VALUE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField(max_length=255)
    
    
    def __str__(self):
        return self.user_name