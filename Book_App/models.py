from django.db import models

# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    qty = models.IntegerField()
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "Book"

    def __str__(self):
        return self.Name
        


