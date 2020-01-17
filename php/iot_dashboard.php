<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no"> <!-- initial scale 1 for mobile website -->
    <title>math.foodonya</title>
    <meta name="apple-mobile-web-app-title" content="math.foodonya">


    <?php
    //Start session right after title
    //session_start();

    //Page-entry parameter check No need for this page------------------------------
    ?>

    <!-- Bootstrap reference starts -->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <link href="https://fonts.googleapis.com/css?family=Titillium+Web&display=swap" rel="stylesheet">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    <!-- md is the breakpoint for 768px device. refer bottom comments on styles.css file. -->
    <!-- Bootstrap reference ends -->

    <!--  Custom Styles file should be added after the Bootstrap library links, as in here.-->
    <link href="../css/style.css" rel="stylesheet" type="text/css">


</head>

<body>

    <!-- Bootstrap Header -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark shadow">
        <a class="navbar-brand" href="/index.php"><i class="fas fa-feather"></i> <span class="span-math">math.</span>FOODONYA.com</a>
    </nav>


    <?php
    require_once('../php/conn_php_math_db.php');

    //getting the most recent record from the database
    $query = "SELECT * from sensehat_readings ORDER BY timestamp DESC LIMIT 1";
    $result = mysqli_query($conn, $query) or die("R_Invalid Error" . mysqli_error($conn));

    while ($row = $result->fetch_assoc()) {
        $timestamp = $row["timestamp"];
        $temperature = $row["temperature"];
        $pressure = $row["pressure"];
        $humidity = $row["humidity"];
    }
    ?>


    <!-- dashboard tiles -->
    <div class="container container-fixed-width">
        <div class="container mt-5">

            <h1 class="display-4 text-secondary mb-2">IoT Dashboard</h1>

            <div class="card-deck">
                <div class="card text-secondary bg-dark mb-3 shadow" style="max-width: 18rem;">
                    <div class="card-header">Sensor 1 <i class="float-right fas fa-thermometer-three-quarters fa-2x"></i></div>
                    <div class="card-body">
                        <h5 class="card-title">Temperature</h5>
                        <h1 class="card-title text-info"><?php echo $temperature; ?>°C</h1>
                        <p class="card-text">
                            Temperature at sensor.
                            Nearby heat sources can give inaccurate readings.
                        </p>
                    </div>
                </div>

                <div class="card text-secondary bg-dark mb-3 shadow" style="max-width: 18rem;">
                    <div class="card-header">Sensor 2 <i class="float-right fas fa-cloud-sun-rain fa-2x"></i></div>
                    <div class="card-body">
                        <h5 class="card-title">Pressure</h5>
                        <h1 class="card-title text-primary"><?php echo $pressure; ?> mbar</h1>
                        <!-- <h2 class="card-title text-primary">millibar</h2> -->
                        <p class="card-text">
                            Atmospheric pressure at sea level is 1 bar.
                            Low pressure systems bring clouds and rain.
                        </p>
                    </div>
                </div>

                <div class="card text-secondary bg-dark mb-3 shadow" style="max-width: 18rem;">
                    <div class="card-header">Sensor 3 <i class="float-right fas fa-tint fa-2x"></i></div>
                    <div class="card-body">
                        <h5 class="card-title">Humidity</h5>
                        <h1 class="card-title text-success"><?php echo $humidity; ?>%</h1>
                        <p class="card-text">
                            A relative humidity level between 35% to 50% is ideal for comfort.
                        </p>
                    </div>
                </div>
            </div>
        </div>


        <div class="container">
            <div class="col container p-4 bg-dark text-secondary rounded shadow">
                <h5><i class="fas fa-cloud-upload-alt"></i>&emsp; Data</h5>
                <p class="pt-4">Last received: <?php echo $timestamp; ?></p>
                <p>From IP address: 103.217.167.118</p>
            </div>
        </div>

        <div class="container">
            <div class="col container">
                <blockquote class=" blockquote my-5">
                    <p class="mb-0 text-secondary">It's estimated that 1.9bn devices are already connected to this Internet of Things.</p>
                    <footer class="blockquote-footer"> <cite title="Source Title">Source: Salesforce</cite></footer>
                </blockquote>
            </div>
        </div>

    </div>

    <?php
    mysqli_close($conn);
    ?>

    <div class="container container-spacer"></div>

        <!-- Bootstrap footer-->
        <nav class="navbar fixed-bottom navbar-dark bg-warning-custom">
            <span class="navbar-text bottom text-warning">
                Yavany & Raja <i class="fas fa-copyright"></i> 2020
            </span>
        </nav>




        <!--Reference to JavaScript code file -->
        <!-- <script src="js/search_page.js">
        </script> -->




</body>

</html>