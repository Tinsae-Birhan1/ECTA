from . import __version__ as app_version
from ecta_dispatch.routes import routes

app_name = "ecta_dispatch"
app_title = "Ecta Dispatch"
app_publisher = "Across Express"
app_description = "module to control ecta dispatches"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "acrossexpressplc@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/ecta_dispatch/css/ecta_dispatch.css"
# app_include_js = "/assets/ecta_dispatch/js/ecta_dispatch.js"

# include js, css files in header of web template
web_include_css = "/assets/ecta_dispatch/css/ecta_dispatch.css"
# web_include_js = "/assets/ecta_dispatch/js/ecta_dispatch.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ecta_dispatch/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

website_context = {
	"favicon": "/assets/ecta_dispatch/images/ecta-log.png",
	"splash_image": "/assets/ecta_dispatch/images/ecta-log.png"
}

app_logo_url = "/assets/ecta_dispatch/images/ecta-log.png"

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]


app_include_js = [
	# "https://maps.googleapis.com/maps/api/js?key=AIzaSyDbpZlnMqg3yXl6tPhQzz2OoKA7GuRAYMY&libraries=places",
]

website_route_rules = routes

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ecta_dispatch.utils.jinja_methods",
# 	"filters": "ecta_dispatch.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ecta_dispatch.install.before_install"
# after_install = "ecta_dispatch.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ecta_dispatch.uninstall.before_uninstall"
# after_uninstall = "ecta_dispatch.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ecta_dispatch.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ecta_dispatch.tasks.all"
# 	],
# 	"daily": [
# 		"ecta_dispatch.tasks.daily"
# 	],
# 	"hourly": [
# 		"ecta_dispatch.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ecta_dispatch.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ecta_dispatch.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ecta_dispatch.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ecta_dispatch.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ecta_dispatch.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ecta_dispatch.auth.validate"
# ]

