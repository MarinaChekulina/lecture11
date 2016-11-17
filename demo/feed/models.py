from django.db import models
from users.models import User


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

    def liked_by(self, user):
        return Like.objects.filter(post=self, user=user).exists()


class Like(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)

    def __str__(self):
        return '{0} {1}'.format(self.post, self.user)


class Comment(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ('created_at', )
