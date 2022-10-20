<!DOCTYPE html>
<html lang="en">

<head>
    <title>Snow Pals Login</title>
    <meta charset="UTF-8">
    <meta name="Project Group 11" content="HOMEPAGE">

    <link rel="icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="stylesheet" href="css/main-style.css">
    <link rel="stylesheet" href="css/user_inf.css">
    <script src="./verification.js" defer></script>

</head>

<body>

    <script language="javascript" type="text/javascript">
        //Browser Support Code
        function ajaxFunction() {
            var ajaxRequest; // The variable that makes Ajax possible!

            ajaxRequest = new XMLHttpRequest();

            // Create a function that will receive data sent from the server and will update
            // the div section in the same page.

            ajaxRequest.onreadystatechange = function() {
                if (ajaxRequest.readyState == 4) {
                    var ajaxDisplay = document.getElementById('ajaxDiv');
                    ajaxDisplay.innerHTML = ajaxRequest.responseText;

                }
            }

            var username = document.getElementById('user').value;
            var password = document.getElementById('pass').value;
            var post_string = "username=" + username;
            post_string += "&password=" + password;
            ajaxRequest.open("POST", "user_login.php", true);
            ajaxRequest.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            ajaxRequest.send(post_string);
        }
    </script>

    <?php include 'nav.php'; ?>

    <div class="user_inf">
        <form method="POST" id="login_form">

            <label for="username">Username:</label>
            <input name="username" type="text" id="user">
            <br>
            <label for="password">Password:</label>
            <input name="password" type="password" id="pass">
            <br>
            <br>
            <input type="button" value="Login">
            <br>
            <br>
            <br>
            <div id="ajaxDiv" style="color:red;"></div>

        </form>
    </div>

    <div class="footer">
        © 2021 Snow Pals
    </div>

</body>

</html>