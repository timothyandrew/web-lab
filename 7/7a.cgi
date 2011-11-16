#!/usr/bin/perl

use strict;
use CGI':standard';

print
header(),
start_html(),
"<h1>Server Info</h1>",
#%ENV,
"<strong>Server Name: </strong>", $ENV{SERVER_NAME},
br(),
"<strong>Server Software: </strong>", $ENV{SERVER_SOFTWARE},
br(),
"<strong>Server Protocol: </strong>", $ENV{SERVER_PROTOCOL},
br(),
"<strong>CGI Version: </strong>", $ENV{GATEWAY_INTERFACE},
br(), br(),
hr(),
"<h3>Other Info</h3>",
%ENV, #Print all environment variables
end_html();
