import frappe

def get_context(context):
  context.show_sidebar = 1
  context.exporter = frappe.get_list("Exporter", filters={'user': frappe.session.user}, fields={'exporter_name','exporter_id'})
  context.csrt_token = frappe.sessions.get_csrf_token()