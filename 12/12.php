<?php 
  session_start(); 
  if(isset($_SESSION['count'])){ 
         print "Your session count: ";
         print $_SESSION['count'];
         print "<br>"; 
         $_SESSION['count']++; 
  } else { 
         $_SESSION['count'] = 1; 
         print "Session does not exist"; 
  } 
?> 
