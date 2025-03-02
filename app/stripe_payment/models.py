from django.db import models


# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField()
    description = models.CharField()
    price = models.IntegerField()

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

    def __str__(self):
        return f"Item № {self.id}"
