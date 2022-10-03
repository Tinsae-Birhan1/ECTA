// Copyright (c) 2022, Across Express and contributors
// For license information, please see license.txt

frappe.ui.form.on('Exporter', {
	// refresh: function(frm) {

	// }

	onload: function(frm){
		cur_frm.set_query("user", function () {
			return {
				query: "ecta_dispatch.ecta_dispatch.doctype.exporter.api.get_exporter"
			}
		});
	}
});
