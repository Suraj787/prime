# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_prime"
app_title = "Prime"
app_publisher = "Techlift.in"
app_description = "Prime"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "suraj@techlift.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_prime/css/erpnext_prime.css"
# app_include_js = "/assets/erpnext_prime/js/erpnext_prime.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_prime/css/erpnext_prime.css"
# web_include_js = "/assets/erpnext_prime/js/erpnext_prime.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

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

# Website user home page (by function)
# get_website_user_home_page = "erpnext_prime.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_prime.install.before_install"
# after_install = "erpnext_prime.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_prime.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
	
	"Sales Invoice": {
		"after_insert": "erpnext_prime.sales_invoice_sms.sales_invoice_sms.custoemr_sms"
	}	
		
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_prime.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_prime.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_prime.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_prime.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_prime.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_prime.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_prime.event.get_events"
# }

