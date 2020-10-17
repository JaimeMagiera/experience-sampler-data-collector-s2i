#!/usr/bin/perl -ws                                                                       
# This cgi script parses the submission.

# Read the DATA_DIR environment variable to construct the path for data files to be written to.
$datadir =  $ENV{'DATA_DIR'};

# Read the QUERY_STRING environment variable into a buffer for parsing.
$buffer = $ENV{'QUERY_STRING'}; 

# Parse the query string into key/value pairs 
@pairs = split(/&/, $buffer); 
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
print "Content-type:text/html\r\n\r\n"; 
print "<html>"; 
print "<head>"; 
print "<title>Experience Sampler</title>"; 
print "</head>"; 
print "<body>"; 
print "Thank you. You are participant $id.";
print "</body>"; 
print "</html>";

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
