from decimal import Decimal
from django.conf import settings
from service.models import Item

class Cart(object):
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID]={}
        self.cart=cart

    def add(self,item, count=1, override=False):
        item_id=str(item.id)
        if item_id not in self.cart:
            self.cart[item_id]={
            'count':0,
            'price':str(item.price)
            }
        if override:
            self.cart[product_id]['count'] = count
        else:
            self.cart[product_id]['count'] += count
        self.save()

    def save(self):
        self.session.modified=True
    def remove(self):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()
    def get_total(self):
        return sum(Decimal(i['price']) * i['count'] for item in self.cart.values())
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()