frappe.ready(function () {
	frappe.web_form.after_save = () => {
		window.location.href = "/warehouse";
	}

	// frappe.web_form.after_load = () => {
	// 	frappe.web_form.set_value("received_volume_in_ton", frappe.web_form.get_value("received_volume_in_ton")*1000);
	// }
})