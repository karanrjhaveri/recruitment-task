<?php
require_once __DIR__ . '/vendor/autoload.php';
use Symfony\Component\Yaml\Parser;

error_reporting(E_ALL ^ E_NOTICE and E_ALL); # Do not print Notices

//echo $argc;
if($argc > 3 or $argc < 2) {
	fwrite(STDERR,'ERROR: Invalid Arguments Provided. Try Again!');
	exit(1);
}

$input = explode('=', $argv[1])[1];
if($argc==3) {
	$output = explode('=', $argv[2])[1];
}
$sum=0;

$in_loc = explode('/',$input)[0]; # data
$out_loc = explode('/',$output)[0]; # results
$in_file = explode('/',$input)[1]; # e.g. file.csv 
$out_file = explode('/',$output)[1]; # results.txt
$in_type = explode('.',$in_file)[1]; # csv or xml or yml
$in_loc = dirname(__DIR__).'\\'.$in_loc.'\\'.$in_file; # exact in-path
$out_loc = dirname(__DIR__).'\\'.$out_loc.'\\'.$out_file; # exact out-path

if($in_type=='csv') {
	$data = array_map("str_getcsv", file($in_loc,FILE_SKIP_EMPTY_LINES));
	array_shift($data); # remove 'values' title
	foreach ($data as $i=>$row) {
		$sum+=(int)$data[$i][2]; # access [row][column]
	}
}elseif($in_type=='xml') {
	$data = simplexml_load_file($in_loc);
	for ($i = 0; $i < count($data->user); $i++) {
		$sum+=(int)$data->user[$i]->value;
	}
}elseif($in_type=='yml') {
	$yaml = new Parser();
	try {
		$data = $yaml->parse(file_get_contents($in_loc));
	} catch (ParseException $e) {
		printf("Unable to parse the YAML string: %s", $e->getMessage());
	}
	foreach($data['users'] as $usr=>$val) {
		$sum+=(int)$val['value'];
	}
}
if($argc==2) {
	echo $sum;
} else {
	$of = fopen($out_loc, 'w');
	fwrite($of, $sum);
	fclose($of);
}
?> 