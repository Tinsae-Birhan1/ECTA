var interval = "";
function initMap() {
		console.log("map loaded");
		console.log(document.getElementById("map"));
		const myLatlng = { lat: 9.009720495837291, lng: 38.76146451857262 };
		const map = new google.maps.Map(document.getElementById("map"), {
			zoom: 13,
			mapTypeControl: false,
			center: myLatlng,
		});
		clearInterval(interval);
		document.getElementById("autocomplete").addEventListener("click", Geocode(map));
	}

	function Geocode(map) {
		var autocomplete = new google.maps.places.Autocomplete(document.getElementById('autocomplete'));
		autocomplete.setFields(['place_id', 'name', 'address_components', 'geometry', 'formatted_address', 'address_components', 'adr_address']);
		// autocomplete.setComponentRestrictions({
		// 	country: ["et", "dj", "er", "ke", "so", "sd"],
		// });
		autocomplete.addListener('place_changed', function () {
			const place = autocomplete.getPlace();
			var formattted_address = place.formatted_address.split(",");
			var address_components = place.address_components;
			// var country = formattted_address.pop();

			// const lat = place.geometry.location.lat();
			// const lng = place.geometry.location.lng();

			// document.querySelector("input[data-fieldname='location']").value = place.formatted_address;

			$('input[data-fieldname="destination"]').val(place.formatted_address);
			// console.log(cur_frm.doc.location);
		});
	}

frappe.ready(function () {
	frappe.web_form.after_save = () => {
		window.location.href = "/outgoings";
	  }

	frappe.web_form.after_load = () => {

		value = frappe.web_form.get_value(["dispatch_approval"]);
		if(value)
		{
			window.location.href = "/outgoings";
		}

		$('input[data-fieldname="destination"]').attr("id", "autocomplete");

		var s = document.createElement("script");
		s.type = "text/javascript";
		s.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyDbpZlnMqg3yXl6tPhQzz2OoKA7GuRAYMY&libraries=places";
		$('body').append(s);

		interval = window.setInterval(function(){
			initMap();
		}, 2000);
	}
})

// // // Copyright (c) 2022, Across Express and contributors
// // // For license information, please see license.txt
