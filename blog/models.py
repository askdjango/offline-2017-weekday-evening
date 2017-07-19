from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


def min_length_3(value):
    if len(value) < 3:
        raise ValidationError('3글자 이상 입력해주세요.')


class Post(models.Model):
    author = models.CharField(max_length=20, help_text='글쓴이 이름을 입력해주세요.')
    title = models.CharField(max_length=100,
            validators=[min_length_3],
            help_text='제목은 간결하게!!')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        # return '/weblog/{}/'.format(self.id)
        return reverse('blog:post_detail', args=[self.id])

