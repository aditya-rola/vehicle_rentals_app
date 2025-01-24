import frappe

def execute():

    vehicles = frappe.get_all("Vehicle", pluck="name")

    for vh in vehicles:
        vehicle = frappe.get_doc("Vehicle", vh)
        vehicle.set_title()
        vehicle.save()
    
    frappe.db.commit()