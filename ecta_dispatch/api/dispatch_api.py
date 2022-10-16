import frappe
from frappe.utils.data import pretty_date

@frappe.whitelist()
def get_dispatches_2(*args, **kwargs):
    frappe.response["draw"] = frappe.form_dict.draw

    #### end filter

    if frappe.form_dict['order[0][column]'] == "0":
        order_info = "modified desc"
    else:
        order_info = frappe.form_dict["columns["+frappe.form_dict['order[0][column]']+"][name]"]+ " "+frappe.form_dict["order[0][dir]"]
    
    warehouse = frappe.get_list("ECTA Approved Warehouses", or_filters={'warehouse_owner': frappe.session.user, 'warehouse_operator': frappe.session.user}, fields={'warehouse_name','name'})   

    if warehouse:
        search_dictionary = {
            "warehouse": warehouse[0].name,
            # 'destination': ['like', "%"+frappe.form_dict['search[value]']+"%"],
        }

        outgoing_dispatches = frappe.db.get_list("Outgoing Dispatch", filters=search_dictionary, or_filters={'exporter': ['like', "%"+frappe.form_dict['search[value]']+"%"],'destination': ['like', "%"+frappe.form_dict['search[value]']+"%"]}, fields=['name','exporter','commodity_type','processing_type','coffee_grade', 'warehouse','dispatch_approval', 'destination','package_type','quantity_of_package', 'net_weight','total_weight', 'creation', 'modified', 'warehouse_outgoing_voucher'], order_by = order_info,start=frappe.form_dict.start, page_length=frappe.form_dict.length)
        outgoing_dispatches_total = frappe.db.get_list("Outgoing Dispatch", filters=search_dictionary, fields=['name','exporter','commodity_type','processing_type','coffee_grade', 'warehouse','dispatch_approval', 'destination','package_type','quantity_of_package', 'net_weight','total_weight', 'warehouse_outgoing_voucher', 'modified'], order_by = order_info)


        #### values to be displayed in the tables

        i = int(frappe.form_dict["start"])+1
        arranged_list_value = []
        arranged_list = []
        
        if len(outgoing_dispatches)>0:
            for dispatch in outgoing_dispatches:
                arranged_list.append(i)
                arranged_list.append(dispatch.exporter)
                arranged_list.append(dispatch.warehouse)
                arranged_list.append(dispatch.destination)
                arranged_list.append(dispatch.commodity_type)
                arranged_list.append(dispatch.net_weight)
                arranged_list.append(pretty_date(dispatch.creation))
                arranged_list.append(pretty_date(dispatch.modified))
                if dispatch.dispatch_approval == "Seen":
                    arranged_list.append("<span class=''>seen</span>")
                elif dispatch.dispatch_approval == "Reject":
                    arranged_list.append("<span class=''>Rejected</span>")
                else:
                    arranged_list.append("<a href='/outgoing-dispatch?name="+dispatch.name +"' class='btn text-center'>Edit</a>")
                
                arranged_list_value.append(arranged_list)
                arranged_list=[]
                i = i+1
            
            #### end of values to be displayed in the tables

        frappe.response["data"] = arranged_list_value
        frappe.response["recordsTotal"] = len(outgoing_dispatches_total)
        frappe.response["recordsFiltered"] = len(arranged_list_value)

@frappe.whitelist()
def get_available_by_warehouse(*args, **kwargs):
    year = frappe.form_dict.year
 
    dispatches = frappe.db.get_list("ECTA Dispatches", filters={'creation':['between', (str(year)+"-01-01", str(year)+"-12-31")]}, fields=["received_volume_in_ton", "sent_warehouse"])
    balances = frappe.db.get_all("Warehouse Balance", filters={'year':year}, fields=['name', 'balance', 'year', 'parent'])
    outgoings = frappe.db.get_list("Outgoing Dispatch", filters={'creation':['between', (str(year)+"-01-01", str(year)+"-12-31")]}, fields=['warehouse', 'net_weight'])
    warehouses_list = frappe.db.get_list("ECTA Approved Warehouses", fields=["name"], order_by="name asc")

    incoming = {}
    balance = {}
    outgoing = {}

    for dispatch in dispatches:
        if dispatch.sent_warehouse in incoming:
            incoming[dispatch.sent_warehouse] = incoming[dispatch.sent_warehouse] + dispatch.received_volume_in_ton
        else:
            incoming[dispatch.sent_warehouse] = dispatch.received_volume_in_ton
    
    for balance in balances:
        if balance.parent in balance:
            balance[balance.parent] = balance[balance.parent] + balance.balance
        else:
            balance[balance.parent] =  balance.balance
    
    for outg in outgoings:
        if outg.warehouse in outgoing:
            outgoing[outg.warehouse] = outgoing[outg.warehouse] + outg.net_weight
        else:
            outgoing[outg.warehouse] =  outg.net_weight

    tt_data(incoming, outgoing, balance, warehouses_list, frappe.form_dict.type)

