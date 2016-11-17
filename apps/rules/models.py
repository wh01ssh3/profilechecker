from django.db import models
from django_extensions.db.models import TitleDescriptionModel


class Rule(TitleDescriptionModel):
    """Model for storing rules

    Rules is a pieces of code, which can be checked separately or in profile

    Attributes:
        code (str): Piece of code to check
    """

    code = models.TextField()

    def __str__(self):
        return self.title


class Profile(TitleDescriptionModel):
    """Model for storing profiles

    Profile is a set of rules. Profile can be checked (rules of this profile
    will be checked altogether) and can be schedule to check.

    Attributes:
        rules (list[Rule]): List of rules
    """

    rules = models.ManyToManyField('rule')

    def __str__(self):
        return self.title
