from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field="username")
    birth_date = models.DateField(null=True, blank=True)

    def str(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"