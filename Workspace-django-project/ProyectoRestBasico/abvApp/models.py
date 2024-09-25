from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)  
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.name} (SCORE: {self.score})"
