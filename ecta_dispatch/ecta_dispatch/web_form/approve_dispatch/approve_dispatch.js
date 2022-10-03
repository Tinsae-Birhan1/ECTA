frappe.ready(function () {
	console.log("test");

	frappe.web_form.after_save = () => {
		window.location.href = "/ecta";
	}
	frappe.web_form.after_load = () => {
		$('input[data-fieldname="destination"]').attr("id", "autocomplete");

		initMap();
	}
	// frappe.web_form.after_load = () => {
	// 	console.log("test");
	// 	// alert(frappe.web_form.get_value("received_volume_in_ton"));
	// 	// console.log(frappe.web_form.get_value("received_volume_in_ton"));
	// 	// frappe.web_form.set_value("received_volume_in_ton", frappe.web_form.get_value("received_volume_in_ton")*1000);
	// }
})