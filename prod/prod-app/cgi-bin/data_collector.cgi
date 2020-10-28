#!/usr/bin/perl -ws
# This cgi script parses the submission.

# Read the DATA_DIR environment variable to construct the path for data files to be written to.
$datadir =  $ENV{'DATA_DIR'};

# Get the request method.
$request_method = $ENV{'REQUEST_METHOD'};

# Read the data into a buffer for parsing, accounting for both GET and POST request methods.
if ($request_method eq "GET") {
          $form_info = $ENV{'QUERY_STRING'};
} else {
      $size_of_form_information = $ENV{'CONTENT_LENGTH'};
      read (STDIN, $form_info, $size_of_form_information);
}

# Parse the query string into key/value pairs 
@pairs = split(/&/, $form_info); 
foreach $pair (@pairs)  
{ 
    ($name, $value) = split(/=/, $pair); 
    $value =~ tr/+/ /; 
    $value =~ s/%([a-fA-F0-9] [a-fA-F0-9])/pack("C", hex($1))/eg; 
    $value =~ s/~!/ ~!/g; 
    $FORM{$name} = $value; 
} 

# Get the participant id from the form values. This will be used in the submission response and in constructing the data file name.
$id = $FORM{'participant_id'};

# Generate an HTML reponse to the submission. 

$response_content = "<html>";
$response_content .= "<head>"
$response_content .= "<title>Experience Sampler</title>";
$response_content .= "</head>";
$response_content .= "<body>";
$response_content .= "Thank you. You are participant $id.";
$response_content .= "</body>";
$response_content .= "</html>";

print "HTTP/1.0 200 OK", "\n\n";
print "Content-type: text/html", "\n\n";
print $response_content;


# Construct the data file name.
my $filename = "participant_${id}_data.csv";

# Construct the data file path.
my $filepath = $datadir . "/" . $filename;

# Open a file handle to write the data.
open( OUTFILE, ">>", $filepath) or die $!, "Couldn\'t open outfile for writing!\n";

# Write the pause_time key and value
print OUTFILE "pause_time\t$FORM{'pause_time'}\n";

# Iterate through the remaining keys, writing each with its associated value into the data file.
foreach $key (keys %FORM)
{
	if (($key ne 'participant_id') && ($key ne 'pause_time')) {
               print OUTFILE "${key}\t";
	       print OUTFILE "$FORM{$key}";
	       print OUTFILE "\n";
       }       
}

# Close the file handle
close( OUTFILE );

# End the script
1;
