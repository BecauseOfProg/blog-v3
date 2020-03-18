/*
 * This file initializes the main Materialize components, so they can work properly.
 */

// Initialize the home page carousel, to display multiple pictures
document.addEventListener('DOMContentLoaded', function() {
  let carousel = document.querySelectorAll('.carousel')
  let carouselInstance = M.Carousel.init(carousel, {
    fullWidth: true,
    indicators: true
  })

  let tooltip = document.querySelectorAll('.account-button .tooltipped')
  let tooltipInstance = M.Tooltip.init(tooltip, {
    margin: 0
  })

  var elems = document.querySelectorAll('.sidenav')
  var instances = M.Sidenav.init(elems)

  // Auto initializer, for components that don't need additional configuration
  M.AutoInit()
})
