from django.db import models


class Subscribe(models.Model):
    subscribes = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False, db_index=True,
        related_name='subscribe_by'
    )
    fans = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False, db_index=True,
        related_name='subscribe'
    )
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
