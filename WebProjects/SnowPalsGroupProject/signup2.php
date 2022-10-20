<!DOCTYPE html>
<html lang="en">

<head>
	<title>Snow Pals Sign Up</title>
	<meta charset="UTF-8">
	<meta name="Project Group 11" content="dummy_signup2">
	<link rel="icon" type="image/x-icon" href="img/favicon.ico">
	<link rel="stylesheet" href="css/main-style.css">
	<link rel="stylesheet" href="css/user_inf.css">
	<script type="text/javascript" src="./verification.js" defer></script>
</head>
<?php include 'nav.php'; ?>

<body>

	<form action="registration2.php" method="post">
		<div class="user_inf">

			<h3>Areas of Interest:</h3>

			<label for="interest1">Skiing<input type="checkbox" id="activities[]" name="activities[]" value="Skiing"></label><br>

			<label for="interest2">Snowboarding<input type="checkbox" id="activities[]" name="activities[]" value="Snowboarding"></label><br>

			<label for="interest">Snowmobiling<input type="checkbox" id="activities[]" name="activities[]" value="Snowmobiling"></label><br>

			<label for="interest2">Snowbiking<input type="checkbox" id="activities[]" name="activities[]" value="Snowbiking"></label><br>

			<label for="interest1">Snowshoeing<input type="checkbox" id="activities[]" name="activities[]" value="Snowshoeing"></label><br>

			<label for="interest2">Sledding<input type="checkbox" id="activities[]" name="activities[]" value="Sledding"></label><br>

			<label for="interest1">Tubing<input type="checkbox" id="activities[]" name="activities[]" value="Tubing"></label><br>

			<label for="interest2">Specialized Skiing<input type="checkbox" id="activities[]" name="activities[]" value="Specialized Skiing"></label><br>

			<label for="interest1">Snow Kiting<input type="checkbox" id="activities[]" name="activities[]" value="Snow kiting"></label><br>

			<label for="interest2">Specialized Fishing<input type="checkbox" id="activities[]" name="activities[]" value="Specialized Fishing"></label><br>

			<label for="interest1">Snowcat Tours<input type="checkbox" id="activities[]" name="activities[]" value="Snowcat"></label><br>
		</div>

		<div class="user_inf" id="right">

			<h3>Accessible Locations:</h3>


			<label for="location2">Breckenridge<input type="checkbox" id="locations[]" name="locations[]" value="Breckenridge"></label><br>

			<label for="location3">Copper<input type="checkbox" id="locations[]" name="locations[]" value="Copper"></label><br>

			<label for="location4">Keystone<input type="checkbox" id="locations[]" name="locations[]" value="Keystone"></label><br>

			<label for="location5">Park City<input type="checkbox" id="locations[]" name="locations[]" value="Park_City"></label><br>

			<label for="location6">Snowbird<input type="checkbox" id="locations[]" name="locations[]" value="Snowbird"></label><br>

			<br>
			<br>

			<h3>Skill Level:</h3>

			Beginner <input type="radio" value="beginner" name="skill"><br>
			Intermediate <input type="radio" value="intermediate" name="skill"><br>
			Advanced <input type="radio" value="advanced" name="skill"><br>
			Expert <input type="radio" value="expert" name="skill">
		</div>

		<br>

		<div class="button">
			<input type="submit" value="Register">
		</div>

	</form>

	<div class="footer">
		© 2021 Snow Pals
	</div>
</body>

</html>