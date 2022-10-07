
warehouse = ""
let makecall = async()=>{
     let res = await $.ajax({
         url: `/api/resource/ECTA Approved Warehouses`,
         type:'GET',
         headers: {
             'Content-Type': 'application/json',
             'X-Frappe-CSRF-Token': frappe.csrf_token
         },
         data: [{warehouse_owner:frappe.session.user}],
         success: function(data){
             return data
         },
         error: function(data){
             return data
         }
     })
     warehouse = res['data'][0]['name'];
    }
makecall();

var newOutgoingForm = document.forms['newOutgoingForm'];
console.log(newOutgoingForm);
newOutgoingForm.onsubmit = function(e){
   
  e.preventDefault();	


// upload method
let makecall = async()=>{
    let formdata = $('#newOutgoingForm').serializeArray().reduce(
        (obj, item)=>(obj[item.name]=item.value, obj), {}
    );
    console.log(formdata.type,formdata);
   
    
    let voucher = $('#warehouseVoucher')[0].files[0];
  
    let otherFile =$('#other')[0].files[0];

    let picture =$('#picture')[0].files[0];
   
    // initialize form
    let file1 = new FormData()
    let file2 = new FormData()
    let file3 = new FormData()
    if(voucher){
        file1.append('file', voucher);
    }
    if(otherFile){
     file2.append('file', otherFile);
    }
    if(picture){
        file3.append('file', picture);
    }
    // end initialize

    // post to API
    if(formdata){
        let res = await $.ajax({
            url: `/api/resource/Outgoing Dispatch`,
            type:'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Frappe-CSRF-Token': frappe.csrf_token
            },
            data: JSON.stringify(formdata),
            success: function(data){
                return data
            },
            error: function(data){
                return data
            }
        })
        console.log(res);
        // upload image
        if(res.data && voucher){
            field = "Warehouse_outgoing_voucher";
            uploadFile1(file1,res);   
        }
        else{
            lert("New Outgoing Dispatch creation successful!");
            document.location.reload(true);
        }
        if(res.data && otherFile){
            field = "other";
            uploadFile2(file2,res);
        }
        else{
            alert("New Outgoing Dispatch creation successful!");
            document.location.reload(true);
        }
        
        if(res.data && picture){
            field = "picture";
            uploadFile3(file3,res);
        }
        else{
            lert("New Outgoing Dispatch creation successful!");
            document.location.reload(true);
        }
        alert("New Outgoing Dispatch creation successful!");
        document.location.reload(true);

    }
        
    }
    makecall();

function uploadFile1(file,res){
    outDispatchName =res["data"]["name"];
    let makecall = async()=>{
    let fileres = await fetch('/api/method/upload_file', {
        headers: {
            'X-Frappe-CSRF-Token': frappe.csrf_token
        },
        method: 'POST',
        body: file
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data);
        
        // finally update document
        if(data.message){
            // update agent
            $.ajax({
                url: `/api/resource/Outgoing Dispatch/${outDispatchName}`,
                type: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Frappe-CSRF-Token': frappe.csrf_token
                },
                data: JSON.stringify({warehouse_outgoing_voucher:data.message.file_url}),
                success: function(data){
                    console.log(data);
                    return data
                    
                },
                error: function(data){
                    console.log(data);
                    return data
                    
                }
            })

            // end update agent
        }
    })
    
}
makecall();

}
function uploadFile2(file,res){
    outDispatchName =res["data"]["name"];
    let makecall = async()=>{
    let fileres = await fetch('/api/method/upload_file', {
        headers: {
            'X-Frappe-CSRF-Token': frappe.csrf_token
        },
        method: 'POST',
        body: file
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data);
        // finally update document
        if(data.message){
            // update agent
            $.ajax({
                url: `/api/resource/Outgoing Dispatch/${outDispatchName}`,
                type: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Frappe-CSRF-Token': frappe.csrf_token
                },
                data: JSON.stringify({other:data.message.file_url}),
                success: function(data){
                    console.log(data);
                    return data
                    
                },
                error: function(data){
                    console.log(data);
                    return data
                    
                }
            })
            alert("other returned");
            // end update agent
        }
    })
    
}
makecall();

}
function uploadFile3(file,res){
    outDispatchName =res["data"]["name"];
    let makecall = async()=>{
    let fileres = await fetch('/api/method/upload_file', {
        headers: {
            'X-Frappe-CSRF-Token': frappe.csrf_token
        },
        method: 'POST',
        body: file
    })
    .then(res=>res.json())
    .then(data=>{
        console.log(data);
        // finally update document
        if(data.message){
            // update agent
            $.ajax({
                url: `/api/resource/Outgoing Dispatch/${outDispatchName}`,
                type: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Frappe-CSRF-Token': frappe.csrf_token
                },
                data: JSON.stringify({picture:data.message.file_url}),
                success: function(data){
                    console.log(data);
                    return data
                    
                },
                error: function(data){
                    console.log(data);
                    return data
                    
                }
            })

            // end update agent
        }
    })
    
}
makecall();

}
}
