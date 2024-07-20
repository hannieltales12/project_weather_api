from django.db import models

# Create your models here.

class WeatherData(models.Model):
    """Classe responsavel por realizar a modelagem de dados do clima que serão extraídos

    Args:
        models (_type_): _description_
    """
    cidade = models.CharField(max_length=100)
    latidude = models.CharField(max_length=50)
    logintude = models.CharField(max_length=50)
    estacao = models.CharField(max_length=100)
    id = models.CharField(max_length=100, primary_key=True)


    def __str__(self):
        return f"{self.estacao} - {self.cidade} - {self.latidude} - {self.logintude}"