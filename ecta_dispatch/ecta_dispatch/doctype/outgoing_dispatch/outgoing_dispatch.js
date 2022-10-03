// Copyright (c) 2022, Across Express and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ethiopian City', {
	refresh: function(frm) {

	},
  before_save: function(frm){
    console.log(frm);
    return false;
  }


});


function initMap() {
  const myLatlng = { lat: 9.009720495837291, lng: 38.76146451857262 };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    mapTypeControl: false,
    center: myLatlng,
  });
  document.getElementById("autocomplete").addEventListener("click",  Geocode(map));

  ////
  const geocoder = new google.maps.Geocoder();
  // Create the initial InfoWindow.
  let infoWindow = new google.maps.InfoWindow({
    content: "Click the map to get Lat/Lng!",
    position: myLatlng,
  });

  infoWindow.open(map);
  // Configure the click listener.
  map.addListener("click", (mapsMouseEvent) => {
    // Close the current InfoWindow.
    infoWindow.close();
    // Create a new InfoWindow.
    infoWindow = new google.maps.InfoWindow({
      position: mapsMouseEvent.latLng,
    });
    infoWindow.setContent(
      JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
    );
    //document.getElementById("lat").value = mapMouseEvent.latLng.toJSON()
    infoWindow.open(map);
    console.log(mapsMouseEvent);
    const el = JSON.parse(JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2));
    document.querySelector("input[data-fieldname='latitude']").value =el.lat;
    document.querySelector("input[data-fieldname='longitude']").value = el.lng;
    geocodeLatLng(geocoder, map, infoWindow,el);
  });   
}

frappe.ui.form.on('Outgoing Dispatch', {
	refresh(frm) {
		// your code here

    $('input[data-fieldname="destination"]').attr("id","autocomplete");

    initMap()
	}
});

function geocodeLatLng(geocoder, map, infowindow,el) {
  geocoder
    .geocode({ location: el })
    .then((response) => {
 
      if (response.results[0]) {
        const marker = new google.maps.Marker({
          position: el,
          map: map,
        });
        console.log(response.results[0].formatted_address)
        document.querySelector("input[data-fieldname='city']").value =response.results[0].formatted_address;
        map.panTo(marker.position);
        infowindow.setContent(response.results[0].formatted_address);
        infowindow.open(map, marker);
      } else {
        window.alert("No results found");
      }
    })
    .catch((e) => window.alert("Geocoder failed due to: " + e));
}

function Geocode(map) {
    var autocomplete = new google.maps.places.Autocomplete(document.getElementById('autocomplete'));
    autocomplete.setFields(['place_id', 'name', 'address_components', 'geometry', 'formatted_address','address_components','adr_address']);
    autocomplete.setComponentRestrictions({
      country: ["et"],
    });
    autocomplete.addListener('place_changed', function () {
        const place = autocomplete.getPlace();
    
        $("input[data-fieldname='destination']").val(place.name);
        cur_frm.doc.destination = place.name;
    });
}

