import frappe

def get_context(context):
    year = frappe.form_dict.year
    warehouse = frappe.form_dict.warehouse
    context.show_sidebar = 1

    context.dispatches = frappe.db.get_list("ECTA Dispatches", filters={'creation': ['between', (str(year)+"-01-01", str(year)+"-12-31")], 'sent_warehouse': warehouse}, fields=["received_volume_in_ton", "sent_warehouse", 'exporter_name', 'creation'], order_by="creation desc")
    context.balances = frappe.db.get_all("Warehouse Balance", filters={'year':year, 'parent': warehouse}, fields=['balance', 'year', 'adjustment', 'creation'], order_by="creation desc")
    context.outgoings = frappe.db.get_list("Outgoing Dispatch", filters={'creation': ['between', (str(year)+"-01-01", str(year)+"-12-31")], 'warehouse': warehouse}, fields=['exporter', 'net_weight', 'creation'], order_by="creation desc")
