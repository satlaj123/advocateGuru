$(function() {
	$("#registration").validate({

		rules: {

			first_name: "required",
			last_name: "required",
			mobile: "required",
			dob: "required",
			adhar_number: {
				required: true,
				maxlength: 12,
				minlength: 12,
				charCode: false,
			},
			address: "required",
			pincode: {
				required: true,
				maxlength: 6,
				minlength: 6,
			},
			// email: "required",
			password: "required",
			// cpassword: "required",

			mobile_number: {
				required: true,
				maxlength: 10,
				minlength : 10,
			},
			password: {
				required: true,
				maxlength: 8,
				minlength: 8,
			},
			cpassword: {
				required: true,
				equalTo: "#password",


			},

			// email: {
				
			// 	required: true,

			// },
		},

		message: {

			name: "Please enter your name!",
			dob: "Please enter your date of birth!",
		// 	email: {
		// 	  email: "Please enter a valid email adress!",
		// },
		mobile_number: {
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
			equalTo: "password must be same!!",
		},
		adhar_number: {
			required: "Please enter the adhar number!!",
			maxlength: "Please enter the 12-digits!!",
			minlength: "Please enter the 12-digits!!",
			charCode: "Only integer is valid!!",

		},
		address: "Please enter the address!!",
		pincode: {
			required: "Please enter the pincode!!",
			maxlength: "Please enter the 6-digits!!",
			minlength: "Please enter the 6-digits!!",
		},

	




},
});
});