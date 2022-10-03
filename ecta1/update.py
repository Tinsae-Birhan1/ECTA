import frappe

def get_context(context):
  context.show_sidebar = 1
  context.booking = frappe.db.get_values("Booking Truck Shipment", {'name': frappe.form_dict.booking}, "*", as_dict=True)
#   context.delivery_notices = frappe.db.get_list("Delivery Notice", "*", filters={"booking":frappe.form_dict.booking})
