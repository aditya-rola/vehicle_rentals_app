# Copyright (c) 2025, Adi and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class RideBooking(Document):
	
	def validate(self):
		if not self.rate:
			frappe.throw("Please provide a Rate.")

		total_distance = 0
		for dis in self.items:
			total_distance += dis.distance

		self.total_amount = self.rate * total_distance