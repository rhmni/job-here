from django.db import models


class BaseModel(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Technology(BaseModel):
    pass


class Category(BaseModel):
    pass


class City(BaseModel):
    pass


class MinSalary(models.Model):
    price = models.PositiveBigIntegerField()

    def __str__(self):
        return str(self.price)
