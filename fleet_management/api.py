import frappe
@frappe.whitelist()

def check_vehicle(vehicle: str):
    vehicle1=frappe.get_doc("Vehicle", vehicle)
    return vehicle1.status
