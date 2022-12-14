import frappe
from ecta_dispatch.api.ecta_webpage_permission_api import checkPermisson

def get_context(context):
    context.UserAvatar = frappe.session.user.upper()[0]
    context.user = frappe.session.user
    context.side_bar_ecta =frappe.get_doc('ECTA Sidebar', 'ECTA sidebar')
    context.side_bar_group = "ECTA"
    context.uid= frappe.session.user
    
    if(checkPermisson("abroadECTA")):
      context.show_sidebar = 1
      context.csrf_token = frappe.sessions.get_csrf_token()

      if("Market Inspection and Control Team" in frappe.get_roles(frappe.session.user)):
        context.dispatches = frappe.db.get_list("Outgoing Dispatch", fields=['exporter','exporter_id','warehouse','name','commodity_type','dispatch_approval','processing_type','coffee_grade','package_type','quantity_of_package','net_weight','total_weight','total_weight','crop_year','driver_name','driver__phone_number','truck_plate_number','container_number','serial_number','other','picture','approve','approved_by','date_of_approval','date_of_approval','unit_price','dispatch_approval','warehouse_outgoing_voucher','port'])
        
        print(context.despatches) 
      else:
        frappe.local.flags.redirect_location = "/warehouse"
        raise frappe.Redirect
      #context.warehouse = frappe.db.get_list("Warehouse",'*',filters={'warehouse_name':"Goods In Transit"});
      
 
     