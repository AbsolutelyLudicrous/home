<?php 
	if(file_exists('/usr/local/www/apache24/lockfiles/WEBSERVER_DEBUGGING')){
		phpinfo();
	}else{
		echo('The webserver currently has this function disabled.');
	}
?>
