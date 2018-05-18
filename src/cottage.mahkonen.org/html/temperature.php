<?php
header("Content-Type: application/json; charset=UTF-8");

$servername = "localhost";
$username = "iot";
$password = "pw4iot";
$dbname = "iot";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}


$result = $conn->query("SELECT * FROM TEMPERATURE");
$outp = array();
$outp = $result->fetch_all(MYSQLI_ASSOC);

echo json_encode($outp);
$conn->close();
?>
