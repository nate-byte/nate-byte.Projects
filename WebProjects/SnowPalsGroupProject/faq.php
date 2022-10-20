<!DOCTYPE html>
<html lang="en">

<head>
	<title>Snow Pals</title>
	<meta charset="UTF-8">
	<meta name="Project Group 11" content="Frequently Asked Questions">
	<link rel="icon" type="image/x-icon" href="img/favicon.ico">
	<link rel="stylesheet" href="css/faq.css">
</head>

<body>
	<?php include 'nav.php'; ?>

	<div class="content">
		<h3>Frequently Asked Questions</h3>
	</div>

	<p class="question">Where can I find the activities offered?</p>
	<div class="answer">
		<p>Our current activities can be found by clicking on <i>Featured Activities</i> in the navigation bar.</p>
	</div>

	<p class="question">Where can I find your participating locations?</p>
	<div class="answer">
		<p>Our current locations can be found by clicking on <i>Available Locations</i> in the navigation bar.</p>
	</div>

	<p class="question">Do you have any advice for meeting up?</p>
	<div class="answer">
		<p>Our safety tips can be found under <i>Safety Information</i> in the navigation bar.</p>
	</div>

	<p class="question">How does matching work?</p>
	<div class="answer">
		<p>You enter the activities you're interested in, your location, and other personal information.<br>
			After creating an account, you will be paired with people who shared the same locations and interests.</p>
	</div>

	<p class="question">How do I sign up?</p>
	<div class="answer">
		<p>Click the <i>Sign Up</i> button in the right hand corner.</p>
	</div>

	<p class="question">What happens if I find a match I'm interested in?</p>
	<div class="answer">
		<p>You can message them using the messaging feature after logging in.</p>
	</div>

	<script>
		var num = document.getElementsByClassName("question");
		var i;

		for (i = 0; i < num.length; i++) {
			num[i].addEventListener("click", function() {
				this.classList.toggle("active");

				var answer = this.nextElementSibling;
				if (answer.style.display === "block") {
					answer.style.display = "none"
				} else {
					answer.style.display = "block"
				}
			});
		}
	</script>

	<div class="footer">
		© 2021 Snow Pals
	</div>
</body>

</html>