import frappe

def get_context(context):
	# do your magic here
	pass

def before_save(self):
	warehouse = frappe.get_list("ECTA Approved Warehouses", filters={'primary_contact_email': frappe.session.user}, fields={'warehouse_name','name'})
	self.warehouse = warehouse[0]["name"]

