window.onload = () => {

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
}
