<!DOCTYPE html>
<?php
    include "connection.php";
    $result=mysqli_query($connection, "SELECT * FROM customer");
?>
<html>
<head>
    <title>POS App</title>
    <link type="text/css" rel="stylesheet" href="assets/css/pos-app.css">
    <script src="assets/jquery/jquery-3.3.1.min.js"></script>
    <script src="assets/jquery/my_jquery_functions.js"></script>
</head>
<body>
    <nav>
        <div class="logo" style="background-image: url(assets/img/logo.png);"></div>
        <div class="search-box"><span>Search anything you need</span></div>
        <button class="addTop" type="button">ADD</button>
    </nav>
    
    <section id="tabel">
        <table class="tabel-menu">
            <tr>
                <th class="topleft">No</th>
                <th>Cashier</th>
                <th>Product</th>
                <th>Category</th>
                <th>Price</th>
                <th class="topright">Action</th>
            </tr>
            <?php
                while($row=mysqli_fetch_assoc($result)){
                    echo "<tr>";
                    echo "<td>".$row['cashier']."</td>";
                    echo "<td>".$row['product']."</td>";
                    echo "<td>".$row['category']."</td>";
                    echo "<td>".$row['price']."</td>";
                    echo "</tr>";
                }
            ?>
        </table>
    </section>
    <section id="addcust">
        <div class="addTitle">Add</div>
        <div class="closeAdd">X</div>
        
        
        <form method="#" action="#" id="addForm">
            <div class="form">
              <input id="inpName" type="text" name="name" placeholder="Raisa Andriana">
            </div>
            <div class="form">
              <input id="inpType" type="text" name="product" placeholder="Drink">
            </div>
            <div class="form">
              <input id="inpMenu" type="text" name="category" placeholder="Ice Tea">
            </div>
            <div class="form">
              <input id="inpPrice" type="text" name="price" placeholder="Rp. 10.000">
            </div>
            <div>
              <input onclick="" type="submit" name="submit" value="ADD" class="addButton">
            </div>
        </form>
    </section>
</body>
</html>