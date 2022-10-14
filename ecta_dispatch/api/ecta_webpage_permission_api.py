
import frappe

def checkPermisson(page):
  roles = ((frappe.get_doc('Ecta roles for page',page )).as_dict())['roles'] 
  role_list = []
  for role in roles:
    role_list.append(role['role'])
  if any(item in role_list for item in frappe.get_roles(frappe.session.user) ):
    print("found the role in api")
    return True
   
  else:
    frappe.local.flags.redirect_location = "/app"
    raise frappe.Redirect
  