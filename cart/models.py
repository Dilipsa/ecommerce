from django.db import models

# Create your models here.

class Cart(models.Model):
    cloth_name = models.CharField(max_length=20, default="leggings")
    cloth_image = models.ImageField(upload_to='pics')
    GREY = 'GREY'
    BLACK = 'BLACK'
    YELLOW = 'YELLOW'
    RED    = 'RED'
    WHITE   = 'WHITE'
    GREEN  = 'GREEN'
    ORANGE = 'ORANGE'
    BLUE   = 'BLUE'
    BROWN  = 'BROWN'
    PINK   = 'PINK'
    CLOTH_COLOR_CHOICES = [
        (GREY, 'Grey'),
        (BLACK, 'Black'),
        (YELLOW, 'Yellow'),
        (RED, 'Red'),
        (WHITE, 'White'),
        (GREEN, 'Green'),
        (ORANGE, 'Orange'),
        (BLUE, 'Blue'),
        (BROWN,'Brown'),
        (PINK,'Pink'),
    ]
    cloth_color = models.CharField(max_length=10, choices=CLOTH_COLOR_CHOICES, default=RED,)

    cloth_price = models.CharField(max_length=20)
    cloth_offer = models.CharField(max_length=20)

    SMALL    = 'SMALL'
    MEDIUM   = 'MEDIUM'
    LARGE  = 'LARGE'
    X_LARGE = 'X LARGEL'
    XX_LARGE   = 'XX LARGE'
    CLOTH_SIZE_CHOICES = [
        (SMALL, 'Small'),
        (MEDIUM, 'Medim'),
        (LARGE, 'LARGE'),
        (X_LARGE, 'X-large'),
        (XX_LARGE, 'XX-large'),
    ]
    cloth_size = models.CharField(max_length=10, choices=CLOTH_SIZE_CHOICES, default=SMALL,)
    new = models.BooleanField(default=False)
    number = models.IntegerField()

    def __str_(self):
        return self.cloth_name
