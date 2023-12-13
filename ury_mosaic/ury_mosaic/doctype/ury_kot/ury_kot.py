# Copyright (c) 2023, Tridz Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
import requests
import json
from frappe.utils.print_format import print_by_server
from frappe.model.document import Document


class URYKOT(Document):
    def on_submit(self):
        Pos_profile = frappe.get_doc("POS Profile", self.pos_profile)
        # if Pos_profile.is_network_printing:
        self.multi_print_kot()
        self.kotDisplayRealtime()
    def before_submit(self):
        self.userSetting()

    # Function for printing multiple KOTs.
    def multi_print_kot(self):
        Pos_profile = frappe.get_doc("POS Profile", self.pos_profile)

        # Function for printing a KOT on a specified printer using a print format.
        def print_kot(printer, kot_print_format):
            try:
                print_by_server("URY KOT", self.name, printer.name, kot_print_format)
            except:
                pass

        if self.production:
            production = frappe.get_doc("URY Production Unit", self.production)
            for printer in production.printer_settings:
                if printer.custom_kot_print == 1:
                    Printer = frappe.get_doc(
                        "Network Printer Settings", printer.printer
                    )
                    print_kot(Printer, printer.custom_kot_print_format)

        if self.restaurant_table:
            restaurant_table = frappe.get_doc("URY Table", self.restaurant_table)
            room = frappe.get_doc("URY Room", restaurant_table.restaurant_room)
            pos_print_flag = True

            try:
                if room.printer_settings:
                    for room_printer in room.printer_settings:
                        if room_printer.custom_kot_print == 1:
                            pos_print_flag = False
                            Printer = frappe.get_doc(
                                "Network Printer Settings", room_printer.printer
                            )
                            print_kot(Printer, room_printer.custom_kot_print_format)
            except:
                pass

            if pos_print_flag == True:
                for printer in Pos_profile.printer_settings:
                    if printer.custom_kot_print == 1:
                        Printer = frappe.get_doc(
                            "Network Printer Settings", printer.printer
                        )
                        print_kot(Printer, printer.custom_kot_print_format)

        else:
            for printer in Pos_profile.printer_settings:
                if printer.custom_kot_print == 1:
                    Printer = frappe.get_doc(
                        "Network Printer Settings", printer.printer
                    )
                    print_kot(Printer, printer.custom_kot_print_format)

    # Function for displaying KOT-related information in real-time On KDS(Kitchen Display System)
    def kotDisplayRealtime(self):
        currentBranch = self.branch
        production = self.production
        kotjson = json.loads(frappe.as_json(self))
        audio_file = frappe.db.get_value(
            "POS Profile", self.pos_profile, "custom_kot_alert_sound"
        )
        cache_key = "{}_{}_last_kot_time".format(currentBranch, production)
        time = frappe.cache().get_value(cache_key)
        kot_channel = "{}_{}_{}".format("kot_update", currentBranch, production)
        frappe.publish_realtime(
            kot_channel,
            {"kot": kotjson, "audio_file": audio_file, "last_kot_time": time},
        )
        frappe.cache().set_value(cache_key, self.time)

    def userSetting(self):
        userDoc = frappe.get_doc("User", self.owner)
        self.user = userDoc.full_name
