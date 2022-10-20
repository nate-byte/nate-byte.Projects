<?php
        

	$server = 'spring-2021.cs.utexas.edu';
	$user   = '';
	$pwd    = '';
	$dbName = '';

	$mysqli = new mysqli ($server, $user, $pwd, $dbName);

	if ($mysqli->connect_errno) {
  		die('Connect Error: ' . $mysqli->connect_errno . ": " . $mysqli->connect_error);
	}
	
	$username = $_POST['username'];
        $password = $_POST['password'];
	
	$username = $mysqli->real_escape_string($username);
        $password = $mysqli->real_escape_string($password);

	$query = "SELECT * FROM snowpals_users WHERE user='$username' AND pass='$password'";
	$userMatch = mysqli_query($mysqli, $query);
	
	
	if (mysqli_num_rows($userMatch) >= 1) {
  		$mysqli->close();
		header('Location: demo_profile.php');
	} else{
		$mysqli->close();
		echo "Invalid username or password";
	}
