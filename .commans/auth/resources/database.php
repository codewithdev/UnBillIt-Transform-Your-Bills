<?php 

$email = '';
$dsn= 'mysql:host=localhost; dbname= register';
$password= '';

try{

$db= new PDO($dsn, $email, $password);
$db=
echo "Connected to the register database";
}
catch(PDOException $ex){
	echo "Connection Failed";
}
?>