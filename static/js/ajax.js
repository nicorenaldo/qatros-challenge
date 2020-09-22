const user_input = $("#user-input")
const div = $('#replaceable-content')
const endpoint = '/'
const delay_by_in_ms = 400
let scheduled_function = false
// var divv =  document.getElementByClass("activez")

let ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			div.fadeTo('fast', 0).promise().then(() => {
				// replace the HTML contents
				div.html(response['html_from_view'])
				
				// fade-in the div with new contents
				div.fadeTo('fast', 1)
				
			})
			
		})
	
}


user_input.on('keyup', function () {

	const request_parameters = {
		q: $(this).val() // value of user_input: the HTML element with ID user-input
	}

	// start animating the search icon with the CSS class
	

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
