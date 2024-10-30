from django.db import models

class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Категория"  # Единичное название
        verbose_name_plural = "Категории"  # Множественное название


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)  # категории продукта, например (обувь, сумки, одежда...)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"  # Единичное название
        verbose_name_plural = "Товары"  # Множественное название


# вопросы и ответы будут храниться в базе
class Answers_and_Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(verbose_name = "вопрос", max_length=290)
    answer = models.TextField(verbose_name = "ответ")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Вопросы и ответы"
        verbose_name_plural = "Вопросы и ответы"
