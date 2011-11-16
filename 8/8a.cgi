#!/usr/bin/perl

use strict;
use CGI ':standard';

my $name = param('name');
my $greet = param('greet');

print
header(),
start_html('8A'),
"Hello $name. $greet!",
end_html();

