from django.db import models

class Costomer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    confirm_password = models.CharField(max_length=500)
    number = models.CharField(max_length=10, null=True)
    
    @staticmethod
    def get_costomer_by_email(email):
        return Costomer.objects.get(email = email)

    def isExist(self):
        if Costomer.objects.filter(email = self.email):
            return True

        return False    