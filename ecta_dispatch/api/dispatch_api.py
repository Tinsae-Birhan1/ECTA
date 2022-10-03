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



