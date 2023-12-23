from django.contrib import admin
from .models import Restaurant
from .models import Post
from .models import Tag
# Register your models here.

admin.site.register(Restaurant)

admin.site.register(Post)

admin.site.register(Tag)