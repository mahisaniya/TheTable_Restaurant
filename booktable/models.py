from django.db import models

# Create your models here.
class Bookingdetails(models.Model):
    customer_name=models.CharField(max_length=50 )
    contact=models.IntegerField()
    date=models.DateField()
    email=models.EmailField(max_length=50  , null=True)
    number_of_guest=models.CharField(max_length=6)
    time=models.TextField()

    def __str__(self):
        return self.customer_name + " -> " + str(self.id)