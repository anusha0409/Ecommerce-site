from django.db import models

class Categorie(models.Model):
    name=models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Categorie.objects.all()
    
    @staticmethod
    def get_category_by_id(ids):
        return Categorie.objects.get(id__in =ids)

    def __str__(self):
        return self.name
