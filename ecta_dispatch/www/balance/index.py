import frappe
from datetime import datetime,date
from ecta_dispatch.api.ecta_webpage_permission_api import checkPermisson


def get_context(context):
    context.UserAvatar = frappe.session.user.upper()[0]
    context.user = frappe.session.user
    context.side_bar_ecta =frappe.get_doc('ECTA Sidebar', 'ECTA sidebar')
    context.side_bar_group = "ECTA"
    context.uid= frappe.session.user
    
    if(checkPermisson("balance")):
        
        
        year = date.today().year
        context.year = year

        context.incoming = {}
        context.balance = {}
        context.outgoing = {}
    
        dispatches = frappe.db.get_list("ECTA Dispatches", filters={'creation':['between', (str(year)+"-01-01", str(year)+"-12-31")]}, fields=["received_volume_in_ton", "sent_warehouse"])
        balances = frappe.db.get_all("Warehouse Balance",  fields=['name', 'balance', 'year', 'parent'])
        outgoings = frappe.db.get_list("Outgoing Dispatch", filters={'creation':['between', (str(year)+"-01-01", str(year)+"-12-31")]}, fields=['warehouse', 'net_weight'])
        warehouses_list = frappe.db.get_list("ECTA Approved Warehouses", fields=["name"], order_by="name asc")
        print("88****************************************************************")
        print(dispatches)
        print('print balances********************************************************')
        print(balances)
        print('outgoings************************************************************')
        print(outgoings)
        print("88****************************************************************")
        context.dispatches = dispatches
        for dispatch in dispatches:
            
            print("dispatch sent warehouse")
            print(dispatch.sent_warehouse)
            if dispatch.sent_warehouse in context.incoming:
                context.incoming[dispatch.sent_warehouse] = context.incoming[dispatch.sent_warehouse] + dispatch.received_volume_in_ton
            else:
                context.incoming[dispatch.sent_warehouse] = dispatch.received_volume_in_ton
        
            print("context.incoming")
            print(context.incoming)
        for balance in balances:
            if balance.parent in context.balance:
                context.balance[balance.parent] = context.balance[balance.parent] + balance.balance
            else:
                context.balance[balance.parent] =  balance.balance
            print('######################################################balace parents********************************************************')
            print(balance.parent)
        for outgoing in outgoings:
            if outgoing.warehouse in context.outgoing:
                context.outgoing[outgoing.warehouse] = context.outgoing[outgoing.warehouse] + outgoing.net_weight
            else:
                context.outgoing[outgoing.warehouse] =  outgoing.net_weight

        data = {}
        for incoming in context.incoming:
            value = context.incoming[incoming]
            data[incoming] = value - (.2*value)

            if incoming in context.balance:
                data[incoming] = data[incoming] + context.balance[incoming]

        for outgoing in context.outgoing:
            if outgoing in data:
                data[outgoing] = data[outgoing] - context.outgoing[outgoing]
            else:
                data[outgoing] = 1*(context.outgoing[outgoing])

        context.all_warehouses = []
        warehouse = {}

        for warehouse in warehouses_list:
            warehouse["name"] = warehouse.name
            
            if warehouse.name in context.incoming:
                warehouse["incoming"] = str("{:,}".format(context.incoming[warehouse.name]))
                warehouse["wastage"] = str("{:,.2f}".format(.2*context.incoming[warehouse.name]))
            else:
                warehouse["incoming"] = 0
                warehouse["wastage"] = 0

            if warehouse.name in context.outgoing:
                warehouse["outgoing"] = str("{:,.2f}".format(context.outgoing[warehouse.name]))
            else: warehouse["outgoing"] = 0

            if warehouse.name in context.balance:
                warehouse["balance"] = str("{:,.2f}".format(context.balance[warehouse.name]))
            else: warehouse["balance"] = 0

            if warehouse.name in data:
                warehouse["total"] = str("{:,.2f}".format(data[warehouse.name]))
            else: warehouse["total"] = 0


            context.all_warehouses.append(warehouse)
            warehouse = {}      

        




        

 


    

