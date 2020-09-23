const user_input = $("#user-input")
const user_input2 = $("#user-input2")
const divv = $('#replaceable-content')
const div2 = $('#replaceable-content2')
const endpoint = '/sample1/'
const endpoint2 = '/sample2/'
const delay_by_in_ms = 400
let scheduled_function = false
// var divv =  document.getElementByClass("activez")

let ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			divv.fadeTo('fast', 0).promise().then(() => {
				divv.html(response['html_from_view'])
				
				divv.fadeTo('fast', 1)	
			})
		})
}

let ajax_call2 = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			div2.fadeTo('fast', 0).promise().then(() => {
				div2.html(response['html_from_view2'])
				
				div2.fadeTo('fast', 1)	
			})
		})
}

user_input.on('keyup', function () {
	const request_parameters = {
		q: $(this).val()
	}
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})

user_input2.on('keyup', function () {
	const request_parameters = {
		q: $(this).val()
	}
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}
	scheduled_function = setTimeout(ajax_call2, delay_by_in_ms, endpoint2, request_parameters)
})
