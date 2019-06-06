/*
 * This file initializes the main Materialize components, so they can work properly.
 */

// Initialize the parallax
document.addEventListener('DOMContentLoaded', function() {
  var parallax_elem = document.querySelectorAll('.parallax');
  var instances = M.Parallax.init(parallax_elem);
});

// Initialize the modal window
document.addEventListener('DOMContentLoaded', function() {
  var modal_elem = document.querySelectorAll('.modal');
  var instances = M.Modal.init(modal_elem);
});

// Initialize the home page carousel, to display multiple pictures
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.carousel');
  var instances = M.Carousel.init(elems, {
    fullWidth: true,
    indicators: true
  });
});

// Initialize the share button, located at the bottom-right of the website
// Disabled : other share options took place
// document.addEventListener('DOMContentLoaded', function() {
//   var elems = document.querySelectorAll('.fixed-action-btn');
//   var instances = M.FloatingActionButton.init(elems);
// });

// Initialize the collapsible part, to display one paragraph at a time
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.collapsible');
  var instances = M.Collapsible.init(elems);
});

// Initialize the sidenav, displayed when navigating on small devices
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems);
});

// Initialize the select field in forms
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);
});

