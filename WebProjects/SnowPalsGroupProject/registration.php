<?php
        $username = $_POST['username'];
        $password = $_POST['password'];
        $number = $_POST['number'];
	$email = $_POST['email'];

	

	$activityOptions = array('Skiing', 'Snowboarding','Snowmobiling','Snowbiking','Snowshoeing','Sledding','Tubing','Specialized Skiing','Snow Kiting','Specialized Fishing','Snowcat Tours');
	$locationOptions = array('Breckenridge', 'Copper', 'Keystone', 'Park_City', 'Snowbird', 'Alta');

	$activities = array();
	$locations = array();

	if(!empty($_POST['activities']) && is_array($_POST['activities'])){
    		foreach($_POST['activities'] as $activity){
        		if(in_array($activity, $activityOptions)){
            			$activities[] = $activity;
        		}
    		}
	}

	if(!empty($_POST['locations']) && is_array($_POST['locations'])){
    		foreach($_POST['locations'] as $location){
        		if(in_array($location, $locationOptions)){
            			$locations[] = $location;
        		}
    		}
	}

        $skill = $_POST['skill'];

	$activities = implode(" ", $activities);
	$locations = implode(" ", $locations);
	

	$server = "spring-2021.cs.utexas.edu";
	$user   = "";
	$pwd    = "";
	$dbName = "";

	$mysqli = new mysqli ($server, $user, $pwd, $dbName);

	if ($mysqli->connect_errno) {
  		die('Connect Error: ' . $mysqli->connect_errno . ": " . $mysqli->connect_error);
	}

	$query = "SELECT * FROM snowpals_users WHERE user='$username'";
	$result = $mysqli->query($query);
	$row = $result->fetch_row();

	if($result){
		
		if($row[0] == $username){
			echo '<script>alert("That username is taken")</script>';
		}
		else if ($row[3] == $email){
			echo '<script>alert("That email is already in use")</script>';
		}
		else if ($row[2] == $number){
			echo '<script>alert("That number is already in use")</script>';
		}
		else if ($row[0] != $username and $row[2] != $number and $row[3] != $email){
			$query1 = "INSERT INTO snowpals_users (user, pass, number, email) 
				VALUES ('$username', '$password', '$number', '$email')"; 
			$result_q1 = $mysqli->query($query1);
			if($result_q1){
				echo "Successfully created a new user! You may now log in from the login page.";
				
			}
		}
		else{echo "System Error. Please try again later.";}
	}
	
	$mysqli->close();
	
	
?>
