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
	<title>Search By Author Or Title For A Book</title>
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
		<li class='active'><a href="searchTitle.php"><span>Search For Book Title</span></a></li>
		<li><a href="searchCategory.php"><span>Search For a Book By Category</span></a></li>
		<li><a href="Book.php"><span>Reserve a Book</span></a></li>
		<li><a href="viewReserved.php"><span>View Reserved Books</span></a></li>
		<li class='last'><a href="logout.php"><span>Log Out</span></a></li>
		</ul>
		</div>
		<center>
<h1>Book Title / Author Search</h1> 

<form id="form4"  method="get">
<fieldset><legend>Search form</legend><p class="first">
<p class="first">
<label for="bookTitle">Book Title:</label>
<input type="text" name="bookTitle"  maxlength="31" size="30"> 
</p>
<p>
<label for="author">Author:</label>
<input type="text" name="author"  maxlength="31" size="30">
</p>
<p>
<p class="submit"><button type="submit" value="Search">Search</button></p>
</fieldset>
</form> 
<?php
	require_once "db_book.php"; 
	
if ( isset($_GET['bookTitle']) && isset($_GET['author']))
	{
		$t = mysqli_real_escape_string($db, $_GET['bookTitle']);
		$a = mysqli_real_escape_string($db, $_GET['author']); 	

		if (trim($t) != '' || trim($a) != '')
		{
			if (trim($a) == '')
			{		
				search($t, NULL, 1);
			}
		
			else if (trim($t) == '')
			{		
				search($a, NULL, 2);
			}
		
			else
			{		
				search($t, $a, 3);
			}
		}

		else
		{
			echo "You must fill in at least one of the fields!";
		}
	}
	else
	{
		echo "Enter the name of the book, the author or both in the boxes above";
	}

	function search($searchTerm1, $searchTerm2, $option)
	{


		global $db;
		if ($option == 1)
		{
			$sql = ("SELECT * FROM books WHERE bookTitle LIKE '%$searchTerm1%'");
		}
			
		else if ($option == 2)
		{
			$sql = ("SELECT * FROM books WHERE author LIKE '%$searchTerm1%'");
		}
			
		else
		{
			$sql = ("SELECT * FROM books WHERE bookTitle LIKE '%$searchTerm1%' AND author LIKE '%$searchTerm2%'");
		}
	
		$result = mysqli_query($db, $sql);
			
		if(mysqli_num_rows($result) === 0) 
		{
			echo "No results found, please refine search!";
			die(mysqli_error()); 
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
			echo"</thead>";
		    
		    echo "<tbody>";
			
			// loop through results of database query, displaying them in the table 
			for ($i = 0; $i < mysqli_num_rows($result); $i++)
			{
		
		

			

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
				
		
			echo "</tbody>";
			echo "</form>";
			echo "</table>";
						if (($i % 2) == 0)
				{
					echo"<tr class =\"even\"><td>"; 
				}
		
				else
				{
					echo"<tr><td>"; 
				} 
				}
			
		}
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
</body>
</html>