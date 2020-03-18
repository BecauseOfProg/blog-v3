window.lazyLoad = lazyLoad
function lazyLoad (selector) {
  let $lazy = typeof selector === 'string' ? [...document.querySelectorAll(selector)] : [...selector]

  window.addEventListener('DOMContentLoaded', () => {
    console.log('LazyLoad : DOMContentLoaded', $lazy.length)
  })

  $lazy = $lazy.filter(el => !(isScrolledIntoView(el) && applyLazy(el)))

  let lastCheck
  window.onscroll = function (e) {
    if (lastCheck && ($lazy.length === 0 || lastCheck > Date.now() - 50)) return
    lastCheck = Date.now()
    $lazy = $lazy.filter(el => !(isScrolledIntoView(el) && applyLazy(el)))
  }

  function applyLazy (el) {
    const imageUrl = el.getAttribute('lazy')
    if (el instanceof window.HTMLImageElement) {
      el.setAttribute('src', imageUrl)
    } else {
      el.style.backgroundImage = `url(${imageUrl})`
    }
    return true
  }

  function isScrolledIntoView (el) {
    var rect = el.getBoundingClientRect()
    var isVisible = (rect.top >= 0) && (rect.bottom <= (window.innerHeight + rect.height))
    return isVisible
  }
}
lazyLoad('[lazy]')
/*
 * This file contains all the sharing options.
 */

// The link copying sharing option
function copyTextToClipboard(text) {
  let textArea = document.createElement('textarea');

  textArea.style.position = 'fixed'
  textArea.style.top = 0
  textArea.style.left = 0

  textArea.style.width = '2em'
  textArea.style.height = '2em'
  textArea.style.padding = 0

  textArea.style.border = 'none'
  textArea.style.outline = 'none'
  textArea.style.boxShadow = 'none'

  textArea.style.background = 'transparent'
  textArea.value = text

  document.body.appendChild(textArea)

  textArea.select()

  try {
    let successful = document.execCommand('copy')
    let msg = successful ? 'successful' : 'unsuccessful'
    console.log(`Copying text command was ${msg}`)
    M.toast({ html: 'Copié dans le presse-papier !' })

    $('.fixed-action-btn').closeFAB()
    Materialize.toast('Lien copié dans le presse-papier !', 4000, 'rounded')
  }
  catch (err) {
    console.log(`Erreur : impossible de copier dans le presse papier : ${err}`);
  }
  document.body.removeChild(textArea)
}
function CopyLink() {
  copyTextToClipboard(location.href)
}

// Using the Web Share API to share page on mobile devices
(() => {
    const webShareTestEl = document.querySelector('.web-share')

    // CHECK IF SHARE IS AVAILABLE
    if (!navigator.share) {
      document.addEventListener('DOMContentLoaded', function() {
        let elements = document.querySelectorAll('.fixed-action-btn')
        M.FloatingActionButton.init(elements)
      })
      return
    }

    let resetTimeout

    // METHODS
    const resetButton = () => {
        clearTimeout(resetTimeout)
        resetTimeout = setTimeout(() => {
            webShareTestEl.children[0].innerText = 'share'
        }, 1000)
    }

    const getOpenGraphData = function (property) {
        return document.querySelector(`meta[property="${property}"]`).getAttribute('content')
    }

    const sharePage = () => {
        navigator.share({
            title: getOpenGraphData('og:title'),
            text: getOpenGraphData('og:description'),
            url: getOpenGraphData('og:url')
        }).then(() => {
            webShareTestEl.children[0].innerText = 'done'
            resetButton()
        })
            .catch(error => {
                console.log(`Error sharing : ${error}`);

                webShareTestEl.children[0].innerText = 'error'
                resetButton()
            })
    }

    // EVENTS
    webShareTestEl.addEventListener('click', sharePage)
})()
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
});
/*
 * This file makes a request to the links so they can be displayed on the home page.
 */

function requestembed(source) {
  var destination = document.getElementById(source);
  if (destination != null) {
    var req = new XMLHttpRequest();
    req.open('GET', '/page/embed/'+source, true);
    req.onreadystatechange = function (aEvt) {
      if (req.readyState == 4 && req.status == 200) {
        destination.innerHTML = req.responseText;
      }
    };
    req.send(null);
  };
}

var handler = function(event) {
  requestembed('links');
  removeEventListener('scroll', handler, false);
};

window.addEventListener('scroll', handler, false);
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
})

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.tab-reseauxsociaux');
  var instances = M.Tabs.init(elems, {onShow: function(elems) {
    var elem = document.getElementById('tab-reseauxsociaux');
    var instance = M.Tabs.getInstance(elem);
    var active_tab = instance.$activeTabLink[0];
    var to_embed = active_tab.innerText;
    requestembed(to_embed.toLowerCase());
  }});
});


// Auto initializer, for components that don't need additional configuration
M.AutoInit()
/*
 * This file is the service worker : it makes an offline copy of pages.
 */

if (navigator.serviceWorker.controller) {
  console.log('[PWA Builder] active service worker found, no need to register')
} else {
  // Register the ServiceWorker
  navigator.serviceWorker
    .register('/pwabuilder-sw.js',  {
      scope: './'
    })
    .then(function(reg) {
      console.log('Service worker has been registered for scope: ' + reg.scope)
    })
}
