<?php

//FOR PHP, YOU NEED A LOCAL MYSQL SERVER (LIKE WORKBENCH) TO CONNECT TO A REMOTE MYSQL SERVER
//BUT PYTHON CAN CONNECT DIRECTLY USING ITS MYSQL.CONNECTOR LIBRARY.
//I am using mysql workbench instead of xampp's mysql, coz could get xampp's mysql to do the job.
//1. I setup a new connection in workbench using below credentials.
//2. I changed port 3308(xampp) to 3306(workbench) in xampp's php.ini, that's all.
//3. Then when I run this file, xampp connects to workbench first using this credentials,..
//   ..workbench then connects this php file to the actual webserver's mysql.
//Here workbench for php acts as mysql.connector for python

//-----For local use to connect to MySQL Workbench:
// $config = parse_ini_file('../r_admin_use/db.ini');
// //print_r($config);
// $server = $config['HOST'];
// $user = $config['USER']; 
// $password = $config['PASSWORD'];
// $database = $config['DB'];

//-----For Online use: math.Foodonya.com
$config = parse_ini_file('/home/foodonya/r_admin_use/db2.ini'); 
$server = "localhost";
$user = $config['USER']; 
$password = $config['PASSWORD']; 
$database = $config['DB'];

// create connection
$conn = new mysqli($server, $user, $password, $database);

// check connection
if ($conn->connect_error) {
	die("Connection failed: " . $conn->connect_error);
}
//echo "Connected successfully";

?>
