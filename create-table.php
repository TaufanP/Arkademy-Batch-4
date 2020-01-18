<?php 
    include "connection.php";

    $sql = "CREATE TABLE customer(
        id int PRIMARY KEY, 
        cashier varchar(50), 
        product varchar(50), 
        category varchar(50), 
        price int, 
        action varchar(50)
    )";

    if ($connection -> query($sql) == TRUE){
        echo "Tabel berhasil dibuat!";
    }else{
        echo "Tabel gagal dibuat!";
    }

?>