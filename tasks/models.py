from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, 
                             on_delete=models.CASCADE, 
                             blank=True, null=True,
                             verbose_name='Author')
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(null=True, blank=True, 
                                   verbose_name='Description')
    complete = models.BooleanField(default=False, verbose_name='Complete')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['-complete']
