<?php
$activityOptions = array('Skiing', 'Snowboarding', 'Snowmobiling', 'Snowbiking', 'Snowshoeing', 'Sledding', 'Tubing', 'Specialized Skiing', 'Snow Kiting', 'Specialized Fishing', 'Snowcat Tours');
$locationOptions = array('Breckenridge', 'Copper', 'Keystone', 'Park_City', 'Snowbird', 'Alta');

$activities = array();
$locations = array();

if (!empty($_POST['activities']) && is_array($_POST['activities'])) {
	foreach ($_POST['activities'] as $activity) {
		if (in_array($activity, $activityOptions)) {
			$activities[] = $activity;
		}
	}
}

if (!empty($_POST['locations']) && is_array($_POST['locations'])) {
	foreach ($_POST['locations'] as $location) {
		if (in_array($location, $locationOptions)) {
			$locations[] = $location;
		}
	}
}

$skill = $_POST['skill'];
header('Location: login.php');
