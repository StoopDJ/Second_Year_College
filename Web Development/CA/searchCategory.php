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
	<title>Search By Category For A Book</title>
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
		<li class='active'><a href="searchCategory.php"><span>Search For a Book By Category</span></a></li>
		<li><a href="Book.php"><span>Reserve a Book</span></a></li>
		<li><a href="viewReserved.php"><span>View Reserved Books</span></a></li>
		<li class='last'><a href="logout.php"><span>Log Out</span></a></li>
		
		</ul>
		</div>

<center>
<h1>Category Search</h1> 
<form id="form4"  method="get">
<fieldset><legend>Search form</legend><p class="first">
<p class="first">
<label for="category">Category Type:</label>
<input type="text" name="category" maxlength="31" size="30"></p> 
<p>
<p class="submit"><button type="submit" value="Search">Search</button></p>
</fieldset></form> 

<?php
	require_once "db_book.php"; 
	if ( isset($_GET['category']))
	{
		$c = $_GET['category'];
		
		if (trim($c) != '')
		{
		
			$sql = ("SELECT * FROM books LEFT JOIN categories ON books.category = categories.categoryID WHERE CategoryDescription LIKE '%".$c."%'");
 
			$result = mysqli_query($db,$sql);
			
			if(mysqli_num_rows($result) === 0) 
			{
				echo "No results found, please refine search!";
				die(mysqli_error($db)); 
			}
			
			$row = mysqli_fetch_assoc($result);
 
			// number of results to show per page
			$per_page = 5;
 
			// figure out the total pages in the database
			$total_results = mysqli_num_rows($result);
			$total_pages = ceil($total_results / $per_page);
 
			// check if the 'page' variable is set in the URL 
			if (isset($_GET['page']) && is_numeric($_GET['page']))
			{
			$show_page = $_GET['page'];
         
				// make sure the $show_page value is valid
				if ($show_page > 0 && $show_page <= $total_pages)
				{
					$start = ($show_page -1) * $per_page;
					$end = $start + $per_page; 
				}
				else
				{
					// error - show first set of results
					$start = 0;
					$end = $per_page; 
				}       
			}
			else
			{
				// if page isn't set, show first set of results
				$start = 0;
				$end = $per_page; 
			}	
     
		// display pagination
		for ($i = 1; $i <= $total_pages; $i++)
		{
			echo "<a href='searchCategory.php?&category=$c&page=$i'>$i</a> ";
		}
		echo "</p>";
         
		
			echo "<table cellspacing='0'>";
			echo "<form action= \"autoReserve.php\" method='post'>";				
			echo "<thead>";	 
			echo"<tr><th>"; echo "ISBN";
			echo"</th><th>"; echo "Title";
			echo"</th><th>"; echo "Author";
			echo "</th><th>"; echo "Edition";
			echo "</th><th>"; echo "Year";
			echo "</th><th>"; echo "Category";
			echo "</th><th>"; echo "Reserved";
			echo "</th><th>"; echo "Do You Wish To Reserve?";
			echo "</th></tr>";
			echo "</thead>";
			echo "<tbody>";
			
			for ($i = $start; $i < $end; $i++)
			{
				// make sure that PHP doesn't try to show results that don't exist
				if ($i == $total_results) 
				{
					break;
				}
          
						
			
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

				echo('<a href="autoReserve.php?id='.htmlentities($row[6]).'">Reserve</a>  ');
				echo("</tdr>\n");
					
			}
			
			echo "</tbody>";
			
			echo "</form>";
			echo "</table>";
			}
		}
			
		
	}
		
	else
	{
		echo "You must fill in the category box!";
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