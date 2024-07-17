<?php

function pdo_connect(){
    $DATABASE_HOST = 'mysql-db';
    $DATABASE_USER = 'root';
    $DATABASE_PASS = 'password';
    $DATABASE_NAME = 'inventory';
    try {
        echo "Connected to MySQL successfully";
        $pdo=new PDO('mysql:host=' . $DATABASE_HOST . ';dbname=' . $DATABASE_NAME, $DATABASE_USER, $DATABASE_PASS);
    	return $pdo;
    } catch(Exception $e) {
        return $e;
    }    
}

var_dump(pdo_connect());
if ( pdo_connect() ) {
    echo "connected\n";

    try {
        $stmt = $pdo->query("SELECT * FROM tb_admin");

        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
            echo "ID: " . $row['id_admin'] . "\n";
            echo "Username: " . $row['username'] . "\n";
            echo "Password: " . $row['password'] . "\n";
        }
    } catch (PDOException $e) {
        echo 'Query failed: ' . $e->getMessage();
    }

    
} else {
    echo "failed to connect";
}
?>

