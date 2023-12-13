import json

import frappe
from ury.ury_pos.api import getBranch


# Function to set order status in a KOT document
@frappe.whitelist()
def serve_kot(name, time):
    frappe.db.set_value("URY KOT", name, "start_time_serv", time)
    frappe.db.set_value("URY KOT", name, "order_status", "Served")


# Function to mark it as verified by a user in cancel type KOT
@frappe.whitelist()
def confirm_cancel_kot(name, user):
    frappe.db.set_value("URY KOT", name, "verified", 1)
    frappe.db.set_value("URY KOT", name, "verified_by", user)


@frappe.whitelist()
def kot_list():
    today = frappe.utils.now()
    branch = getBranch()
    kot_alert_time = frappe.db.get_value(
        "POS Profile", {"branch": branch}, "custom_kot_warning_time"
    )
    three_hours_ago = frappe.utils.add_to_date(today, hours=-3)
    audio_alert = frappe.db.get_value(
        "POS Profile", {"branch": branch}, "custom_kot_alert"
    )
    kotList = frappe.get_list(
        "URY KOT",
        fields=["name"],
        filters={
            "order_status": "Ready For Prepare",
            "branch": branch,
            "type": [
                "in",
                [
                    "New Order",
                    "Order Modified",
                    "Duplicate",
                    "Cancelled",
                    "Partially cancelled",
                ],
            ],
            "docstatus": 1,
            "verified": 0,
            "creation": (">=", three_hours_ago),
        },
        order_by="creation desc",
    )
    KOT = []
    for kot in kotList:
        kotdoc = frappe.get_doc("URY KOT", kot.name)
        kotjson = json.loads(frappe.as_json(kotdoc))
        KOT.append(kotjson)
    return {
        "KOT": KOT,
        "Branch": branch,
        "kot_alert_time": kot_alert_time,
        "audio_alert": audio_alert
    }

