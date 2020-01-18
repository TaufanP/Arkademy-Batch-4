<?php
    include "connection.php";
    
    $sql = "CREATE DATABASE cafe";

    if($connection->query($sql) === TRUE){
        echo "Database berhasil dibuat!";
    }else{
        echo "Database gagal dibuat!";
    }
?>