import frappe
from datetime import datetime,date


def get_context(context):
    year = date.today().year
    context.year = year

    context.incoming = {}
    context.balance = {}
    context.outgoing = {}
 
    dispatches = frappe.db.get_list("ECTA Dispatches", filters={'creation':['>=', str(year)+"-01-01"]}, fields=["volume_in_bag", "sent_warehouse"])
    balances = frappe.db.get_list("Warehouse Balance",filters={'year': year}, fields=['warehouse', 'balance', 'quarter'])
    outgoings = frappe.db.get_list("Outgoing Dispatch", filters={'creation':['>=', str(year)+"-01-01"]}, fields=['warehouse', 'total_weight'])

    for dispatch in dispatches:
        if dispatch.sent_warehouse in context.incoming:
            context.incoming[dispatch.sent_warehouse] = context.incoming[dispatch.sent_warehouse] + dispatch.volume_in_bag
        else:
            context.incoming[dispatch.sent_warehouse] = dispatch.volume_in_bag

    for balance in balances:
        if balance.warehouse in context.balance:
            context.balance[balance.warehouse] = context.balance[balance.warehouse] + balance.balance
        else:
            context.balance[balance.warehouse] =  balance.balance
    
    for outgoing in outgoings:
        if outgoing.warehouse in context.outgoing:
            context.outgoing[outgoing.warehouse] = context.outgoing[outgoing.warehouse] + outgoing.total_weight
        else:
            context.outgoing[outgoing.warehouse] =  outgoing.total_weight

    data = {}
    for incoming in context.incoming:
        value = context.incoming[incoming]
        data[incoming] = value 
        # - (.2*value)

    for outgoing in context.outgoing:
        if outgoing in data:
            data[outgoing] = data[outgoing] - context.outgoing[outgoing]
        else:
            data[outgoing] = -1*(context.outgoing[outgoing])

    context.data = data

    # context.data = {}
    # temp = {}

    # for d in data:
    #     temp['warehouse'] = data[d]
    #     temp['outgoing']
            

    




    

 


    

