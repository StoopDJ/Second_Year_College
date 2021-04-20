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
	<title>Reserve A Book</title>
	<link rel="stylesheet" type="text/css" href="style.css">
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
		<li><a href="Book.php"><span>Reserve a Book</span></a></li>
		<li class='active'><a href="viewReserved.php"><span>View Reserved Books</span></a></li>
		<li class='last'><a href="logout.php"><span>Log Out</span></a></li>
		</ul>
		</div>
		
<center>
<h1>View Your Reserved Books</h1> 



<?php
	require_once "db_book.php";
		
	$check = false;
	$u = $_SESSION['userName'];
	$result = mysqli_query("SELECT * FROM reservedbooks");
            
	if($result === FALSE) 
	{
		echo "There was an error when processing the request";
		die(mysqli_error()); 
	}
		
	else
	{
		echo "<table cellspacing='0'>";
		echo "<form action= \"removeReserve.php\" method='post'>";
		echo "<thead>";
		echo"<tr><th>"; echo "ISBN";
		echo"</th><th>"; echo "Title";
		echo"</th><th>"; echo "Author";
		echo "</th><th>"; echo "Edition";
		echo "</th><th>"; echo "Year";
		echo "</th><th>"; echo "Category";
		echo "</th><th>"; echo "Date Reserved";
		echo "</th><th>"; echo "Remove Reservation?";
		echo "</th></tr>";
		echo "</thead>";
		echo "<tbody>";
		
	
	
		while ( $row = mysqli_fetch_row($result) ) {
				
				
					echo("<tr><td>");
					echo($row[0]);
					echo("</td><td>");
					echo($row[1]);
					echo("</td><td>");
					echo($row[2]);
					echo("</td><td>");
					echo($row[3]);
					echo("</td><td>");
					echo($row[4]);
					echo("</td><td>");
					echo($row[5]);
					echo("</td><td>");
					echo($row[6]);
					echo("</td><td>");
					echo('<a href="removeReserve.php?id='.htmlentities($row[6]).'">Remove</a>  ');
					echo("</tdr>\n");
				}
		
	echo "</tbody>";
	echo "</form>";
	echo "</table>";
	
}
if ($check == false)
	{
		$url = "noReserved.php";
		header( "Location: $url" );
	}
	
	
?>

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