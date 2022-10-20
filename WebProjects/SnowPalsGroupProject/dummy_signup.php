<!DOCTYPE html>
<html lang="en">

<head>
	<title>Snow Pals</title>
	<meta charset="UTF-8">
	<meta name="Project Group 11" content="dummy_signup">
	<link rel="icon" type="image/x-icon" href="img/favicon.ico">
	<link rel="stylesheet" href="css/main-style.css">
</head>

<body>
	<?php include 'nav.php'; ?>
	<div class="register">
		<form action="registration.php" method="post">
			<label for="username">Username:</label><br>
			<input type="text" id="username" name="username"><br>
			<label for="password">Password:</label><br>
			<input type="text" id="password" name="password"><br>
			<label for="confirmpword">Confirm password:</label><br>
			<input type="text" id="confirmpword" name="confirmpword"><br><br>
			<label for="number">Phone Number:</label><br>
			<input type="text" id="number" name="number"><br><br>
			<label for="email">Email Address:</label><br>
			<input type="text" id="email" name="email"><br><br>

			<input type="submit" value="Next">
		</form>
	</div>

	<div class="footer">
		© 2021 Snow Pals
	</div>
</body>

</html>