/*
 * This file initializes the main Materialize components, so they can work properly.
 * It also enables the search bar.
 */

document.addEventListener("DOMContentLoaded",function(){

  let searchBarContainer = document.getElementById('search-field-container')
  let navbarLinksContainer = document.getElementById('navbar-links-container')

  document.getElementById('search-field-open').addEventListener('click', () => {
    searchBarContainer.className = 'col s12'
    navbarLinksContainer.className = 'hide'
  })

  document.getElementById('search-field-close').addEventListener('click', () => {
    searchBarContainer.className = 'hide'
    navbarLinksContainer.className = ''
  })

  // Initialize the home page carousel, to display multiple pictures
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
});