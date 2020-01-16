<?php

require_once('../php/conn_php_math_db.php');

$query = "SELECT * FROM sensehat_readings";
$result = mysqli_query($conn, $query) or die("R_Invalid Error" . mysqli_error($conn));

while ($row = $result->fetch_assoc()) {
    echo "reading id: " . $row["reading_id"] . " timestamp: " . $row["timestamp"] . " temp: " . $row["temperature"]
     . " pres: " . $row["pressure"] . " hum: " . $row["humidity"] . "<br>";
}

mysqli_close($conn);

?>