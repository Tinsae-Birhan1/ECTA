import frappe
try:
    import simplejson as json
except (ImportError,):
    import json

@frappe.whitelist()
def get_exporter(self, *args, **kwargs):
    return frappe.db.sql("""
        select u.name, concat(u.first_name, ' ', u.last_name)
        from tabUser u,`tabHas Role` r
        where u.name = r.parent and r.role = 'Exporter'
    """); 