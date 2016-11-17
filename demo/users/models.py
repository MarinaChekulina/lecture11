from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Переопределяем пользователя, добавляем аватарку и подписчиков
    """
    avatar = models.ImageField(null=True, verbose_name='Аватарка', upload_to='avatars')
    subscribes = models.ManyToManyField('self', verbose_name='Подписки', symmetrical=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def subscribed(self):
        """
        Кто подписан на пользователя
        """
        return User.objects.filter(subscribes=self)

    def subscribed_on(self, user):
        """
        Подписан ли на пользователя
        """
        return User.objects.filter(id=self.id, subscribes=user).exists()
