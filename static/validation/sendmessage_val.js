$(function() {
	$("#contactform").validate({
		rules: {
			name: "required",
			email: "required",
			subject: "required",
			message: "required",
		},

	// message at validation error
	messages: {
		name: "Please enter your name!!",
		email: {
			  email: "Please enter a valid email!!",
		},
		subject: "Please enter the your subject!!",
		message: "Please enter the message!!",
	},

	});
});