/*
 * This file initializes the main Materialize components, so they can work properly.
 */

// Auto initializer, for components that don't need additional configuration
M.AutoInit()

// Initialize the home page carousel, to display multiple pictures
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.carousel')
  var instances = M.Carousel.init(elems, {
    fullWidth: true,
    indicators: true,
    duration: 3000
  })
})
