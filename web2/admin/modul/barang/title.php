<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="">
  <meta name="author" content="">
  <title><?php echo $judul; ?></title>

  <!-- Bootstrap CSS -->
  <link href="../vendor/css/bootstrap/bootstrap.min.css" rel="stylesheet">
  <!-- Font Awesome CSS -->
  <link href="../vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
  <!-- Custom CSS -->
  <link href="../css/tampilanadmin.css" rel="stylesheet">
</head>
<body>

  <!-- Menu -->
  <div id="wrapper">
    <nav class="navbar navbar-default navbar-static-top" role="navigation" style="margin-bottom: 0">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="sr-only">Toggle navigation</span> Menu <i class="fa fa-bars"></i>
        </button>
        <a class="navbar-brand">Inventory</a>
      </div>
      <?php 
        $id = $_SESSION['idinv'];
        include '../koneksi.php';
        $sql = "SELECT * FROM tb_admin WHERE id_admin = '$id'";
        $query = mysqli_query($koneksi, $sql);
        $r = mysqli_fetch_array($query);
      ?>
      <ul class="nav navbar-top-links navbar-right">
        <li class="dropdown">
          <a class="dropdown-toggle" data-toggle="dropdown" href="#">
            <img src="../images/admin/<?php echo $r['foto']; ?>" height="50"></i> <?php echo $r['nama']; ?>
          </a>
          <ul class="dropdown-menu dropdown-user">
            <li>
              <form class="" action="logout.php" onclick="return confirm('Yakin ingin logout?');" method="post">
                <button class="btn btn-default" type="submit" name="keluar"><i class="fa fa-sign-out"></i> Logout</button>
              </form>
            </li>
          </ul>
        </li>
      </ul>

      <!-- Menu samping -->
      <div class="navbar-default sidebar" role="navigation">
        <div class="sidebar-nav navbar-collapse">
          <ul class="nav" id="side-menu">
            <li>
              <a href="?m=awal.php">
                <i class="fa fa-dashboard"></i> Beranda
              </a>
            </li>
            <li>
              <a href="?m=admin&s=awal">
                <i class="fa fa-user"></i> Data Admin
              </a>
            </li>
            <li>
              <a href="?m=petugas&s=awal">
                <i class="fa fa-users"></i> Data Petugas
              </a>
            </li>
            <li>
              <a href="?m=supplier&s=awal">
                <i class="fa fa-building"></i> Data Supplier
              </a>
            </li>
            <li>
              <a href="?m=rak&s=awal">
                <i class="fa fa-cubes"></i> Data Rak
              </a>
            </li>
            <li>
              <a href="?m=barang&s=awal">
                <i class="fa fa-archive"></i> Data Barang
              </a>
            </li>
            <li>
              <a href="?m=barangKeluar&s=awal">
                <i class="fa fa-cart-arrow-down"></i> Data Barang Keluar
              </a>
            </li>
            <li>
              <a href="logout.php" onclick="return confirm('Yakin ingin logout?')">
                <i class="fa fa-warning"></i> Logout
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <!-- Konten Utama -->
    <div id="page-wrapper">
      <div class="row">
        <div class="col-lg-12">
          <h1 class="page-header">Data Barang</h1>
        </div>
      </div>

      <!-- Tombol trigger modal -->
      <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalCenter">
        Tambah data
      </button>

      <!-- Modal -->
      <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
        <!-- Konten Modal -->
      </div>

      <!-- Form Cari Barang -->
      <div class="row">
        <center>
          <form action="" method="POST">
            <label>Cari Barang</label>
            <input type="text" name="cari"> <button type="submit" name="go" class="btn btn-success">Cari Barang</button>
          </form>
        </center>
      </div>

      <!-- Tabel Data Barang -->
      <div class="row">
        <div class="table-responsive table--no-card m-b-30">
          <table class="table table-borderless table-striped table-earning">
            <thead>
              <tr>
                <th>Kode Barang</th>
                <th>Nama Barang</th>
                <th>Stok</th>
                <th>Rak</th>
                <th>Supplier</th>
                <th>Aksi</th>
              </tr>
            </thead>
            <tbody>
              <?php 
                include 'paging.php';
              ?>
            </tbody>
          </table>
          <!-- Pagination -->
          <center>
            <ul class="pagination justify-content-center">
              <li class="page-item">
                <a class="page-link" <?php if ($halaman > 1) { echo "href='?m=barang&s=awal&halaman=$previous'"; } ?>>Previous</a>
              </li>
              <?php 
                for ($x = 1; $x <= $total_halaman; $x++) {
              ?> 
                <li class="page-item"><a class="page-link" href="?m=barang&s=awal&halaman=<?php echo $x ?>"><?php echo $x; ?></a></li>
              <?php
                }
              ?>              
              <li class="page-item">
                <a  class="page-link" <?php if ($halaman < $total_halaman) { echo "href='?m=barang&s=awal&halaman=$next'"; } ?>>Next</a>
              </li>
            </ul>
          </center> 
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="text-center">
      <div class="footer-below">
        <div class="container">
          <div class="row">
            <div class="col-lg-12">
              <p class="text-muted" style="font-size: 16px;">Copyright &copy; <script>document.write(new Date().getFullYear());</script> Angelita Salsabila Afifah. All rights reserved</p>
            </div>
          </div>
        </div>
      </div>
    </footer>

    <!-- jQuery -->
    <script src="../vendor/jquery/jquery.min.js"></script>
    <!-- Bootstrap JavaScript -->
    <script src="../vendor/css/js/bootstrap.min.js"></script>

  </body>
</html>