@frappe.whitelist()
def get_available_by_exporter(*args, **kwargs):
    year = frappe.form_dict.year
  
    dispatches = frappe.db.get_list("ECTA Dispatches", filters={'creation':['between', (str(year)+"-01-01", str(year)+"-12-31")]}, fields=["received_volume_in_ton", "exporter_id", "exporter_name"])
    # balances = frappe.db.get_all("Warehouse Balance", filters={'year':year}, fields=['name', 'balance', 'year', 'parent'])
    outgoings = frappe.db.get_list("Outgoing Dispatch", filters={'creation':['between', (str(year)+"-01-01", str(year)+"-12-31")]}, fields=['exporter_id', 'net_weight'])
    exporter_list = frappe.db.get_list("Exporter", fields=["name", "exporter_id"], order_by="name asc")

    incoming = {}
    balance = {}
    outgoing = {}
    exporter = {}

    for dispatch in dispatches:
        if dispatch.exporter_id in incoming:
            incoming[dispatch.exporter_id] = incoming[dispatch.exporter_id] + dispatch.received_volume_in_ton
        else:
            incoming[dispatch.exporter_id] = dispatch.received_volume_in_ton
    
    frappe.errprint(incoming)
    # for exporter in exporter_list:  
    #     exporter[exporter.exporter_id] = exporter.exporter_name
    
    for outg in outgoings:
        if outg.exporter_id in outgoing:
            outgoing[outg.exporter_id] = outgoing[outg.exporter_id] + outg.net_weight
        else:
            outgoing[outg.exporter_id] =  outg.net_weight
    
    data = {}
    for incom in incoming:
        value = incoming[incom]
        data[incom] = value - (.2*value)

    for outg in outgoing:
        if outg in data:
            data[outg] = data[outg] - outgoing[outg]
        else:
            data[outg] = outgoing[outg]

    

    all_datas = []
    data = {}

    for exp in exporter_list:

        data["name"] = exp.name
        data["exporter_id"] = exp.exporter_id
        
        if exp.exporter_id in incoming:
            data["incoming"] = str("{:,}".format(incoming[exp.exporter_id]))
            data["wastage"] = str("{:,.2f}".format(.2*incoming[exp.exporter_id]))
        else:
            data["incoming"] = 0
            data["wastage"] = 0

        if exp.exporter_id in outgoing:
            data["outgoing"] = str("{:,.2f}".format(outgoing[exp.exporter_id]))
        else: data["outgoing"] = 0

        if exp.exporter_id in balance:
            data["balance"] = str("{:,.2f}".format(balance[exp.exporter_id]))
        else: data["balance"] = 0

        if exp.exporter_id in data:
            data["total"] = str("{:,.2f}".format(data[exp.exporter_id]))
        else: data["total"] = 0

        all_datas.append(data)
        data = {}      

    frappe.response['data'] = all_datas

def tt_data(incoming, outgoing, balance, warehouses_list, data_type):
    
    data = {}
    for incom in incoming:
        value = incoming[incom]
        data[incom] = value - (.2*value)

        if incom in balance:
            data[incom] = data[incom] + balance[incom]

    for outg in outgoing:
        if outg in data:
            data[outg] = data[outg] - outgoing[outg]
        else:
            data[outg] = outgoing[outg]

    all_warehouses = []
    warehouse = {}

    frappe.errprint(outgoing)

    for warehouse in warehouses_list:
        warehouse["name"] = warehouse.name
        
        if warehouse.name in incoming:
            warehouse["incoming"] = str("{:,}".format(incoming[warehouse.name]))
            warehouse["wastage"] = str("{:,.2f}".format(.2*incoming[warehouse.name]))
        else:
            warehouse["incoming"] = 0
            warehouse["wastage"] = 0

        if warehouse.name in outgoing:
            warehouse["outgoing"] = str("{:,.2f}".format(outgoing[warehouse.name]))
        else: warehouse["outgoing"] = 0

        if warehouse.name in balance:
            warehouse["balance"] = str("{:,.2f}".format(balance[warehouse.name]))
        else: warehouse["balance"] = 0

        if warehouse.name in data:
            warehouse["total"] = str("{:,.2f}".format(data[warehouse.name]))
        else: warehouse["total"] = 0

        all_warehouses.append(warehouse)
        warehouse = {}      

    frappe.response['data'] = all_warehouses