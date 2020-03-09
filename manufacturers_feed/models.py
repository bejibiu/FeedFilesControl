from django.db import models

BRAND_LEN = 200


class Brand(models.Model):
    name = models.CharField(max_length=BRAND_LEN)


def get_feed_dir(instance, filename):
    return f'{instance.brand.name}/{filename}'


class Feed(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    feed_file = models.FileField(upload_to=get_feed_dir)

