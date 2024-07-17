<?php 
$koneksi = mysqli_connect("mysql-db", "root", "password", "inventory");

if (mysqli_connect_errno()) {
	echo "Koneksi gagal".mysqli_connect_error();
}
 ?>