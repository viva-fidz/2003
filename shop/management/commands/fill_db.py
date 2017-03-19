from django.core.management.base import BaseCommand
from simple_shop.models import *
from shop.models import *


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Автомобильные аккумуляторы', 'url': '#'},
            {'name': 'Преобразователи напряжения', 'url': '#'},
        ]

        products = [
            {'category': 'Автомобильные аккумуляторы',
             'name': 'Mega Ватт 6ст-60',
             'description': 'Стартовая свинцово-кислотная аккумуляторная батарея предназначена для пуска двигателей и обеспечения энергией электрического оборудования легковых автомобилей',
             'price': '3050',
             'available': '576'},

            {'category': 'Автомобильные аккумуляторы',
             'name': 'START.Bat 60',
             'description': 'Автомобильный аккумулятор START.Bat 60 Ач о.п подойдет для современных транспортных средств. Эти модели АКБ производятся по технологии Ca/Ca и соответствуют международным стандартам, поэтому этот аккумулятор может использоваться в современных автомобилях. Модель START.Bat 60 Ач о.п имеет повышенную емкость электродов. Корпус батареи – европейский с обратной полярностью.',
             'price': '3199',
             'available': '576'},

            {'category': 'Преобразователи напряжения',
             'name': 'PMega Ватт 6ст-60',
             'description': 'Преобразователи Модель START.Bat 60 Ач о.п имеет повышенную емкость электродов. Корпус батареи – европейский с обратной полярностью.Преобразователи напряжения',
             'price': '3050',
             'available': '576'},

            {'category': 'Преобразователи напряжения',
             'name': 'PSTART.Bat 60',
             'description': 'Преобразователи Модель START.Bat 60 Ач о.п имеет повышенную емкость электродов. Корпус батареи – европейский с обратной полярностью.Преобразователи напряжения',
             'price': '3199',
             'available': '576'},
        ]
        Category.objects.all().delete()
        for category in categories:
            category = Category(**category)
            category.save()

        Product.objects.all().delete()
        for product in products:
            product_category = product['category']
            category = Category.objects.get(name=product_category)
            product['category'] = category
            product = Product(**product)
            product.save()
