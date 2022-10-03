import frappe

def get_context(context):
#   context.show_sidebar = 1
# #   context.new_dispatches = frappe.db.get_list("ECTA Dispatch", filters={'file_attached_by':frappe.session.user}, fields=['center','exporter_name','sent_warehouse','exporter_type','name','creation','excel_import'])
#   context.dispatches = frappe.db.get_list("ECTA Dispatch", fields=['center','exporter_name','sent_warehouse','exporter_type','name','creation','excel_import','status', 'proof_of_delivery','name','approved'])
#   # context.warehouse = frappe.db.get_list("Warehouse",'*',filters={'warehouse_name':"Goods In Transit"});