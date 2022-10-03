var warehouseName = "";
$("#dispatchStatus").change(function() {
  if ($(this).val() == "Undelivered") {
    $(".formInputs").attr("disabled", "disabled");
  } else {
    $(".formInputs").removeAttr("disabled");
  }
}).trigger("change");

[...document.getElementsByClassName("dispatchName")].forEach(function(item){
    item.addEventListener("click", function() {
        warehouseName = $(this).data('id');
        console.log(warehouseName);
    })
  });

var dispatchForm = document.forms['dispatchForm'];
dispatchForm.onsubmit = function(e){
  e.preventDefault();	


// upload method
let makecall = async()=>{
    let formdata = $('#dispatchForm').serializeArray().reduce(
        (obj, item)=>(obj[item.name]=item.value, obj), {}
    );
    console.log(formdata.type,formdata);
    alert("hello");
    formdata["id"]= warehouseName;
    let filedata = $('#file')[0].files[0];
    // initialize form
    let file = new FormData()
    if(filedata){
        file.append('file', filedata);
    }
    // end initialize

    // post to API
    if(formdata){
        let res = await $.ajax({
            url: `/api/resource/ECTA Dispatches/${warehouseName}`,
            type: 'PUT',
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
        if(res.data && filedata){
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
                        url: `/api/resource/ECTA Dispatches/${warehouseName}`,
                        type: 'PUT',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-Frappe-CSRF-Token': frappe.csrf_token
                        },
                        data: JSON.stringify({proof_of_delivery:data.message.file_url}),
                        success: function(data){
                            console.log(data);
                            alert("Dispatch Recieve success!!!");
                            document.location.reload(true);
                            return data
                            
                        },
                        error: function(data){
                            return data
                        }
                    })

                    // end update agent
                }
            })
        }else{
            alert("Update successful!");
            document.location.reload(true);
        }
        
    }

  }
  makecall();
}








// var dispatchForm = document.forms['dispatchForm'];
// dispatchForm.onsubmit = function(e){
//   e.preventDefault();	

//   var select = document.getElementById('dispatchStatus');
//   select_value = select.options[select.selectedIndex].value;
//   var VolumeInTon = document.getElementById('VInTon').value;
//   var VolumeInBag = document.getElementById('VInBag').value;
//   formDictionary = {"warehouseName":warehouseName ,"status":select_value,"volumeInBag":VolumeInBag,"volumeInTon":VolumeInTon}
//   let makecall = async()=>{
//         // post to API
//                 res = await $.ajax({
//                 url: '/api/method/ecta_dispatch.api.dispatch_accept_api.dispatchAcceptanceForm',
//                 method: 'POST',
//                 data:formDictionary,
//                 headers: {
//                     'X-Frappe-CSRF-Token': frappe.csrf_token
//                 },
//             });
//             var message = res.message
            
//             alert(message);
//             document.location.reload(true);
            
//         }	
//     makecall();	

// }
// // document.getElementById("dispatchForm").addEventListener("submit", function(e){
   
    

// // let makecall = async()=>{
// //     // post to API
    
// //         res = await $.ajax({
// //             url: '/api/method/employee.api.dispatch_accept_api.dispatchAcceptanceForm',
// //             method: 'POST',
// //             headers: {
// //                 'X-Frappe-CSRF-Token': frappe.csrf_token
// //             },
// //         });
// //         var message = res.message
        
// //         alert(message);
// //         document.location.reload(true);
        
// //     }	
// // makecall();	
// });
