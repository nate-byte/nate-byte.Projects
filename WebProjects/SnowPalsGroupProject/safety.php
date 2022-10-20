<!DOCTYPE html>
<html lang="en">

<head>
    <title>Safety Tips - SnowPals</title>
    <meta charset="UTF-8">
    <meta name="Project Group 11" content="Contact Us">
    <link rel="icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="stylesheet" href="css/main-style.css">
    <link rel="stylesheet" href="css/safety.css">
</head>

<body>
    <?php include 'nav.php'; ?>

    <div class="content">
        <h2>Safety Tips</h2>
        <div class="tips">
            <div id="online">
                <h3 class="question">Tips for SnowPals Use:</h3>
                <ul class="answer">
                    <li>Don't give out personal information (your address, etc until you are confident that the other user is not operating in bad faith.</li>
                    <li>Be respectful towards your fellow users. Violators can be reported <a href="">here.</a></li>
                </ul>
            </div>
            <div id="meeting">
                <h3 class="question">Tips for In-Person Meetings:</h3>
                <ul class="answer">
                    <li>Let someone trusted know what you are doing before you meet up with someone for the first time.</li>
                    <li>Take someone you trust along when meeting up with someone for the first time.</li>
                </ul>
            </div>
            <div id="activities">
                <h3 class="question">Safety Guides for Activities:</h3>
                <ul class="answer">
                    <li><a href="https://www.nsaa.org/NSAA/Safety/Safety_Facts___Tips/NSAA/Safety/Safety_Facts___Tips.aspx">Skiing and Snowboarding Safety - National Ski Areas Associaton</a></li>
                    <li><a href="https://www.dnr.state.mn.us/snowmobiling/safety.html">Snowmobile Safety - Minnesota Department of Natural Resources</a></li>
                    <li><a href="https://www.nsc.org/home-safety/tools-resources/seasonal-safety/winter/sledding">Sledding Safety - National Safety Council</a></li>
                    <li><a href="https://awe365.com/a-guide-to-safety-gear-for-snowkiting/">Snowkiting Safety - AWE365.com</a></li>
                    <li><a href="https://www.takemefishing.org/ice-fishing/ice-fishing-basics/ice-fishing-safety/">Ice Fishing Safety - TakeMeFishing.org</a></li>
                    <li><a href="https://safetyoneinc.com/training/snowcat-operator-training/snowcat-operator-certification/">Snowcat Safety Training - Safety One, Inc (not sponsored)</a></li>
                </ul>
            </div>
            <div id="additional">
                <h3 class="question">Additional Resources:</h3>
                <ul class="answer">
                    <li><a href="https://www.rei.com/">REI.com - Retail and Outdoor Gear (not sponsored)</a></li>
                    <li><a href="">Terms of Service</a></li>
                </ul>
            </div>
        </div>
    </div>

    <?php
    echo '<script type="text/JavaScript">
    var num = document.getElementsByClassName("question");
    var i;

    for (i = 0; i < num.length; i++) {
	    num[i].addEventListener("click", function() {
	        this.classList.toggle("active");
	        var answer= this.nextElementSibling;
	        if (answer.style.display === "block") {
		        answer.style.display = "none"} 
	        else {
     		    answer.style.display = "block"
            }
        });
    }
	</script>';
    ?>

    <div class="footer">
        © 2021 Snow Pals
    </div>
</body>

</html>