<?php

 define('DB_HOST', 'localhost');
 define('DB_NAME', 'book'); 
 define('DB_USER','root'); 
 define('DB_PASSWORD','');
$db = mysqli_connect('localhost', 'root', ''); 
if ( $db === FALSE ) die('Fail message'); 
if ( mysqli_select_db($db, "book") === FALSE ) die("Fail message"); 
?>  