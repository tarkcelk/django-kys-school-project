from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    number_of_pages = models.PositiveIntegerField()
    summary = models.TextField(
        max_length=500, null=True, blank=True)
    date = models.DateTimeField(auto_now=False)
    quantity = models.IntegerField(blank=False)
    image = models.ImageField(upload_to='uploads/')


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name_surname = models.CharField(max_length=100, verbose_name='Adı Soyadı')
    identity_number = models.BigIntegerField(verbose_name='T.C Kimlik No')
    phone_number = models.BigIntegerField(verbose_name='Cep Telefonu')
    email = models.CharField(max_length=50)


class BarrowedBook(models.Model):
    id = models.AutoField(primary_key=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    returns_at = models.DateTimeField(blank=False)
    created_at = models.DateTimeField(blank=False, auto_now_add=True)
    is_returned = models.BooleanField(
        blank=True, default=False)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name_surname = models.CharField(max_length=100, verbose_name='Adı Soyadı')
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=False, auto_now_add=True)
    is_admin = models.BooleanField(blank=True, default=False)
    is_approved = models.BooleanField(blank=True, default=False)
