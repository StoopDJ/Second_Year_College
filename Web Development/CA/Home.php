<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset='utf-8'>
   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   <meta name="viewport" content="width=device-width, initial-scale=1"> 
   <link rel="stylesheet" href="style.css">
   <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
   <script src="script.js"></script>

   
	<title>Home</title>
	   <link rel="stylesheet" href="style.css">
	
	<?php
		session_start();
		if(!$_SESSION['userName'])
		{
			header("location:login.php");
		}
	?>
	

</head>
<body>

<div class="body">
	<div id='cssmenu'>
		<ul>
		<li class='active'><a href="Home.php"><span>Home</span></a></li>
		<li><a href="searchTitle.php"><span>Search For Book Title</span></a></li>
		<li><a href="searchCategory.php"><span>Search For a Book By Category</span></a></li>
		<li><a href="Book.php"><span>Reserve a Book</span></a></li>
		<li><a href="viewReserved.php"><span>View Reserved Books</span></a></li>
		<li class='last'><a href="logout.php"><span>Log Out</span></a></li>
		</ul>
		</div>
		<center>
	<h1>Welcome To The Digital Library</h1>
<img src="./images/library-open-book_stock_29062017.jpg" alt="library" style="width:680px;height:340px">
		</center></div>
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