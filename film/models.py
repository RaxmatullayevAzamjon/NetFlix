from django.db import models

j = (
    ("Erkak","Erkak"),
    ("Ayol","Ayol")
)
class Aktyor(models.Model):
    ism = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30, blank=True)
    jins = models.CharField(max_length=30,choices=j, blank=True)
    tugilgan_sana = models.DateField(blank=True)

    def str(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=30, blank=True)
    yil = models.DateField(blank=True)
    aktyorlar = models.ManyToManyField(Aktyor)

    def str(self):
        return self.nom


class Tarif(models.Model):
    nom = models.CharField(max_length=30)
    davomiyligi = models.CharField(max_length=40)
    narx = models.CharField(max_length=30)

    def str(self):
        return self.nom


