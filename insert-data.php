<?php
    include "connection.php";

    if(isset($_POST['submit'])){
        $cashier = $_POST["cashier"];
        $product = $_POST["product"];
        $category = $_POST["category"];
        $price = $_POST["price"];


        $sql = "INSERT customer SET 
        cashier = '$name', 
        product = '$product', 
        category = '$category', 
        price = '$price'";

        if($connection->query($sql) == TRUE){
            echo "Data berhasil di update!";
        }else{
            echo "Data gagal di update!";
        }
    }
?>