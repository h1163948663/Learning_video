from django.core.exceptions import ValidationError

def valid_difficulty(n):
    if n > 5 or n <1:
        raise ValidationError("等级介于1到5之间")

def valid_difficulty1(n):
    if n >11 or n < 1 :
        raise ValidationError("数值介于1到11之间")