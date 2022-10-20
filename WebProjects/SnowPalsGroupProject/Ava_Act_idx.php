<!DOCTYPE html>

<html lang="en">

<head>
    <title>Available Activities</title>
    <meta charset="UTF-8">
    <meta name="Activities index page" content="Resort Activities">
    <meta name="Princess Owotade" content="Group 11">
    <link rel="icon" type="image/x-icon" href="img/favicon.ico">
    <link rel="stylesheet" href="css/activ_index.css">
    <script type="text/javascript" src="Filter.js" defer></script>
</head>

<body>

    <?php include 'nav.php'; ?>

    <div id="selectors">
        <button class="btn active" onclick="filter('all')"> Show all</button>
        <button class="btn" onclick="filter('skiboard')"> Skiing/Snowboarding</button>
        <button class="btn" onclick="filter('snowmobile')"> Snowmobiling</button>
        <button class="btn" onclick="filter('snowbike')"> Snow Biking</button>
        <button class="btn" onclick="filter('snowshoe')"> Snow Shoeing</button>
        <button class="btn" onclick="filter('sledtube')"> Sledding/Tubing</button>
        <button class="btn" onclick="filter('specski')"> Specialized Skiing</button>
        <button class="btn" onclick="filter('snowkite')"> Snow Kiting</button>
        <button class="btn" onclick="filter('specfish')"> Specialized Fishing</button>
        <button class="btn" onclick="filter('snowcat')"> Snowcat Tours/Skiing</button>
    </div>
    <br>
    <br>

    <div class="container">
        <div class="filterDiv skiboard snowmobile snowbike snowshoe specski">
            <h2>Park City Mountain</h2>
            <a href="ParkCity.php"><img class="park" src="img/park_c.jpg"></a>
        </div>

        <br>
        <div class="filterDiv skiboard snowshoe snowcat">
            <h2>Alta Resort</h2>
            <a href="Alta.php"><img class="park" src="img/Alta.jpg"></a>
        </div>
        <br>

        <div class="filterDiv sledtube snowmobile skiboard snowshoe">

            <h2>Keystone Resort</h2>
            <a href="Keystone.php"><img class="park" src="img/keystone.jpg"></a>
        </div>

        <br>

        <div class="filterDiv sledtube skiboard snowkite specfish snowshoe">


            <h2>Breckenridge Ski Resort</h2>
            <a href="Breckenridge.php"><img class="park" src="img/brek.jpg"></a>
        </div>


        <br>
        <div class="filterDiv specski snowkite snowbike specfish skiboard">

            <h2>Copper Mountain</h2>
            <a href="Copper.php"><img class="park" src="img/copper.jpg"></a>
        </div>

        <br>

        <div class="filterDiv specfish specski snowcat snowmobile snowshoe">

            <h2>Snowbird Ski Resort</h2>

            <a href="Snowbird.php"><img id="snowbird" class="park" src="img/snowbird.jpg"></a>
        </div>

    </div>

    <div class="footer">
        © 2021 Snow Pals
    </div>

</body>

</html>