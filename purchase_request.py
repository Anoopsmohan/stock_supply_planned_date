# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
from trytond.model import ModelSQL, ModelView
from trytond.pool import Pool

class PurchaseRequest(ModelSQL, ModelView):
    _name = 'purchase.request'

    def generate_requests(self):
        move_obj = Pool().get('stock.move')
        # For stock moves which are not yet received from the supplier, the 
        # planned date has to be updated to the current date. If it is not
        # the future stock will not include those moves.
        #
        # If this step is not done, tryton assumes that all moves from supplier
        # which have a planned date before today and not received will never 
        # be received, prompting the purchase request algorithm to create new
        # purchase requests for such orders.
        move_obj.update_supply_planned_date()
        return super(PurchaseRequest, self).generate_requests()

PurchaseRequest()
