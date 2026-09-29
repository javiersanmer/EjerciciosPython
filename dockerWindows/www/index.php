<?php

try {
    $pdo = new PDO(
        'mysql:host=db;port=3306;dbname=juegos;charset=utf8',
        'usuario',
        'pass',
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
        ]
    );

} catch (PDOException $e) {
    die('Error de conexión a la base de datos: ' . $e->getMessage());
}

$stmt = $pdo->query("SELECT id, titulo, portada FROM videojuegos");
$videojuegos = $stmt->fetchAll();

?>
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Lista de Videojuegos</title>

    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pN1yT2bRjXh0JMhjY6hW+ALEwIH"
    crossorigin="anonymous">

    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="container">
        <h1>Videojuegos Disponibles</h1>

        <div class="juegos">

            <?php foreach ($videojuegos as $juego): ?>
                <div class="card juego" style="width: 18rem;">
                    
                    <img src="<?= 'img/' . $juego['portada']; ?>" class="card-img-top">

                    <div class="card-body">
                        <h2 class="card-title"><?= $juego['titulo']; ?></h2>
                        <button class="btn btn-primary" onclick="location.href='juego.php?id=<?= $juego['id']; ?>'">
                            Ver juego
                        </button>
                    </div>

                </div>
            <?php endforeach; ?>

        </div>
    </div>

</body>
</html>