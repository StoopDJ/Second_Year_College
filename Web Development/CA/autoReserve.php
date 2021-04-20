<!DOCTYPE html PUBLIC "-//W3C//DD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<html lang="en">
<head>
	<meta charset='utf-8'>
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <link rel="stylesheet" href="style.css">
   <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
   <script src="script.js"></script>
	<title>Reserving Book</title>
	
	<?php
		session_start();
		if(!$_SESSION['userName'])
		{
			header("location:login.php");
		}
	
	?>
</head>

<body>
<div class="wrapper">
	<div id='cssmenu'>
		<ul>
		<li><a href="Home.php"><span>Home</span></a></li>
		<li><a href="searchTitle.php"><span>Search For Book Title</span></a></li>
		<li><a href="searchCategory.php"><span>Search For a Book By Category</span></a></li>
		<li class='active'><a href="Book.php"><span>Reserve a Book</span></a></li>
		<li><a href="viewReserved.php"><span>View Reserved Books</span></a></li>
		<li class='last'><a href="logout.php"><span>Log Out</span></a></li>
		</ul>
		</div>
<center>		
 


<?php
require_once "db_book.php";


if(isset($_GET['ISBN'])){
		
		$ISBN = mysqli_real_escape_string($db, $_GET['ISBN']);
		$sql= mysqli_query("INSERT INTO reservedbooks (ISBN, userName, reservedDate) VALUES ('$ISBN','".$_SESSION['userName']."', '".date("d/m/Y")."')");

		mysqli_query($db, $sql);
		
		
		$sql ="UPDATE books SET reserved = 'Y' WHERE ISBN = '".$ISBN."'";
		
		if (!mysql_query($sql))
		{
			echo $sql;
			echo "<h1>There was an error when processing the request</h1>";
		}
		
		else
		{
			$result = mysql_query($sql);
			echo "<h1>Book Successfully Reserved</h1>";
		}	
		

		
}
?>


<a href="Home.php">Return to Home</a>
</center>
</div>
</div>


<?php
echo "<div class=\"footer\">";
echo "<p>Logged in as: " . $_SESSION['userName'] . "</p>";
echo "</div>";
?>
<script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
   <script src="script.js"></script>
</body>
</html>