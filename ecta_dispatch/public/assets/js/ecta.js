


  warehouseECTA = "";
   
  [...document.getElementsByClassName("dispatchlinks")].forEach(function(item){
    item.addEventListener("click", function() {
      warehouseECTA = $(this).data('id');
      console.log(warehouseECTA);
      
      let call = async()=>{       
        if(true){
            let result = await $.ajax({
              
                  url: `/api/resource/ECTA Dispatches/${warehouseECTA}?fields=['volume_in_bag','volume_in_ton','received_volume_in_bag','received_volume_in_ton']`,
                  type: 'GET',
                
                headers: {
                    'Content-Type': 'application/json',
                    'X-Frappe-CSRF-Token': frappe.csrf_token
                },
                
                success: function(data){
                    return data
                },
                error: function(data){
                    return data
                }
            });
            console.log(result['data']['creation']);
            volume_in_bag = result['data']['volume_in_bag'];
            volume_in_ton = result['data']['volume_in_ton'];
            received_volume_in_bag = result['data']['received_volume_in_bag'];
            received_volume_in_ton = result['data']['received_volume_in_ton'];
            document.getElementById("VBD").value = volume_in_bag;
            document.getElementById("VTD").value = volume_in_ton;
            document.getElementById("VBW").value = received_volume_in_bag;
            document.getElementById("VTW").value = received_volume_in_ton;
            
      }
      }
      call();

        
    })
  });

  $("#customCheck2").change(function() {
    console.log("i am changed");
    if ($(this).is(':checked') ) {
       approve = 1;
    } else {
      approve = 0;
    }
  }).trigger("change");
  
var compareform = document.forms['compareform'];
compareform.onsubmit = function(e){

  e.preventDefault();
  let call = async()=>{       
    if(true){
        let result = await $.ajax({
          
              url: `/api/resource/ECTA Dispatches/${warehouseECTA}`,
              type: 'PUT',
            
            headers: {
                'Content-Type': 'application/json',
                'X-Frappe-CSRF-Token': frappe.csrf_token
            },
            data: JSON.stringify({status:"Seen",approved:approve}),
            success: function(data){
                return data
            },
            error: function(data){
                return data
            }
        });
        console.log(result);
       
        
  }
  }
  
  call();
  alert("hello");
  document.location.reload(true);
}
  
