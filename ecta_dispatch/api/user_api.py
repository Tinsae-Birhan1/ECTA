import frappe
from frappe.utils.data import pretty_date

@frappe.whitelist()
def create_user():
    exporter = frappe.db.get_list("Exporter", filters={'user':frappe.session.user}, fields=['name'])
    frappe.errprint(exporter)
    if len(exporter)>0:
        user = frappe.new_doc("User")
        form_data = frappe.parse_json(frappe.form_dict)
        frappe.errprint(form_data)
        user.first_name = form_data.firstname
        user.last_name = form_data.lastname
        user.gender = form_data.sex
        user.email = form_data.email
        user.phone = form_data.phone
        user.insert()
        frappe.db.commit()

        if form_data.job_type:
            exp_employee = frappe.new_doc("Exporter Employee")
            exp_employee.exporter = exporter[0].name 
            exp_employee.employee = user.name
            exp_employee.job_type = frappe.form_dict.job_type
            exp_employee.insert()
            frappe.db.commit()
    else:
        return {"message" : "Exporter Not Found. Please contact Administrator"}
    # return user

@frappe.whitelist()
def update_user():
    exporter = frappe.db.get_list("Exporter", filters={'user':frappe.session.user}, fields=['name'])
    form_data = frappe.parse_json(frappe.form_dict)

    if len(exporter)>0:
        exp_employee = frappe.get_doc("Exporter Employee", form_data.name)
        if exp_employee:
            user = frappe.get_doc("User", exp_employee.employee)
            user.first_name = form_data.firstname
            user.last_name = form_data.lastname
            user.gender = form_data.sex
            user.email = form_data.email
            user.phone = form_data.phone
            user.save()
            frappe.db.commit()

        if form_data.job_type:
            exp_employee.job_type = frappe.form_dict.job_type
            exp_employee.save()
            frappe.db.commit()
        return {"message": "Data updated Successfully"}
    else:
        return {"message" : "Exporter Not Found. Please contact Administrator"}
    # return user




@frappe.whitelist()
def get_employees_data( *args, **kwargs):
    frappe.response["draw"] = frappe.form_dict.draw

    employee_list = []

    ####  get exporter information
    exporter = frappe.db.get_list("Exporter", filters={'user':frappe.session.user}, fields=['name'])
    
    ####  filter
    if len(exporter)>0: 
        search_dictionary = {
            "exporter": exporter[0].name,
            'name': "%"+frappe.form_dict['search[value]']+"%",
        }
    #### end filter


    #### fetch employee data

        employee_list = frappe.db.sql("""
            SELECT first_name, last_name, email, phone, job_type, user.creation, exp_emp.name, user.modified
            FROM `tabExporter Employee` exp_emp
            JOIN `tabUser` user
            on exp_emp.employee = user.name
            WHERE exporter=%(exporter)s and first_name like %(name)s
            order by first_name
        """, values=search_dictionary, as_dict=0)
        
    #### end fetch data


    #### values to be displayed in the tables

    i = int(frappe.form_dict["start"])+1
    arranged_list_value = []
    arranged_list = []
    
    if len(employee_list)>0:
        for employee in employee_list:
            arranged_list.append(i)
            arranged_list.append(employee[0]+" "+employee[1])
            arranged_list.append(employee[2])
            arranged_list.append(employee[3])
            arranged_list.append(employee[4])
            arranged_list.append(pretty_date(employee[5]))
            arranged_list.append(pretty_date(employee[7]))
            arranged_list.append("<a href='/exporter/employee/edit/"+employee[6] +"'>Edit</a> ")
            
            arranged_list_value.append(arranged_list)
            arranged_list=[]
            i = i+1
        
        #### end of values to be displayed in the tables

    frappe.response["data"] = arranged_list_value
    frappe.response["recordsTotal"] = len(arranged_list_value)
    frappe.response["recordsFiltered"] = len(arranged_list_value)

