<!DOCTYPE html>
<html lang="en">

<head>
    <title>Snow Pals Sign Up</title>
    <meta charset="UTF-8">
    <meta name="Project Group 11" content="HOMEPAGE">
    <link rel="icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="stylesheet" href="css/main-style.css">
    <link rel="stylesheet" href="css/user_inf.css">
    <script type="text/javascript" src="verification.js" defer></script>
   
</head>
<body>
<script language = "javascript" type = "text/javascript">

            //Browser Support Code
            function ajaxFunction(){
               var ajaxRequest;  // The variable that makes Ajax possible!

               ajaxRequest = new XMLHttpRequest();

               // Create a function that will receive data sent from the server and will update
               // the div section in the same page.

               ajaxRequest.onreadystatechange = function(){
                  if(ajaxRequest.readyState == 4){
		     var ajaxDisplay = document.getElementById('ajaxDiv');
		     document.body.scrollTop = document.documentElement.scrollTop = 0;
		     ajaxDisplay.innerHTML = ajaxRequest.responseText;

                  }
	       }

	       var username = document.getElementById('username').value;
	       var password = document.getElementById('password').value;
	       var email = document.getElementById('email').value;
	       var num = document.getElementById('number').value;
	       var activities = document.getElementsByName('activities[]');
	       var loc = document.getElementsByName('locations[]');
	       var skill = document.getElementsByName('skill');
	       var post_string = "username="+username;
	       post_string += "&password="+password;
	       post_string +="&number="+num;
	       post_string += "&email="+email;
	      
	       ajaxRequest.open("POST", "registration.php", true);
	       ajaxRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	       ajaxRequest.send(post_string);
	    }
 </script>
<?php
        include 'nav.php';

?>

   
    
    <div class="registration">
	    <form id = "myform"  method="POST">
		<div id="ajaxDiv" style="color:green;">STatus</div>
		<br>
		<br>
		
            <label for="username" style="font-weight: bold">Username:</label><br>
                <div class="req">Username must be at least 6 characters long<br>
                Username must contain only letters and digits<br>
                Username cannot begin with a digit
                </div>

 			<input type="text" id="username" name="username" placeholder="Username"><br>
 			<label for="password" style="font-weight: bold">Password:</label><br>

                <div class="req">Password must be at least 8 characters long<br>
                Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character</div>

 			<input type="password" id="password" name="password" placeholder="Password"><br><br>
 			<label for="number" style="font-weight: bold">Phone Number:</label><br>
 			<input type="text" id="number" name="number" placeholder="8882224444"><br><br>
 			<label for="email" style="font-weight: bold">Email Address:</label><br>
 			<input type="text" id="email" name="email" placeholder="name@email.com"><br><br>
		
		<div class="user_inf" >      
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
        
 			<h3>Skill Level:</h3>
        
 			Beginner <input type="radio" value="beginner" name="skill"><br> 
 			Intermediate <input type="radio" value="intermediate" name="skill"><br>
 			Advanced <input type="radio" value="advanced" name="skill"><br>
 			Expert <input type="radio" value="expert" name="skill"> 
        	</div>
            	<br>           
    
   		<div class="button">
       			<input type="button" value="Register" onclick="Reg(document.getElementById('username').value, document.getElementById('password').value, document.getElementById('number').value, document.getElementById('email').value); ajaxFunction()">
			<br> <br>
			<input type = "button" value = "Clear" onclick = "Clr()" id="s_1">

		
        	</div>
	

	</form> 


 	</div>

     <div class="footer">
         © 2021 Snow Pals
     </div>
    
 </body>

 </html> 
