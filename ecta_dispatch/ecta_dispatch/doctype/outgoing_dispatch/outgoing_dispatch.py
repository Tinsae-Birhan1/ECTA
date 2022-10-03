# Copyright (c) 2022, Across Express and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OutgoingDispatch(Document):
	pass

	def before_save(self):
		warehouse = frappe.get_list("ECTA Approved Warehouses", or_filters={'warehouse_owner': frappe.session.user, 'warehouse_operator': frappe.session.user}, fields={'warehouse_name','name'})
		if warehouse:
			self.warehouse = warehouse[0]["name"]


		