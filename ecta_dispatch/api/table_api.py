from dis import dis
import frappe
from frappe.utils.data import pretty_date
from numpy import disp

@frappe.whitelist()
def get_outgoing_dispatches(*args, **kwargs):
    frappe.response["draw"] = frappe.form_dict.draw

    # search_dictionary = {
    #         "exporter": exporter[0].name,
    #         'name': "%"+frappe.form_dict['search[value]']+"%",
    #     }
    #### end filter

    if frappe.form_dict['order[0][column]'] == "0":
        order_info = "creation desc"
    else:
        frappe.errprint(frappe.form_dict['order[0][column]'] )
        order_info = frappe.form_dict["columns["+frappe.form_dict['order[0][column]']+"][name]"]+ " "+frappe.form_dict["order[0][dir]"]
    
    outgoing_dispatches = frappe.db.get_list("Outgoing Dispatch", or_filters={'exporter': ['like', "%"+frappe.form_dict['search[value]']+"%"],'destination': ['like', "%"+frappe.form_dict['search[value]']+"%"],'warehouse': ['like', "%"+frappe.form_dict['search[value]']+"%"]}, fields=['name','exporter','commodity_type','processing_type','coffee_grade', 'destination', 'warehouse', 'package_type','quantity_of_package', 'net_weight','total_weight', 'warehouse_outgoing_voucher', 'creation', 'dispatch_approval'], order_by = order_info,start=frappe.form_dict.start, page_length=frappe.form_dict.length)
    outgoing_dispatches_total = frappe.db.get_list("Outgoing Dispatch", fields=['name','exporter','commodity_type','processing_type','coffee_grade', 'destination', 'warehouse', 'package_type','quantity_of_package', 'net_weight','total_weight', 'warehouse_outgoing_voucher', 'creation', 'dispatch_approval', 'modified'], order_by = order_info)


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
            arranged_list.append(pretty_date(dispatch.modified))
            if dispatch.dispatch_approval == "Seen":
                arranged_list.append("<span >Approved</span>")
            elif dispatch.dispatch_approval == "Reject":
                arranged_list.append("<span class='bad bdge-danger'>Rejected</span>")
            else:
                arranged_list.append("<a href='/outgoing-dispatch-approval-form?name="+dispatch.name +"' class='btn text-center btn-success'>Approve</a>")
            
            arranged_list_value.append(arranged_list)
            arranged_list=[]
            i = i+1
        
        #### end of values to be displayed in the tables

    frappe.response["data"] = arranged_list_value
    frappe.response["recordsTotal"] = len(outgoing_dispatches_total)
    frappe.response["recordsFiltered"] = len(arranged_list_value)

