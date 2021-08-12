from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AppManager(BaseModel):
    class Meta:
        verbose_name = ' 앱관리'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self._meta.verbose_name


class GenderCategory(BaseModel):
    value = models.CharField(max_length=16)
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    manager = models.ForeignKey(AppManager, on_delete=models.DO_NOTHING, default=1, related_name='genders')

    class Meta:
        verbose_name = '성별 카테고리'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


class AgeCategory(BaseModel):
    min = models.PositiveIntegerField(null=True, blank=True)
    max = models.PositiveIntegerField(null=True, blank=True)
    str = models.CharField(max_length=32, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    manager = models.ForeignKey(AppManager, on_delete=models.DO_NOTHING, default=1, related_name='ages')

    class Meta:
        verbose_name = '나이 카테고리'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.str or f'{self.min}~{self.max}세'


class PriceCategory(BaseModel):
    value = models.PositiveIntegerField()
    str = models.CharField(max_length=32, blank=True)
    is_active = models.BooleanField(default=True, verbose_name='활성화')
    manager = models.ForeignKey(AppManager, on_delete=models.DO_NOTHING, default=1, related_name='prices')

    class Meta:
        verbose_name = '가격 카테고리'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.str or f'{self.value}원'


class User(AbstractUser):
    class Meta:
        verbose_name_plural = '회원관리'


class ProductCategory(BaseModel):
    value = models.CharField(max_length=32)

    class Meta:
        verbose_name = '상품 카테고리'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


class Product(BaseModel):
    code = models.AutoField(primary_key=True, verbose_name='코드')
    name = models.CharField(max_length=128, verbose_name='상품명')
    category = models.ForeignKey(ProductCategory, verbose_name='상품유형', related_name='products', on_delete=models.CASCADE)
    # img = models.ImageField(verbose_name='썸네일')
    description = models.TextField(blank=True, verbose_name='상품소개')
    vendor = models.CharField(max_length=64, verbose_name='판매처')
    views = models.PositiveIntegerField(default=0, verbose_name='노출수')
    likes = models.PositiveIntegerField(default=0, verbose_name='좋아요수')
    # likes = models.PositiveIntegerField(default=0, verbose_name='주문수')
    gender = models.ManyToManyField(GenderCategory, verbose_name='성별', related_name='products')
    age = models.ManyToManyField(AgeCategory, verbose_name='연령', related_name='products')
    price = models.ForeignKey(PriceCategory, verbose_name='가격', related_name='products', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품관리'

    def __str__(self):
        return self.name






