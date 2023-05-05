from django.shortcuts import render, redirect
from .forms import BookForm, MemberForm, BarrowedBookForm, SignUpForm
from .models import Book, Member, BarrowedBook, User
from django.core import serializers


def is_not_logged_in(request):
    member_id = request.session.get('member_id', '')
    return member_id == 'None'


def index(request):
    barrowed_books = BarrowedBook.objects.filter(is_returned=False).all()
    books = Book.objects.order_by('-id').all()
    for book in books:
        book.quantity -= barrowed_books.filter(
            book_id=book.id).all().count()
    return (render(request, 'index.html', {'books': books, 'json_books': serializers.serialize('json', books)}))


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.filter(
            email=email, password=password).first()
        if user != None and user.is_approved:
            request.session['member_id'] = user.id
            request.session['member_name_surname'] = user.name_surname
            request.session['member_is_admin'] = user.is_admin
            return redirect('index')
        else:
            exception_message = 'Email veya şifre yanlış, tekrar deneyiniz' if user == None else 'Onay bekleniyor'
            return (render(request, 'login.html', {'exceptionMessage':  exception_message}))
    return (render(request, 'login.html'))


def logout(request):
    request.session['member_id'] = 'None'
    request.session['member_name_surname'] = 'None'
    request.session['member_is_admin'] = 'None'
    return redirect('index')


def signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        user = User.objects.filter(email=email).first()
        if user != None:
            form = SignUpForm
            return (render(request, 'signup.html', {'form': form, 'exceptionMessage': 'Başka bir email deneyiniz.'}))
        form = SignUpForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect('login')
    else:
        form = SignUpForm
        return (render(request, 'signup.html', {'form': form}))


def members(request):
    if (is_not_logged_in(request)):
        return redirect('login')
    members = Member.objects.order_by('-id')
    return (render(request, 'members.html', {'members': members}))


def barrowed_books(request):
    if (is_not_logged_in(request)):
        return redirect('login')
    barrowed_books = BarrowedBook.objects.all()
    return (render(request, 'barrowed_books.html', {'barrowed_books': barrowed_books}))


def barrowed_books_post(request, id='None'):
    if (is_not_logged_in(request)):
        return redirect('login')
    if request.method == "POST":
        instance = BarrowedBook.objects.filter(id=id).first()
        instance.is_returned = True
        instance.save()
        return redirect('barrowed_books')
    else:
        return redirect('barrowed_books')


def barrow_a_book(request, book_id):
    if (is_not_logged_in(request)):
        return redirect('login')
    if request.method == "POST":
        form = BarrowedBookForm(request.POST)
        if form.is_valid() and form.cleaned_data.get('member_id') != 0:
            form = form.save()
            return redirect('index')
        else:
            book = Book.objects.filter(id=book_id).first()
            members = Member.objects.order_by('-name_surname')
            return (render(request, 'barrow_a_book.html', {'book': book, 'members': members, 'exceptionMessage': 'Lütfen bir üye seçiniz.'}))
    else:
        book = Book.objects.filter(id=book_id).first()
        members = Member.objects.order_by('-name_surname')
        return (render(request, 'barrow_a_book.html', {'book': book, 'members': members}))


def add_book(request):
    if (is_not_logged_in(request)):
        return redirect('login')
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save()
            return redirect('index')
    else:
        form = BookForm
        return (render(request, 'add_book.html', {'form': form}))


def add_member(request):
    if (is_not_logged_in(request)):
        return redirect('login')
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            if Member.objects.filter(email=form.cleaned_data.get('email')).exists():
                return (render(request, 'add_member.html', {'form': form, 'exceptionMessage': 'Email veritabanında kayıtlı lütfen başka bir email deneyiniz'}))
            if Member.objects.filter(identity_number=form.cleaned_data.get('identity_number')).exists():
                return (render(request, 'add_member.html', {'form': form, 'exceptionMessage': 'T.C Kimlik No veritabanında kayıtlı lütfen başka bir no deneyiniz'}))
            if Member.objects.filter(phone_number=form.cleaned_data.get('phone_number')).exists():
                return (render(request, 'add_member.html', {'form': form, 'exceptionMessage': 'Cep telefonu veritabanında kayıtlı lütfen başka bir cep telefonu deneyiniz'}))
            form = form.save()
            return redirect('members')
    else:
        form = MemberForm
        return (render(request, 'add_member.html', {'form': form}))


def users(request):
    if (is_not_logged_in(request)):
        return redirect('login')
    if (request.session['member_is_admin'] == False):
        return redirect('index')
    users = User.objects.filter(is_admin=False).all()
    return (render(request, 'users.html', {'users': users}))


def users_update(request, id='None'):
    if (is_not_logged_in(request)):
        return redirect('login')
    if request.method == "POST":
        instance = User.objects.filter(id=id).first()
        instance.is_approved = False if instance.is_approved else True
        instance.save()
    return redirect('users')
