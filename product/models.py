from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    image = models.ImageField(default='default.jpg', upload_to='post_image/')
    quantity = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name

