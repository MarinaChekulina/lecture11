from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    image = models.ImageField(upload_to='posts', verbose_name='Картинка')
    text = models.TextField(null=True, blank=True, verbose_name='Текст')
    user = models.ForeignKey(User, verbose_name='Кто запостил')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return '{0}: {1} {2}'.format(self.user, self.text, self.created_at)

    def likes_count(self):
        return self.like_set.count()

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'


class Like(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)

    def __str__(self):
        return '{0} {1}'.format(self.post, self.user)
