frappe.ready(function() {
	frappe.web_form.after_save = () => {
		window.location.href = "/ectaoutgoing";
	  }

	frappe.web_form.after_load = () => {
	//   frappe.web_form.validate = () => {
		frappe.web_form.set_value(["approved_by"], frappe.session.user)
		frappe.web_form.set_value(["date_of_approval"], current_date())
	// }
	}
})

function current_date()
{
	var today = new Date();
	var dd = String(today.getDate()).padStart(2, '0');
	var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
	var yyyy = today.getFullYear();


	var hh = today.getHours(); 
	var m = today.getMinutes();
	var ss = today.getSeconds();

	today = dd+"-"+mm+"-"+yyyy+" "+hh+":"+m+":"+ss;
	return today;	
}