#!/usr/bin/perl

use strict;
use CGI ':standard';

my $name = param('name');
my @greet = ("Good morning", "Good afternoon", "Good night", "Good evening");

print
header(),
start_html('8A'),
"Hello $name. $greet[int(rand(4))]!",
end_html();

