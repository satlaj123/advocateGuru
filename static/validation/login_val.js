$(function() {
	$("#login").validate({

		rules: {

			name: "required",
			dob: "required",
			mobile: "required",
			Email: "required",
			password: "required",
			cpassword: "required",

			mobile: {
				required: true,
				maxlength: 10,
				minlength : 10,
			},
			password: {
				required: true,
				maxlength: 8,
				minlength: 5,
			},
			cpassword: {
				required: true,
				equalTo: "#password",


			},

			email: {
				required: false,
				required: true,

			},
		},

		message: {

			name: "Please enter your name!",
			dob: "Please enter your date of birth!",
			email: {
			  email: "Please enter a valid email adress!",
		},
		mobile: {
			required: "Please enter a phone number!",
			maxlength: "Please enter a valid phone number!",
			minlength: "Please enter a valid phone number!",
		},
		password: {
			required: "Please Provide a password!",
			minlength: "Your password must be at least 5 character!",
		},
		cpassword: {
			required: "Please confirm your password!",
			equalTo: "password must be same",
		},

	




},
});
});