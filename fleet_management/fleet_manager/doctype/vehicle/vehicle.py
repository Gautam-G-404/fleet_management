# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Vehicle(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amended_from: DF.Link | None
		model: DF.Data
		status: DF.Literal["Available", "In Trip", "Maintenance"]
		vehicle_number: DF.Data
		vehicle_type: DF.Data
	# end: auto-generated types

	def validate(self):
		if len(self.vehicle_number) < 5:
			frappe.throw("Vehicle number must be at least 5 characters long")
	def before_save(self):
		if self.status=='Maintenance' and not self.model:
			frappe.throw("Vehicle Model is required when vehicle status is Maintenance")

	def on_submit(self):
		if(self.status=='Maintenance'):
			frappe.msgprint("Your vehicle details submitted for maintenance successfully")
		else:
			frappe.msgprint("Vehicle details submitted successfully")
			
			
	_DOCTYPE_NAME = "Vehicle"

