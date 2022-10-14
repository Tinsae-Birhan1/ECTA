
import frappe
def get_context(context):
 
 user= frappe.session.user
 context.UL = user.upper()
 context.user = user
 routes = frappe.db.get_list('Ecta roles for page', pluck='route_name')
 print("hello from base")
 print(routes)
 
 return context

