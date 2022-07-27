from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    # image = models.ImageField(upload_to='images/', default="")
    # TODO add image field

    def __str__(self):
        date = str(self.created_on.date())
        return self.title + " | " + date

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
