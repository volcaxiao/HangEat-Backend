"""
用户发布在餐馆下的帖子
"""

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    grade = models.IntegerField(default=0, choices=((0, '未评分'), (1, '一星'), (2, '二星'), (3, '三星'), (4, '四星'), (5, '五星')))
    avg_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='post_image')
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    agree = models.IntegerField(default=0)

    recommend_dish = models.ManyToManyField('Dish', related_name='recommended_by', through='RecommendDish')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']
