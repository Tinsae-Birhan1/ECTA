
import frappe

def get_context(context):
  if(("Warehouse Owner" in frappe.get_roles(frappe.session.user)) or ("Warehouse Operator" in frappe.get_roles(frappe.session.user))):
   print("Not permitted")
  else:
    frappe.local.flags.redirect_location = "/"
    raise frappe.Redirect
  