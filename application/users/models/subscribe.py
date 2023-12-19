from django.db import models


class Subscribe(models.Model):
    subscription = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False, db_index=True,
        related_name='subscribe_by'
    )
    subscriber = models.ForeignKey(
        'User', on_delete=models.CASCADE, null=False, db_index=True,
        related_name='subscribe'
    )
    created_at = models.DateTimeField(blank=False, null=False, auto_now_add=True)

    def is_mutual(self):
        return self.subscription in self.subscriber.subscribe_by.all()

    class Meta:
        ordering = ['-created_at']
