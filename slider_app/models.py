from django.db import models
from django.core.validators import FileExtensionValidator

news_img = models.FileField(upload_to="pictures/%Y/%m/", validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])


class LogoAndContacts(models.Model):
    """ Логотип и контактная информация фирмы. """

    logo = models.FileField("Логотип", upload_to="images/logo/", validators=[FileExtensionValidator(['svg',])])
    logo_name = models.CharField("Название фирмы", max_length=30)
    phone = models.CharField("Телефон", max_length=20)
    address = models.CharField("Адрес", max_length=60)


class Soc(models.Model):
    """ Иконки, ссылки соцсетей и шеринга. """

    icon = models.FileField("Иконка", upload_to="images/soc_icons/", validators=[FileExtensionValidator(['svg', ])])
    link = models.URLField("Ссылка на аккаунт", max_length=100, blank=True)
    share = models.CharField("Ссылка шеринга", max_length=100, blank=True)
    alt = models.CharField("Alt инфо", max_length=30, blank=True)
    publish = models.BooleanField("Опубликовать", default=False)


class SliderItem(models.Model):
    """ Фото и текст страницы слайдера. """

    image = models.ImageField("Изображение", upload_to="images/slider_img/")
    header = models.CharField("Заголовок слайдера", max_length=60, blank=True)
    description = models.TextField("Описание", blank=True)
    publish = models.BooleanField("Опубликовать", default=False)


class Mail(models.Model):
    """ Заявки отправленные с сайта. """

    name = models.CharField("Имя", max_length=70)
    phone = models.CharField("Телефон", max_length=20)
    message = models.TextField("Сообщение")
    date = models.DateTimeField("Дата", auto_now_add=True)
