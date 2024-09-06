<?php

    $host = "localhost";
    $username = "root";
    $password = "";
    $database = "phpecom";

    $con = mysqli_connect($host, $username, $password, $database);

    if(!$con)
    {
        die("Connection Falied: ". mysqli_connect_error());
    }
?>