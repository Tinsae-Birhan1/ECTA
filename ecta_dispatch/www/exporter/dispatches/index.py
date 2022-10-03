import frappe

def get_context(context):
  context.show_sidebar = 1
  context.exporter = frappe.get_list("Exporter", filters={'user': frappe.session.user}, fields={'exporter_name','exporter_id'})

  context.dispatches = {}
  if context.exporter:
    context.dispatches = frappe.db.get_list("ECTA Dispatches", filters={"exporter_id": context.exporter[0].exporter_id}, fields=['center','exporter_name','sent_warehouse','status','drivers_name', 'serial_number','drivers_phone','eta','name','creation','excel_import','date_of_received','received_volume_in_bag','proof_of_delivery','coffee_type'], order_by='status desc',)
