<?php
    require_once('../php/conn_php_math_db.php');

    //receiving data in a POST request from IoT device using python's requests library
    $temperature = $_POST['temp'];
    $pressure = $_POST['pres'];
    $humidity = $_POST['humi'];

    //writing the received data in the database
    $query = "INSERT INTO sensehat_readings (timestamp, temperature, pressure, humidity)".
    " VALUES (CONVERT_TZ(NOW(),'SYSTEM','Australia/Adelaide'), ".$temperature.", ".$pressure.", ".$humidity.")";
    $result = mysqli_query($conn, $query) or die("R_Invalid Error" . mysqli_error($conn));

    mysqli_close($conn);
    
?>