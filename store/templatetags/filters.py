from django import template

register =template.Library()

def promotion_price(price ,promotion):
    return int(price)*int(promotion)/100


def promotioned(product):
    return int(product.price)*int(product.promotion)/100

register.filter('promotion_price',promotion_price)
register.filter('promotioned',promotioned)
