from dataclasses import fields
import frappe

def get_context(context):
  context.show_sidebar = 1

  context.exporter = frappe.get_list("Exporter", filters={'user': frappe.session.user}, fields={'exporter_name','exporter_id'})

  context.dispatches = {}
  if context.exporter:
    context.outgoing_dispatches = frappe.db.get_list("Outgoing Dispatch", filters={'exporter':context.exporter[0]["exporter_id"]}, fields=['name','exporter','commodity_type','processing_type','coffee_grade','package_type','quantity_of_package', 'net_weight','total_weight', 'warehouse_outgoing_voucher', 'destination', 'modified'])
