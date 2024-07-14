from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='categories/')
    is_enable = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='products/')
    is_enable = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPES = (
        (FILE_AUDIO, 'audio'),
        (FILE_VIDEO, 'video'),
        (FILE_PDF, 'pdf')
    )

    product = models.ForeignKey(Product, related_name='files', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/%Y/%m/')
    is_enable = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    file_type = models.IntegerField(choices=FILE_TYPES, default=FILE_VIDEO)


    def __str__(self):
        return self.title


