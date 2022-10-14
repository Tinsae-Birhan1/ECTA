from dataclasses import fields
import frappe
from ecta_dispatch.api.ecta_webpage_permission_api import checkPermisson

def get_context(context):
    if(checkPermisson("outgoings")):
      context.show_sidebar = 1
      context.warehouse = frappe.get_list("ECTA Approved Warehouses", or_filters={'warehouse_owner': frappe.session.user, 'warehouse_operator': frappe.session.user}, fields={'warehouse_name','name'})

      context.outgoing_dispatches = frappe.db.get_list("Outgoing Dispatch", filters={'warehouse':context.warehouse[0]["name"]}, fields=['name','exporter','commodity_type','processing_type','coffee_grade','dispatch_approval','package_type','quantity_of_package', 'net_weight','total_weight', 'warehouse_outgoing_voucher'])
    #   if("Market Inspection and Control Team" in frappe.get_roles(frappe.session.user)):
    #     context.dispatches = frappe.db.get_list("ECTA Dispatches", fields=['center','exporter_name','sent_warehouse','exporter_type','name','creation','excel_import','status', 'proof_of_delivery','name','approved'], order_by='status asc')
    #   else:
    #     frappe.local.flags.redirect_location = "/warehouse"
    #     raise frappe.Redirect
      # context.warehouse = frappe.db.get_list("Warehouse",'*',filters={'warehouse_name':"Goods In Transit"});
      
      print(context.outgoing_dispatches)
      print(context.dispatch) 

  