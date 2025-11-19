<html>
  <head>
    <title>
    DL list  
    </title>
  </head>
  <body>
    <h1>Files</h1>
    <h2>Latest</h2>
    <p><a href="/latest.php">Download Latest</a></p>
    <h2>List</h2>
    <?php
      $dir_path = "/var/www/html/list/";
      $files = scandir($dir_path, SCANDIR_SORT_DESCENDING);
      foreach($files AS $f_name){
    		?>
        <p><a href="/list/<?php echo $f_name; ?>">
        <?php echo $f_name; ?> - <?php filemtime($dir_path.$f_name); ?>
        </a></p>
    <?php
    	}
    ?>
  </body>
</html>
