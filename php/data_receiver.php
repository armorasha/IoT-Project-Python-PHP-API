<?php
    
//receiving data in a POST request from IoT device using python's requests library
$temperature = $_POST['temp'];
$pressure = $_POST['pres'];
$humidity = $_POST['humi'];
$client_key = $_POST['key'];

//get the server key and check with POSTed client key
//$config = parse_ini_file('../r_admin_use/db2.ini'); //localhost
$config = parse_ini_file('/home/foodonya/r_admin_use/db2.ini'); //Online use

$server_key = $config['POST_KEY'];

if ($server_key === $client_key) //when authentication pass write to db
{
        require_once('../php/conn_php_math_db.php');

        //writing the received data in the database
        $query = "INSERT INTO sensehat_readings (timestamp, temperature, pressure, humidity)" .
            " VALUES (CONVERT_TZ(NOW(),'SYSTEM','Australia/Adelaide'), " . $temperature . ", " . $pressure . ", " . $humidity . ")";
        $result = mysqli_query($conn, $query) or die("R_Invalid Error" . mysqli_error($conn));

        mysqli_close($conn);

        echo "POST data written to database after Auth";
    }
    else {
        echo "Authentication failed";
    }

?>