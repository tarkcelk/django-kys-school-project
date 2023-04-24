from django import forms
from .models import Book, Member, BarrowedBook, User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class BarrowedBookForm(forms.ModelForm):
    class Meta:
        model = BarrowedBook
        fields = '__all__'


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class BarrowedBookForm(forms.ModelForm):
    class Meta:
        model = BarrowedBook
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
