var topLayer = "layer1";
var currentZ = 5;

function stack(toTop){
  var oldTop = document.getElementById(topLayer).style;
  var newTop = document.getElementById(toTop).style;
  newTop.zIndex = currentZ++;
  top = toTop;
}