const user_input = $("#user-input")
// const user_input2 = $("#user-input2")
const div = $('#replaceable-content')
// const div2 = $('#replaceable-content2')
const endpoint = '/'
const delay_by_in_ms = 400
let scheduled_function = false
// var divv =  document.getElementByClass("activez")

let ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			div.fadeTo('fast', 0).promise().then(() => {
				div.html(response['html_from_view'])
				
				div.fadeTo('fast', 1)	
			})
		})
}

user_input.on('keyup', function () {

	const request_parameters = {
		q: $(this).val() // value of user_input: the HTML element with ID user-input
	}

	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
