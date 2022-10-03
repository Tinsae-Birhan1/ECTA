# Copyright (c) 2022, Across Express and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import random_string


class ECTAApprovedWarehouses(Document):
	pass
	# def before_insert(self):
	# 	user = frappe.get_doc({
	# 		"doctype":"User",
	# 		"email": self.primary_contact_email,
	# 		"first_name": self.primary_contact_name,
	# 		"last_name": self.primary_contact_father_name,
	# 		"enabled": 1,
	# 		"new_password": self.primary_contact_name+"@1234AC",
	# 		"user_type": "Website User"
	# 	})
	# 	user.flags.ignore_permissions = True
	# 	user.insert()

	# 	self.primary_user = user.name

	# 	default_role = frappe.db.get_value("Warehouse Owner", "External User")
	# 	if default_role:
	# 		user.add_roles(default_role)
