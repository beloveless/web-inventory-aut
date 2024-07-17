<?php
function pdo_connect() {
    $host = 'mysql-db';
    $dbname = 'inventory';
    $username = 'root';
    $password = 'password';

    try {
        $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        echo 'Connection failed: ' . $e->getMessage();
        return false;
    }
}


var_dump(pdo_connect());
if ( $pdo = pdo_connect() ) {
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
