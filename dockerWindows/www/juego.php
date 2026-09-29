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

$id = $_GET['id'] ?? null;

if (!$id) {
    die("ID no válido");
}

$stmt = $pdo->prepare("SELECT titulo, portada, fecha_lanzamieno FROM videojuegos WHERE id = ?");
$stmt->execute([$id]);
$juego = $stmt->fetch();

if (!$juego) {
    die("Juego no encontrado");
}

?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title><?= $juego['titulo']; ?></title>

    <link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
    integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pN1yT2bRjXh0JMhjY6hW+ALEwIH"
    crossorigin="anonymous">

    <link rel="stylesheet" href="juegos.css">
</head>

<body>

<div class="container">
    <h1><?= $juego['titulo']; ?></h1>

    <div class="card juego" style="width: 18rem; margin:auto;">

        <img src="<?= 'img/' . $juego['portada']; ?>" class="card-img-top">

        <div class="card-body">

            <h2 class="card-title">
                <?= $juego['titulo']; ?>
            </h2>

            <p>
                Fecha de lanzamiento:
                <?= $juego['fecha_lanzamieno']; ?>
            </p>

        </div>

    </div>
</div>

</body>
</html>