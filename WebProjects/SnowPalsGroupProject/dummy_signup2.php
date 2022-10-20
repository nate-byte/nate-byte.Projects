<!DOCTYPE html>
<html lang="en">

<head>
	<title>Snow Pals</title>
	<meta charset="UTF-8">
	<meta name="Project Group 11" content="dummy_signup2">
	<link rel="icon" type="image/x-icon" href="img/favicon.ico">
	<link rel="stylesheet" href="css/main-style.css">
</head>

<body>
	<?php include 'nav.php'; ?>
	<div class="register">
		<form action="registration2.php" method="post">
			<label for="interest">Areas of Interest:</label><br>
			<input type="checkbox" id="activities[]" name="activities[]" value="Skiing">
			<label for="interest1">Skiing</label><br>
			<input type="checkbox" id="activities[]" name="activities[]" value="Snowboarding">
			<label for="interest2">Snowboarding</label><br>

			<label for="interest">Accessible Locations:</label><br>
			<input type="checkbox" id="locations[]" name="locations[]" value="Ava_Act">
			<label for="location1">Ava Act</label><br>
			<input type="checkbox" id="locations[]" name="locations[]" value="Breckenridge">
			<label for="location2">Breckenridge</label><br>
			<input type="checkbox" id="locations[]" name="locations[]" value="Copper">
			<label for="location3">Copper</label><br>
			<input type="checkbox" id="locations[]" name="locations[]" value="Keystone">
			<label for="location4">Keystone</label><br>
			<input type="checkbox" id="locations[]" name="locations[]" value="Park_City">
			<label for="location5">Park City</label><br>
			<input type="checkbox" id="locations[]" name="locations[]" value="Snowbird">
			<label for="location6">Snowbird</label><br>

			<label for="interest">Skill Level:</label><br>
			<input type="radio" value="beginner" name="skill"> Beginner
			<input type="radio" value="intermediate" name="skill"> Intermediate
			<input type="radio" value="advanced" name="skill"> Advanced
			<input type="radio" value="expert" name="skill"> Expert

			<input type="submit" value="Register">
		</form>

	</div>

	<div class="footer">
		© 2021 Snow Pals
	</div>
</body>

</html>