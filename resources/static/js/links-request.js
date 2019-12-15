/*
 * This file makes a request to the links so they can be displayed on the home page.
 */

function requestembed(source) {
  var destination = document.getElementById(source);
  var req = new XMLHttpRequest();
  req.open('GET', '/page/embed/'+source, true);
  req.onreadystatechange = function (aEvt) {
    if (req.readyState == 4 && req.status == 200) {
      destination.innerHTML = req.responseText;
    }
  };
  req.send(null);
}