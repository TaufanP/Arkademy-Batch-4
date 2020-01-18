<?php
    $host = "localhost"; //localhost database
    $username = "root"; //username database
    $password = "";
    $db = "profile";
    $connection = new mysqli($host, $username, $password, $db); //membuat koneksi ke server mysql
    
    /*if ($connection->connect_error){
        die("Koneksi ke database gagal!");
    }else{
        echo "Koneksi ke database berhasil!";
    }*/

?>