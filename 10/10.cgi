#! /usr/bin/perl

use CGI ':standard';
use DBI;

print header();
print start_html('SQL');

$dbh = DBI->connect("dbi:mysql:student:localhost:3306","root","root");
print 'Connected';
$name=param("name");
$age=param("age");
$qh=$dbh->prepare("insert into user values('$name','$age')");
$qh->execute();
$qh=$dbh->prepare("Select * from user");
$qh->execute();

print "Table info: <br>";
print "<table border size=1><tr><th>Name</th><th>Age</th></tr>";

while ( ($name,$age)=$qh->fetchrow()){ 
       print "<tr><td>$name</td><td>$age</td></tr>";
}

print "</table>";
$qh->finish();
$dbh->disconnect();
print"</HTML>";
