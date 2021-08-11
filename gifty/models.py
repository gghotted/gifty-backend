from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AgeCategory(BaseModel):
    min = models.PositiveIntegerField(null=True)
    max = models.PositiveIntegerField(null=True)
    str = models.CharField(max_length=32, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.str or f'{self.min}~{self.max}'


class PriceCategory(BaseModel):
    value = models.PositiveIntegerField()
    str = models.CharField(max_length=32, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.str or f'{self.value}원'


class User(AbstractUser):
    class Meta:
        verbose_name_plural = '회원관리'


class Product(BaseModel):
    pass


