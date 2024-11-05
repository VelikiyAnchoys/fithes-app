from django.db import models
from pytils.translit import slugify

class Category(models.Model):
    name= models.CharField("Название категории", max_length=255)
    slug= models.SlugField(unique=True, editable=False, blank=True)

    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class Zal(models.Model):
    title =models.CharField("Название зала", max_length=255)
    category=models.ForeignKey(Category, on_delete= models.CASCADE, verbose_name="Выберите категорию")
    detail_title= models.CharField("Оценка зала", max_length=100)
    imo=models.ImageField(upload_to='images/', null=True, blank=True)
    description= models.TextField("Описание зала")
    adress=models.CharField("Адрес", max_length=255, default="ул. Абиша Кекилбайулы, 38А/1, Алматы (этаж 1)" )
    telephone=models.CharField("телефон", max_length=25)
    time=models.CharField(" Рабочие часы", max_length=25, default="06:00–23:00")
    price=models.CharField("Стоимость абонемента", max_length=80)

    class Meta:
        verbose_name="Зал"
        verbose_name_plural="Залы"

    def __str__(self):
        return self.title


class Abonement(models.Model):
    names =models.CharField("Название абонемента", max_length=255)
    category=models.ForeignKey(Category, on_delete= models.CASCADE, verbose_name="Выберите категорию")
    training= models.CharField("Количество тренеровок", max_length=100, default='безлимит(месяц)')
    descriptions= models.CharField("Скидка", max_length=100)
    times=models.CharField(" Сколько человек приобрело", max_length=45)
    prices=models.CharField("Стоимость абонемента", max_length=80)

    class Meta:
        verbose_name="Абонемент"
        verbose_name_plural="Абонементы"

    def __str__(self):
        return self.names


class Trener(models.Model):
    foto= models.ImageField(upload_to='images/', null=True, blank=True)
    first_name =models.CharField("ФИО тренера", max_length=255)
    category=models.ForeignKey(Category, on_delete= models.CASCADE, verbose_name="Выберите категорию")
    det_title= models.CharField("Опыт работы", max_length=100)
    specialization= models.CharField("Специализация", max_length=100)
    describing_trener=models.CharField("Награды", max_length=255, default="Не указано")
    lessons_tren=models.CharField("Цена занятий", max_length=255,default="Не указано")
    contact=models.CharField("Контакты", max_length=30, default="Не указано")

    class Meta:
        verbose_name="Тренер"
        verbose_name_plural="Тренера"

    def __str__(self):
        return self.first_name

        
class Pitanie(models.Model):
    pit_card_name=models.CharField("Название вида питания", max_length=100)
    image = models.ImageField(upload_to='images/')
    kall_text=models.CharField("Подбирание питания по категории",max_length=255)
    kall_description= models.TextField("Рекомендации по подбору питания")
    kall_text_one=models.CharField("Составленик рациона", max_length=255)
    kall_description_one= models.TextField("Схема рациона питания")
    kall_text_two=models.CharField("Ежедневный рацион питания", max_length=255)
    kall_description_two= models.TextField("Схема ежедневного рациона питания")


    class Meta:
        verbose_name="Питание и диета"
        verbose_name_plural="Питание и диеты"

    def __str__(self):
        return self.pit_card_name


class DomTrenirovki(models.Model):
    exercise= models.CharField("Упражнение", max_length=50)
    quantity= models.CharField("Количество раз", max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name="Тренировки дом"
        verbose_name_plural="Тренировки дома"

    def __str__(self):
        return self.exercise


class SpecTren(models.Model):       
    exercise=models.CharField("название", max_length=50,default="Не указано")
    times=models.CharField("количество раз", max_length=50,default="Не указано")
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    class Meta:
        verbose_name="Специальная тренировка"
        verbose_name_plural="Специальные тренировки"

    def __str__(self):
        return self.exercise