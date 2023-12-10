from django.db import models


class Collection(models.Model):
    collectors = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False, db_index=True,
        related_name='collectors'
    )
    collections = models.ForeignKey(
        'restaurant.Restaurant', on_delete=models.CASCADE, null=False, db_index=True,
        related_name='collections'
    )
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    class Meta:
        ordering = ['-created_at']