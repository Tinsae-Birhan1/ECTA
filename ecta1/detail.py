import frappe

def get_context(context):
  context.show_sidebar = 1
  context.dispatch = frappe.db.get_values("ECTA Dispatch", {'name': frappe.form_dict.dispatch}, "*", as_dict=True)
#   context.delivery_notices = frappe.db.get_list("Delivery Notice", "*", filters={"booking":frappe.form_dict.booking})