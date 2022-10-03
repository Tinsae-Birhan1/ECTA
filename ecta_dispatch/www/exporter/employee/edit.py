import frappe
from frappe.exceptions import DoesNotExistError
from frappe.utils.data import pretty_date

def get_context(context):
  context.show_sidebar = 1
  context.csrf_token = frappe.sessions.get_csrf_token()
  context.user = {}


  try:
    get_employee = frappe.get_doc("Exporter Employee", frappe.form_dict.employee)
    user = frappe.get_doc("User", get_employee.employee)
  
    exporter = frappe.db.get_list("Exporter", filters={'user':frappe.session.user}, fields=['exporter_name'])

    if len(exporter)>0: 
      if exporter[0]['exporter_name'].strip() == get_employee.exporter.strip():
        context.first_name = user.first_name
        context.last_name = user.last_name
        context.gender = user.gender
        context.phone = user.phone
        context.email = user.email
        context.job_type = get_employee.job_type
        context.name = get_employee.name
      else:
        frappe.flags.redirect_location = "/exporter/employee"
        raise frappe.Redirect
    else:
      frappe.flags.redirect_location = "/exporter/employee"
      raise frappe.Redirect

  except frappe.DoesNotExistError:
    frappe.flags.redirect_location = "/exporter/employee"
    raise frappe.Redirect



  exporter_employee_meta_data = frappe.get_meta("Exporter Employee")
  job_type_options = exporter_employee_meta_data.get_field("job_type")
  context.options = job_type_options.options.split("\n")
