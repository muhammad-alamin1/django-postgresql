from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify

def get_year_in_school_choices():
    return [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]

class Author(models.Model):
    name = models.CharField(max_length=100)
    # other fields

    def __str__(self):
        return self.name

# orm schema
class OrmTestModel(models.Model):
    
    
    user_id = models.BigAutoField(primary_key=True, unique=True, editable=False, help_text="This field is not editable in the admin interface.")
    user_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date = models.DateField()
    time = models.DateTimeField()
    duration = models.DurationField()
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    float_f = models.FloatField()
    year_in_school = models.CharField(max_length=2, choices=get_year_in_school_choices)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255, unique=True)
    url = models.URLField(max_length=200)
    photo = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='documents/')
    unique_code = models.CharField(max_length=50, verbose_name="Unique Code.", help_text="Enter a unique code for this entry.")
    integer_field = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], verbose_name="Integer Field", help_text="Enter an integer between 0 and 100.", error_messages={
        'min_value': 'The value cannot be less than 0.',
        'max_value': 'The value cannot be greater than 100.',
    })
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name