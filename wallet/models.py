from django.db import models
from users.models import CustomUser

# Create your models here.


class Shylockentry(models.Model):

    TYPE_CHOICES = (("C", "creditor"), ("D", "debtor"))
    name = models.CharField(max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    deadline = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)

    # type- whether its a creditor or debtor
    type_choice = models.CharField(max_length=1, choices=TYPE_CHOICES)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, db_constraint=False)

    class Meta:
        db_table = "shylockentries"
        verbose_name_plural = "shylockentries"

    def __str__(self):
        # type = self.get_type_choices_display()
        printed_string = f'{self.name} is a {self.get_type_choice_display()} of {self.user} owing {self.amount}'
        return printed_string
