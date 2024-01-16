from . import __version__ as app_version

app_name = "ury_mosaic"
app_title = "URY Mosaic"
app_publisher = "Tridz Technologies Pvt. Ltd."
app_description = "URY KOT(Kitchen Order Ticket) Management Software"
app_email = "info@tridz.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ury_mosaic/css/ury_mosaic.css"
# app_include_js = "/assets/ury_mosaic/js/ury_mosaic.js"
app_include_js = "/assets/ury_mosaic/js/ury_pos_kot.js"

# include js, css files in header of web template
# web_include_css = "/assets/ury_mosaic/css/ury_mosaic.css"
# web_include_js = "/assets/ury_mosaic/js/ury_mosaic.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ury_mosaic/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
page_js = {"point-of-sale" :["public/js/ury_poskot_extend.js"]}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ury_mosaic.utils.jinja_methods",
#	"filters": "ury_mosaic.utils.jinja_filters"
# }

fixtures = [
	{
		"doctype" : "Custom Field",
		"filters" : [
			[
				"name",
				"in",
					{
						"Printer Settings-kot_print_format_",
						"Printer Settings-kot",
						"POS Profile-kot_naming_series",
						"POS Profile-custom_kot_settings",
						"POS Profile-custom_kot_alert",
						"POS Profile-custom_kot_alert_sound",
						"POS Profile-custom_kot_warning_time",
						"POS Profile-custom_cl",
						"POS Profile-custom_notify_kot_delay",
						"POS Profile-custom_recipients",
                        "URY Printer Settings-custom_block_takeaway_kot"
					}
			]
		]
  
	}
]

# Installation
# ------------

# before_install = "ury_mosaic.install.before_install"
# after_install = "ury_mosaic.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ury_mosaic.uninstall.before_uninstall"
# after_uninstall = "ury_mosaic.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ury_mosaic.utils.before_app_install"
# after_app_install = "ury_mosaic.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ury_mosaic.utils.before_app_uninstall"
# after_app_uninstall = "ury_mosaic.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ury_mosaic.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    "cron":{
		"* * * * *":[
			"ury_mosaic.ury_mosaic.api.ury_kot_validation.kotValidationThread"
		]
	}
#	"all": [
#		"ury_mosaic.tasks.all"
#	],
#	"daily": [
#		"ury_mosaic.tasks.daily"
#	],
#	"hourly": [
#		"ury_mosaic.tasks.hourly"
#	],
#	"weekly": [
#		"ury_mosaic.tasks.weekly"
#	],
#	"monthly": [
#		"ury_mosaic.tasks.monthly"
#	],
}

# Testing
# -------

# before_tests = "ury_mosaic.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ury_mosaic.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ury_mosaic.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ury_mosaic.utils.before_request"]
# after_request = ["ury_mosaic.utils.after_request"]

# Job Events
# ----------
# before_job = ["ury_mosaic.utils.before_job"]
# after_job = ["ury_mosaic.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ury_mosaic.auth.validate"
# ]

website_route_rules = [{'from_route': '/URYMosaic/<path:app_path>', 'to_route': 'URYMosaic'},]