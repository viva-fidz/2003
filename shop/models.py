from django.db import models
from django.core.urlresolvers import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings
from django.utils.translation import to_locale, get_language, ugettext_lazy as _
import uuid
from simple_shop.models import *
from properties.models import ProductProperty, CategoryProperty
from filters.models import ProductFilter, FilterCategory


def make_upload_path(instance, filename, prefix=False):
    """
    Create unique name for image or file.
    """
    new_name = str(uuid.uuid1())
    parts = filename.split('.')
    f = parts[-1]
    filename = new_name + '.' + f
    return u"%s/%s" % (settings.SHOP_IMAGE_DIR, filename)


class Category(MPTTModel, OrderingBaseModel):
    """
    Category of products
    extend ItemBaseModel
    which has name,
    description, keywords
    """


    name = models.CharField(_("Название"),
                            default="",
                            max_length=250)
    url = models.CharField(_("Scrapy Url"),
                           default="",
                           blank=True,
                           max_length=250)
    title = models.CharField(_("Заголовок"),
                             blank=True,
                             default="",
                             max_length=250)
    description = models.CharField(_("Описание"),
                                   blank=True,
                                   default="",
                                   max_length=250)
    keywords = models.CharField(_("Keywords"),
                                blank=True,
                                default="",
                                max_length=250)
    parent = TreeForeignKey('self',
                            null=True,
                            blank=True,
                            related_name='children',
                            verbose_name=_('Parent'))
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name=_('Image'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductList', args=[self.id])

    def get_products(self):
        return Product.objects.filter(category=self)

    def get_products_price(self):
        products = Product.objects.filter(category=self)
        return products.order_by('price')

    def get_products_name(self):
        products = Product.objects.filter(category=self)
        return products.order_by('name')

     def get_products_inquote(self):
        products = Product.objects.filter(category=self)
        return products[:4]

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    class MPTTMeta:
        order_insertion_by = ['created_at']


class Product(OrderingBaseModel):
    category = models.ForeignKey(Category, related_name='products', verbose_name="Категория")
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    image = models.ImageField(upload_to='products/%Y_%m_%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе", blank=True)
    available = models.BooleanField(default=True, verbose_name="Доступен", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # checker_runtime = models.ForeignKey(SchedulerRuntime, blank=True, null=True, on_delete=models.SET_NULL)


    def save(self, *args, **kwargs):
        if self.category:
            super(Product, self).save(*args, **kwargs)
            # we create properties if not exist
            for cp in CategoryProperty.objects.filter(category=self.category):
                pp = ProductProperty.objects.filter(category_property=cp,
                                                    product=self)
                if not pp:
                    pp = ProductProperty(category_property=cp, product=self, value="--")
                    pp.save()
            # we create filters if not exist
            for fc in FilterCategory.objects.filter(category=self.category):
                pf = ProductFilter.objects.filter(filter_category=fc,
                                                  product=self)
                if not pf:
                    pf = ProductFilter(filter_category=fc, product=self)
                    pf.save()

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id])


    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class Offer(OrderingBaseModel):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='offers',
                                null=True,
                                verbose_name=_('Продукт'))
    name = models.CharField(_("Name"),
                            default="",
                            max_length=250)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                null=True,
                                default=0.00,
                                verbose_name=_('Цена'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Offer')
        verbose_name_plural = _('Offers')


class Images(OrderingBaseModel):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images',
                                null=True,
                                verbose_name=_('Продукт'))
    image = models.ImageField(
        upload_to=make_upload_path,
        blank=True,
        default="",
        verbose_name=_('Image'))

    name = models.CharField(_("Name"),
                            default="",
                            max_length=250)

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)

    class Meta:
        verbose_name = _('Изображение')
        verbose_name_plural = _('Изображения')
