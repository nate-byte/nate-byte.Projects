<?php

if (!isset($_COOKIE["User"])) {
    //this indicates the page you wanted to access
    setcookie("lastPage", 'exampleAccess.php');
    // this is the page you just came from, so like the login section
    header("Location: login.php");
} else {
    //Here we print if the user had logged in the page they wanted to access only if the cookie "User" is activated.
    print <<<page
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="CSS/main-style.css">
<head>
<title>Log In</title>
</head>
<body>

</body>
</html>
page;
}
