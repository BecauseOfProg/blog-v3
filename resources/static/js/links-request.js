/*
 * This file makes a request to the links so they can be displayed on the home page.
 */

function request() {
  var req = new XMLHttpRequest();
  req.open('GET', '/page/links-embed', true);
  req.onreadystatechange = function (aEvt) {
    if (req.readyState == 4 && req.status == 200) {
      display.innerHTML = req.responseText;
    }
  };
  req.send(null);
}
window.onload = request()