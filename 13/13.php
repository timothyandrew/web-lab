<?php

  $id    = $_POST['id'];
  $name  = $_POST['name'];
  $addr1 = $_POST['addr1'];
  $addr2 = $_POST['addr2'];
  $email = $_POST['email'];
  $sname = $_POST['sname'];

  mysql_connect('localhost','root', 'root');
  mysql_select_db("student") or die("Unable to select database");

  $insertquery="INSERT INTO personinfo VALUES('$id','$name','$addr1','$addr2','$email')";
  mysql_query($insertquery);

  $selectquery="SELECT * FROM personinfo where Name='$sname'";
  $result = mysql_query($selectquery);
  $numrows=mysql_numrows($result);
  
  print "<table border size=1> <tr><th>ID</th><th>Name</th> 
  <th>Address1</th><th>Address2</th><th>Email</th></tr>";
  $rownum=0;
  while($rownum<$numrows)
  { 
     $row=mysql_fetch_array($result);
     print "<tr><td>".$row['ID']."</td><td>".$row['Name']."</td> 
     <td>".$row['Address1']."</td><td>".$row['Address2']."</td>
     <td>".$row['email']."</td></tr>";
     $rownum++;
  }
  print "</table>";
  mysql_close();
?>
