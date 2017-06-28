<?php
echo 'Test to determine if script gives a valid result:'."\n\n";
$cmds = array(
	'php script.php --input="data/file.csv"',
	'php script.php --input="data/file.xml"',
	'php script.php --input="data/file.yml"'
	);
foreach($cmds as $cmd) {
	$output = shell_exec($cmd);
	if((int)$output==1000) {
		echo $cmd.' --> Success !'."\n";
	} else {
		echo $cmd.' --> Failed. Invalid Result!'."\n";
	}
}
?>