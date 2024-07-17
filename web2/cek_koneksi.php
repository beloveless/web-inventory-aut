<?php

function pdo_connect(){
    $DATABASE_HOST = 'mysql-db';
    $DATABASE_USER = 'root';
    $DATABASE_PASS = 'password';
    $DATABASE_NAME = 'inventory';
    try {
        echo "Connected to MySQL successfully";
    	return new PDO('mysql:host=' . $DATABASE_HOST . ';dbname=' . $DATABASE_NAME, $DATABASE_USER, $DATABASE_PASS);
    } catch(Exception $e) {
        return $e;
    }    
}

var_dump(pdo_connect());
if ( pdo_connect() ) {
    echo "connected";
} else {
    echo "failed to connect";
}
?>