#!/usr/bin/perl

use strict;
use CGI ':standard';

my @t = localtime(time);
my $ampm = 'AM';

if($t[2] > 12){
  $t[2] = $t[2] - 12;
  $ampm = 'PM';
}

print
header(),
start_html('9'),
"$t[2]:$t[1]:$t[0] $ampm",
end_html();