from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    number_of_cats = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'students'

    def __str__(self):
        return f"{self.first_name}{self.last_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.number_of_cats = self.cat_set.count()
        super().save(*args, **kwargs)


class Cat(models.Model):
    name_of_cat = models.CharField(max_length=32)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'cats'

    def __str__(self):
        return f"{self.name_of_cat}"

