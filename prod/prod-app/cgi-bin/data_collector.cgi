#!/usr/bin/perl -ws                                                                       

my $datadir =  $ENV{'DATA_DIR'};
$buffer = $ENV{'QUERY_STRING'}; 
#split information into key/value pairs 
@pairs = split(/&/, $buffer); 
foreach $pair (@pairs)  
{ 
    ($name, $value) = split(/=/, $pair); 
    $value =~ tr/+/ /; 
    $value =~ s/%([a-fA-F0-9] [a-fA-F0-9])/pack("C", hex($1))/eg; 
    $value =~ s/~!/ ~!/g; 
    $FORM{$name} = $value; 
} 

my $id = $FORM{'participant_id'};
print "Content-type:text/html\r\n\r\n"; 
print "<html>"; 
print "<head>"; 
print "<title>GeeksForGeeks - Get Method</title>"; 
print "</head>"; 
print "<body>"; 
print "You are participant $id!";
print "</body>"; 
print "</html>";

# Create outfile for saving data
my $filename = "participant_${id}_data.csv";
my $filepath = $datadir . "/" . $filename;
open( OUTFILE, ">>", $filepath) or die $!, "Couldn\'t open outfile for writing!\n";
print OUTFILE "pause_time\t$FORM{'pause_time'}\n";

foreach $key (keys %FORM)
{
	if (($key ne 'participant_id') && ($key ne 'pause_time')) {
               print OUTFILE "${key}\t";
	       print OUTFILE "$FORM{$key}";
	       print OUTFILE "\n";
       }       
}

close( OUTFILE );

1;
