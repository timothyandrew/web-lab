<?
  if(isset($_COOKIE['DateVisit'])){
    $last_visit = $_COOKIE['DateVisit'];
  }
  
  date_default_timezone_set('Asia/Calcutta');
  $d = getdate();
  $datestring = "$d[mday]-$d[month]-$d[year] $d[hours]:$d[minutes]:$d[seconds]";
  setcookie("DateVisit", $datestring);

  print "Last visited at $last_visit";
?>