import frappe
from ecta_dispatch.api.ecta_webpage_permission_api import checkPermisson

def get_context(context):
    if(checkPermisson("outgoings")):
      context.UserAvatar = frappe.session.user.upper()[0]
      context.user = frappe.session.user
      context.side_bar_ecta =frappe.get_doc('ECTA Sidebar', 'ECTA sidebar')
      context.side_bar_group = "warehouse"
      context.uid= frappe.session.user
  