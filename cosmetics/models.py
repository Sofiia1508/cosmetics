from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=50, default="Unknown")

    def __str__(self):
        return self.name


class Book(models.Model):
    GENRE_CHOICES = [
        ('FIC', 'Fiction'),
        ('NF', 'Non-Fiction'),
        ('SCI', 'Science'),
        ('BIO', 'Biography'),
        ('FAN', 'Fantasy'),
    ]

    LANGUAGE_CHOICES = [
        ('EN', 'English'),
        ('UA', 'Ukrainian'),
        ('DE', 'German'),
        ('FR', 'French'),
    ]

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_year = models.PositiveIntegerField(default=2020)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES, default='FIC')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='EN')
    pages = models.PositiveIntegerField()
    in_stock = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

