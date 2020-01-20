<?php
    
//receiving data in a POST request from IoT device using python's requests library
$client_key = $_POST['key'];

//get the server key and check with POSTed client key
//$config = parse_ini_file('../r_admin_use/db2.ini'); //localhost
$config = parse_ini_file('/home/foodonya/r_admin_use/db2.ini'); //Online use

$server_key = $config['POST_KEY'];

if ($server_key === $client_key) //when authentication passes write to db
{
        require_once('../php/conn_php_math_db.php');

        //writing the received data in the database
        $query = "DELETE FROM sensehat_readings WHERE reading_id NOT IN(SELECT * FROM(SELECT reading_id FROM sensehat_readings ORDER BY timestamp DESC LIMIT 10) r)";
        $result = mysqli_query($conn, $query) or die("R_Invalid Error" . mysqli_error($conn));

        mysqli_close($conn);

        echo "Database cleaned after Auth";
    }
    else {
        echo "POST Authentication failed";
    }

?>