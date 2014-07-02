from django.db import models
import useraccounts
from librehatti.catalog.models import *
from django.contrib.auth.models import User

class QuotedOrder(models.Model):
    quote_buyer_id = models.ForeignKey(User)
    quote_is_debit = models.BooleanField()
    quote_delivery_address = models.ForeignKey('useraccounts.Address')
    quote_organisation = models.ForeignKey('useraccounts.AdminOrganisations')
    quote_date_time = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return '%s' % (self.quote_buyer_id) +' - ' '%s' % (self.quote_date_time.strftime ('%b %d, %Y'))

class QuotedItem(models.Model):
    quote_order = models.ForeignKey(PurchaseOrder)
    quote_price = models.IntegerField()
    quote_qty = models.IntegerField()
    quote_discount= models.IntegerField()
    quote_item = models.ForeignKey(Product)
    status = models.IntegerField(default=0)
    def save(self):
        if not self.id:
            self.quote_price = self.quote_item.price * self.quote_qty
        super(QuotedItem,self).save()

    def __unicode__(self):
        return '%s' % (self.quote_item) + ' - ' '%s' % (self.quote_order)


	
	
