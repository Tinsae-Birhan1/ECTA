import frappe

def get_context(context):
    year = frappe.form_dict.year
    exporter = frappe.form_dict.exporter

    context.show_sidebar = 1

    context.dispatches = frappe.db.get_list("ECTA Dispatches", filters={'creation': ['between', (str(year)+"-01-01", str(year)+"-12-31")], 'exporter_id': exporter}, fields=["received_volume_in_ton", "sent_warehouse", 'exporter_name', 'creation'], order_by="creation desc")
    context.outgoings = frappe.db.get_list("Outgoing Dispatch", filters={'creation': ['between', (str(year)+"-01-01", str(year)+"-12-31")], 'exporter_id': exporter}, fields=['warehouse', 'net_weight', 'creation'], order_by="creation desc")
