<?php

//$config = parse_ini_file('../r_admin_use/db2.ini'); //localhost
$config = parse_ini_file('/home/foodonya/r_admin_use/db2.ini'); //Online use

$server_key = $config['POST_KEY'];

    if ($server_key === $client_key) //when authentication fails
    {
        return true;
    }
    else {
       return false;
    }

    ?>
