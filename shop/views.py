from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from shop.models import *
from simple_shop.forms import *
from .models import Product


# Create your views here.
def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    title = 'Главная'
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    return render(request, 'index.html', {'title': title,
                                          'products': products,
                                          'categories': categories
                                          })

# Страница с товарами
def ProductList(request, id):
    category = get_object_or_404(Category, id=id)
    categories = Category.objects.all()
    products = Product.objects.all()
    products.filter(category=category)
    return render(request, 'product/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def CategoryList(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'category/list.html', {
        'categories': categories,
        'products': products,

    })


# Страница товара
def ProductDetail(request, product_id=id):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=product_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    print(request.session.session_key)
    return render(request, 'product/detail.html', {'product': product, 'categories': categories} )


def contacts(request):
    title = 'Контакты'
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        # Если форма заполнена корректно, сохраняем все введённые                   пользователем значения
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            copy = form.cleaned_data['copy']

            recipients = ['viva.fidz@yandex.ru']
            # Если пользователь захотел получить копию себе, добавляем его в список получателей
            if copy:
                recipients.append(sender)
            try:
                send_mail(subject, message, 'viva.fidz@yandex.ru', recipients)
            except BadHeaderError:  # Защита от уязвимости
                return HttpResponse('Invalid header found')
                # Переходим на другую страницу, если сообщение отправлено
            return render(request, 'thanks.html', {'title': title, 'categories': categories})
    else:
        # Заполняем форму
        form = ContactForm()
        # Отправляем форму на страницу
    return render(request, 'contacts.html', {'title': title, 'form': form, 'categories': categories})


def thanks(request):
    categories = Category.objects.all()
    title = 'Контакты'
    return render(request, 'thanks.html', {'title': title,
                                           'categories': categories})

