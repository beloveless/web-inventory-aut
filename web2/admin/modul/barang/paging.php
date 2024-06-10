<script>
  // Variable untuk memastikan notifikasi hanya muncul satu kali
  var notificationDisplayed = false;

  function checkStockNotification(stok) {
    if (stok <= 20 && !notificationDisplayed) {
      alert('Periksa stok Anda, hampir habis!');
      // Gantilah dengan tampilan pop-up notifikasi yang lebih canggih jika diinginkan.
      notificationDisplayed = true; // Set notifikasi telah ditampilkan agar tidak tampil lagi
    }
  }
</script>

<?php
$batas = 5;
$halaman = isset($_GET['halaman']) ? (int)$_GET['halaman'] : 1;
$halaman_awal = ($halaman > 1) ? ($halaman * $batas) - $batas : 0;

$previous = $halaman - 1;
$next = $halaman + 1;

if (isset($_POST['go'])) {
    $cari = $_POST['cari'];
    $data_rak = mysqli_query($koneksi, "SELECT * FROM tb_barang WHERE nama_brg LIKE '%$cari%'");
} else {
    $data_rak = mysqli_query($koneksi, "SELECT * FROM tb_barang LIMIT $halaman_awal, $batas");
}

// Hitung total data
$total_data = mysqli_num_rows(mysqli_query($koneksi, "SELECT * FROM tb_barang"));

// Hitung total halaman
$total_halaman = ceil($total_data / $batas);

foreach ($data_rak as $row):
?>

  <tr>
    <td><?php echo $row['kode_brg']; ?></td>
    <td><?php echo $row['nama_brg']; ?></td>
    <td><?php echo $row['stok']; ?></td>
    <td><?php echo $row['rak']; ?></td>
    <td><?php echo $row['supplier']; ?></td>
    <td>
      <a href="index.php?m=barang&s=hapus&kode_brg=<?php echo $row['kode_brg'];?>" onclick="return confirm('Yakin Akan dihapus?')"><button class="btn btn-danger">Hapus</button></a>
      | <a href="index.php?m=barang&s=ubah&kode_brg=<?php echo $row['kode_brg'];?>" ><button class="btn btn-primary">Ubah</button></a>
    </td>
    <!-- Panggil fungsi JavaScript dengan stok barang sebagai parameter -->
    <script>checkStockNotification(<?php echo $row['stok']; ?>)</script>
  </tr>

<?php endforeach; ?>
