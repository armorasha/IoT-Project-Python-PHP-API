    <?php
    require_once('../php/conn_php_math_db.php');

    //getting the most recent record from the database
    $query = "SELECT * from sensehat_readings ORDER BY timestamp DESC LIMIT 1";
    $result = mysqli_query($conn, $query) or die("R_Invalid Error" . mysqli_error($conn));

    //and get the sensor readings for that record
    while ($row = $result->fetch_assoc()) {
        $timestamp = $row["timestamp"];
        $temperature = $row["temperature"];
        $pressure = $row["pressure"];
        $humidity = $row["humidity"];
    }
    ?>

    <!-- Draw the card deck -->
    <div class="card-deck">
        <div class="card text-secondary bg-dark mb-3 shadow mx-auto">
            <div class="card-header">Sensor 1 <i class="float-right fas fa-thermometer-three-quarters fa-2x"></i></div>
            <div class="card-body">
                <h5 class="card-title">Temperature</h5>
                <!--print reading here-->
                <h1 class="card-title text-info"><?php echo $temperature; ?> °C</h1>
                <p class="card-text">
                    Temperature at sensor.
                    Nearby heat sources can give inaccurate readings.
                </p>
            </div>
        </div>

        <div class="card text-secondary bg-dark mb-3 shadow mx-auto">
            <div class="card-header">Sensor 2 <i class="float-right fas fa-cloud-sun-rain fa-2x"></i></div>
            <div class="card-body">
                <h5 class="card-title">Pressure</h5>
                <!--print reading here-->
                <h1 class="card-title text-primary"><?php echo $pressure; ?> mbar</h1>
                <!-- <h2 class="card-title text-primary">millibar</h2> -->
                <p class="card-text">
                    Atmospheric pressure at sea level is 1 bar.
                    Low pressure systems bring clouds and rain.
                </p>
            </div>
        </div>

        <div class="card text-secondary bg-dark mb-3 shadow mx-auto">
            <div class="card-header">Sensor 3 <i class="float-right fas fa-tint fa-2x"></i></div>
            <div class="card-body">
                <h5 class="card-title">Humidity</h5>
                <!--print reading here-->
                <h1 class="card-title text-success"><?php echo $humidity; ?> %</h1>
                <p class="card-text">
                    A relative humidity level between 35% to 50% is ideal for comfort.
                </p>
            </div>
        </div>
    </div>
    </div>


    <div class="container-fluid data mx-auto p-0 mx-4">
        <!--p-0 float-left-->
        <div class="col container px-3 pt-3 pb-1 bg-dark text-secondary rounded shadow">
            <h5><i class="fas fa-cloud-upload-alt"></i>&emsp; Data</h5>
            <!--print reading here-->
            <p class="pt-2 mb-n1">Last received: <?php echo $timestamp; ?></p>
            <p>From IP address: 103.217.167.118</p>
        </div>
    </div>


    <?php
    mysqli_close($conn);
    ?>