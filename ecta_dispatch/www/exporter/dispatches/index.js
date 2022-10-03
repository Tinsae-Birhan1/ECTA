$("body").on("click", ".accept", function(e){
    e.preventDefault();

    console.log("test");
    let d = new frappe.ui.Dialog({
        title: 'Enter details',
        fields: [
            {
                label: 'First Name',
                fieldname: 'first_name',
                fieldtype: 'Data'
            },
            {
                label: 'Last Name',
                fieldname: 'last_name',
                fieldtype: 'Data'
            },
            {
                label: 'Age',
                fieldname: 'age',
                fieldtype: 'Int'
            }
        ],
        primary_action_label: 'Submit',
        primary_action(values) {
            console.log(values);
            d.hide();
        }
    });
    
    d.show();
});
