from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    cat_img = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Title")
    news_img = models.ImageField(upload_to='images/')
    details = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Name")
    email = models.CharField(max_length=100, verbose_name="Email")
    comment = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.comment