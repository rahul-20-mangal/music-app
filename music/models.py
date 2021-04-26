from django.db import models
from django.utils.text import slugify


class Music(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return "{} of album {}".format(self.title, self.album)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Music, self).save(*args, **kwargs)


class Album(models.Model):
    title = models.CharField(max_length=200)
    prefix = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    band = models.ForeignKey('Band', on_delete=models.CASCADE)
    label = models.ForeignKey('Label', on_delete=models.CASCADE)
    ASIN = models.CharField(max_length=10)
    released_date = models.DateField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='cover_image')
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return "{} by band {}".format(self.title, self.band)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Album, self).save(*args, **kwargs)


class Band(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Label(models.Model):
    name = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Genre(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        return super(Genre, self).save(*args, **kwargs)

    def __str__(self):
        return self.title