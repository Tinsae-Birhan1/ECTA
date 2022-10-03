// Copyright (c) 2022, Across Express and contributors
// For license information, please see license.txt

frappe.ui.form.on('ECTA Approved Warehouses', {
    onload: function (frm) {
        frm.set_query("warehouse_owner", function () {
            return {
                query: "ecta_dispatch.ecta_dispatch.doctype.ecta_approved_warehouses.api.get_owner"
            }
        });

        frm.set_query("warehouse_operator", function () {
            return {
                query: "ecta_dispatch.ecta_dispatch.doctype.ecta_approved_warehouses.api.get_operator"
            }
        });
    }
});


