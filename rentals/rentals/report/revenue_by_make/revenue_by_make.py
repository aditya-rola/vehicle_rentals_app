# Copyright (c) 2025, Adi and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data",
            "width": 300
        },
        {
            "fieldname": "total_revenue",
            "label": "Total Revenue",
            "fieldtype": "Currency",
            "width": 300
        },

    ]

    data = frappe.get_all("Ride Booking", fields=[
                          "SUM(total_amount) as total_revenue", "vehicle.make"], group_by="make")

    chart_data = {

        "labels": [dt.make for dt in data],
        "datasets": [
            {
                "values": [dt.total_revenue for dt in data]
            }
        ],
    }
    chart = {
        "data": chart_data,
        "type": "percentage"
    }
    return columns, data, "message", chart
