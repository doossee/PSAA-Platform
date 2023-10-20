from django.db import models
from django.contrib.auth.models import User
import django_filters
from datetime import datetime

current_year = datetime.now().year
current_month = datetime.now().month

start_date = datetime(current_year, current_month, 1)
end_date = start_date.replace(month=current_month + 1) if current_month < 12 else start_date.replace(year=current_year + 1, month=1)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField() 
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-publish_date',]

    def __str__(self):
        return self.title


class PostFilter(django_filters.FilterSet):
    creator = django_filters.CharFilter(field_name='creator__username')
    publish_date__gte = django_filters.DateTimeFilter(field_name='check_in', lookup_expr='gte')
    publish_date__lt = django_filters.DateTimeFilter(field_name='check_in', lookup_expr='lt')

    class Meta:
        model = Post
        fields = {
            'creator': ['exact', ],
            'publish_date':[],
        }