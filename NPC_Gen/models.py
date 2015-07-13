from django.db import models


# Create your models here.


class NPC(models.Model):
    name = models.CharField(max_length = 255)
    race = models.CharField(max_length = 255)
    char_class = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

    #TODO: Add alignment to NPC
    #TODO: Add attributes to NPC
    #TODO: Add skills to NPC
    #TODO: Add HP and AC to NPC
