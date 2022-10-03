# Copyright (c) 2022, Across Express and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ECTADispatches(Document):
	def validate(self):
		if self.approved == 1:
			# frappe.errprint("seen")
			self.status = "Seen"
		# else: 
			# frappe.errprint("not seen")
		# self.received_volume_in_ton = self.received_volume_in_ton/1000