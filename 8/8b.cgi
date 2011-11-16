#!/usr/bin/perl

use strict;
use CGI ':standard';

my $count;
my $line;
open(FH, '<', 'log.txt') or die "can't open";

while(<FH>){
  $count = $_; # $_ is automatically set to the current line.
}

close(FH);
$count++;

open(FH, '>', 'log.txt') or die "can't open";
print FH $count;
close(FH);

print
header(),
start_html('8B'),
"You are user $count.",
end_html();