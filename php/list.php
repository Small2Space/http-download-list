<html>
  <head>
    <title>
    DL list  
    </title>
  </head>
  <body>
    <h1>List</h1>
    <?php
      $dir_path = "/var/www/html/list/";
      $files = scandir($dir_path, SCANDIR_SORT_DESCENDING);
      foreach($files AS $f_name){
    		?>
        <p><a href="/list/<?php echo $f_name; ?>">
        <?php echo $f_name; ?>
        </a></p>
    <?php
    	}
    ?>
  </body>
</html>
