import frappe

def get_context(context):
  if(frappe.request.args):
    context.show_sidebar = 1
    context.csrf_token = frappe.sessions.get_csrf_token()
    query_params = frappe.request.args
    context.user = frappe.session.user
    context.doc = query_params["doc"]
    context.date = frappe.utils.getdate()

    if("Market Inspection and Control Team" in frappe.get_roles(frappe.session.user)):
      context.dispatch = frappe.db.get_list("Outgoing Dispatch", filters={"name":query_params["doc"] },fields=['name','exporter','destination','exporter_id','warehouse','name','commodity_type','dispatch_approval','processing_type','coffee_grade','package_type','quantity_of_package','net_weight','total_weight','total_weight','crop_year','driver_name','driver__phone_number','truck_plate_number','container_number','serial_number','other','picture','approve','approved_by','date_of_approval','date_of_approval','unit_price','dispatch_approval','warehouse_outgoing_voucher','port'])
      
      print(context.dispatch) 
    else:
      frappe.local.flags.redirect_location = "/"
      raise frappe.Redirect
    #context.warehouse = frappe.db.get_list("Warehouse",'*',filters={'warehouse_name':"Goods In Transit"});
  
    #ImmutableMultiDict([('name', 'helloIamworking')])
  else:
    frappe.local.flags.redirect_location = "/ectaoutgoing"
    raise frappe.Redirect