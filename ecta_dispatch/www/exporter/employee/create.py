import frappe

def get_context(context):
  context.show_sidebar = 1
  context.csrf_token = frappe.sessions.get_csrf_token()
  exporter_employee_meta_data = frappe.get_meta("Exporter Employee")
  job_type_options = exporter_employee_meta_data.get_field("job_type")
  context.options = job_type_options.options.split("\n")
