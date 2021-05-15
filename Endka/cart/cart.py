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


    def add(self,item, quantity=1, override=False):
        item_id=str(item.id)
        if item_id not in self.cart:
            self.cart[item_id]={
            'quantity':0,
            'price':str(item.price)
            }
        if override:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def __iter__(self):

        item_ids=self.cart.keys()
        items=Item.objects.filter(id__in=item_ids)
        cart=self.cart.copy()
        for item in items:
            cart[str(item.id)]['item']=item

        for i in cart.values():
            i['price'] = Decimal(i['price'])
            i['total_price'] = i['price'] * i['quantity']
            yield i



    def save(self):
        self.session.modified=True


    def remove(self):
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()


    def get_total(self):
        return sum(Decimal(i['price']) * i['quantity'] for item in self.cart.values())


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()