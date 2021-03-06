# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from shop.models_bases import BaseProduct
from shop.models_bases.managers import (
    ProductManager,
    ProductStatisticsManager,
)


class Product(BaseProduct):
    slug = models.SlugField(verbose_name=_('Slug'), unique=True)

    objects = ProductManager()
    statistics = ProductStatisticsManager()

    class Meta(object):
        abstract = False
        app_label = 'shop'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
