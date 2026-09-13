# Copyright (c) 2026, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Maintenance(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		cost: DF.Currency
		date: DF.Date
		description: DF.Data
		vehicle: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Maintenance"
