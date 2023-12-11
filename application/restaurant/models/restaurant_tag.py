from django.db import models


class RestaurantTag(models.Model):
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag.name