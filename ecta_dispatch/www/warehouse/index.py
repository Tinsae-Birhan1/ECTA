import frappe
from frappe.utils import pretty_date, now, add_to_date

def get_context(context):
  
  if(("Warehouse Owner" in frappe.get_roles(frappe.session.user)) or ("Warehouse Operator" in frappe.get_roles(frappe.session.user))):
    context.show_sidebar = 1
  #   context.new_dispatches = frappe.db.get_list("ECTA Dispatch", filters={'file_attached_by':frappe.session.user}, fields=['center','exporter_name','sent_warehouse','exporter_type','name','creation','excel_import'])
    context.warehouse = frappe.get_list("ECTA Approved Warehouses", or_filters={'warehouse_owner': frappe.session.user, 'warehouse_operator': frappe.session.user}, fields={'warehouse_name','name'})

    context.dispatches = update(context.warehouse)
      # context.warehouse = frappe.db.get_list("Warehouse",'*',filters={'warehouse_name':"Goods In Transit"});
  else:
    frappe.local.flags.redirect_location = "/"
    raise frappe.Redirect
  
  
def update(warehouse): 
  iterate = 0
  dispatches = frappe.db.get_list("ECTA Dispatches", filters={"sent_warehouse": warehouse[0].name}, fields=['center','exporter_name','sent_warehouse','status','drivers_name','drivers_phone','eta','name','serial_number', 'creation','excel_import','date_of_received','received_volume_in_bag','proof_of_delivery','coffee_type', 'approved', 'modified'], order_by='modified desc')
  # context.warehouse = frappe.db.get_list("Warehouse",'*',filters={'warehouse_name':"Goods In Transit"});
  for dispatch in dispatches :
    print(dispatches[iterate]['modified'])
    dispatches[iterate]['modified'] = pretty_date (dispatch['modified'])
    print(dispatches[iterate]['modified'])
    iterate +=1
  return dispatches

    
