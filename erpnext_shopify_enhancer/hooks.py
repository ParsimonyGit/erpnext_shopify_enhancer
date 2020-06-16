# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_shopify_enhancer"
app_title = "Erpnext Shopify Enhancer"
app_publisher = "GreyCube Technologies"
app_description = "Customize shopify data to suite erpnext. ex. truncate item_name to 140 char"
app_icon = "octicon octicon-plug"
app_color = "red"
app_email = "admin@greycube.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_shopify_enhancer/css/erpnext_shopify_enhancer.css"
# app_include_js = "/assets/erpnext_shopify_enhancer/js/erpnext_shopify_enhancer.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_shopify_enhancer/css/erpnext_shopify_enhancer.css"
# web_include_js = "/assets/erpnext_shopify_enhancer/js/erpnext_shopify_enhancer.js"

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
# get_website_user_home_page = "erpnext_shopify_enhancer.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_shopify_enhancer.install.before_install"
# after_install = "erpnext_shopify_enhancer.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_shopify_enhancer.notifications.get_notification_config"

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

doc_events = {
	"Item": {
		"before_insert": "erpnext_shopify_enhancer.item.truncate_item_name_from_shopify",
	},
	"Sales Order": {
		"before_insert": "erpnext_shopify_enhancer.item.truncate_item_name_from_shopify_for_SO",
	}	
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erpnext_shopify_enhancer.tasks.all"
# 	],
# 	"daily": [
# 		"erpnext_shopify_enhancer.tasks.daily"
# 	],
# 	"hourly": [
# 		"erpnext_shopify_enhancer.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erpnext_shopify_enhancer.tasks.weekly"
# 	]
# 	"monthly": [
# 		"erpnext_shopify_enhancer.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "erpnext_shopify_enhancer.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_shopify_enhancer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erpnext_shopify_enhancer.task.get_dashboard_data"
# }

