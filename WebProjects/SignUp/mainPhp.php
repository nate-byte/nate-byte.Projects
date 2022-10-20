<?php
function console_log($output, $with_script_tags = true) {
    $js_code = 'console.log(' . json_encode($output, JSON_HEX_TAG) . 
');';
    if ($with_script_tags) {
        $js_code = '<script>' . $js_code . '</script>';
    }
    echo $js_code;
}
?>
<?php
$mainfile = file("signup.txt");
$inputs = array($_POST["8am"],
$_POST["9am"],
$_POST["10am"],
$_POST["11am"],
$_POST["12pm"],
$_POST["1pm"],
$_POST["2pm"],
$_POST["3pm"],
$_POST["4pm"],
$_POST["5pm"]
);


$slots = array();
$count = 0;
file_put_contents ("signup.txt" , "okokok");
foreach($mainfile as $line){
    if($inputs[$count] != null){
        $temp = $line;
        preg_replace ($line, "-", $inputs[$count]);
        preg_replace ($mainfile, $temp, $line);
        console_log($line);
        console_log($temp);
        console_log($inputs[$count]);
        console_log(preg_replace ($mainfile, $temp, $line))

    } else {
        list($num, $cont) = explode('-', $line);
        $slots[$num] = $cont;
    }
    $count ++;
}
console_log($_POST["8am"]);

?>
<?php
print <<<PRHTMLHEAD
<!DOCTYPE html>
<html>
<link rel="stylesheet" href="Style/styleh12.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script> 
<head>
<title>Sing Up Sheet</title>
</head>
<body>
<h1>yeet</h1>
<body>
PRHTMLHEAD;
 echo(
"<form action = \"mainPhp.php\" method = \"POST\">
<table class=\"timeTable\">\n
<caption style=\"margin-bottom:0.25cm;\"><h1>Sign-Up Sheet</h1> </caption>\n
<tr><thead><th  class=\"tableTop\">Time</th><th>Name</th></thead></tr>\n
<tbody>
 ");
            echo "<tr><td> 8:00 AM </td><td>", $slots["8am"] ,"</td></tr>";
            echo "<tr><td> 9:00 AM </td><td>", $slots["9am"] ,"</td></tr>";
            echo "<tr><td> 10:00 AM </td><td>", $slots["10am"] ,"</td></tr>";
            echo "<tr><td> 11:00 AM </td><td>", $slots["11am"] ,"</td></tr>";
            echo "<tr><td> 12:00 PM </td><td>", $slots["12pm"] ,"</td></tr>";
            echo "<tr><td> 1:00 PM </td><td>", $slots["1pm"] ,"</td></tr>";
            echo "<tr><td> 2:00 PM </td><td>", $slots["2pm"] ,"</td></tr>";
            echo "<tr><td> 3:00 PM </td><td>", $slots["3pm"] ,"</td></tr>";
            echo "<tr><td> 4:00 PM </td><td>", $slots["4pm"] ,"</td></tr>";
            echo "<tr><td> 5:00 PM </td><td>", $slots["5pm"] ,"</td></tr>";
echo("
</tbody>
</table>
<br>
<div id = \"btn\">
<input name= \"submit\" type = \"submit\" value = \"Submit\"/>
</div>
</form>
</body>
</html>
");

?>