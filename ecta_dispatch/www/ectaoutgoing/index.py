import frappe

def get_context(context):
  context.show_sidebar = 1
  context.csrf_token = frappe.sessions.get_csrf_token()
#   context.new_dispatches = frappe.db.get_list("ECTA Dispatches", filters={'file_attached_by':frappe.session.user}, fields=['center','exporter_name','sent_warehouse','exporter_type','name','creation','excel_import'])
  # if("Market Inspection and Control Team" in frappe.get_roles(frappe.session.user)):
  #   context.dispatches = frappe.db.get_list("Outgoing Dispatches", fields=['center','exporter_name','sent_warehouse','exporter_type','name','creation','excel_import','status', 'proof_of_delivery','name','approved'], order_by='status asc')
  # else:
  #   frappe.local.flags.redirect_location = "/warehouse"
  #   raise frappe.Redirect
  #  # context.warehouse = frappe.db.get_list("Warehouse",'*',filters={'warehouse_name':"Goods In Transit"});