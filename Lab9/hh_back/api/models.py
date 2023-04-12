from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField()
    adress = models.TextField()
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'adress': self.adress
        }
    
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey()
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'salary': self.salary,
            'company': self.company
        }
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'