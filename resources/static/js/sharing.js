/*
 * This file contains all the sharing options.
 */

// The link copying sharing option
function copyTextToClipboard(text) {
  var textArea = document.createElement("textarea");

  textArea.style.position = 'fixed';
  textArea.style.top = 0;
  textArea.style.left = 0;

  textArea.style.width = '2em';
  textArea.style.height = '2em';
  textArea.style.padding = 0;

  textArea.style.border = 'none';
  textArea.style.outline = 'none';
  textArea.style.boxShadow = 'none';

  textArea.style.background = 'transparent';
  textArea.value = text;

  document.body.appendChild(textArea);

  textArea.select();

  try {
    var successful = document.execCommand('copy');
    var msg = successful ? 'successful' : 'unsuccessful';
    console.log('Copying text command was ' + msg);
    M.toast({html: 'Copié dans le presse-papier !'})

    $('.fixed-action-btn').closeFAB();
    Materialize.toast('Lien copiÃ© dans le presse-papier !', 4000, 'rounded');
  }
  catch (err) {
    console.log('Oops, unable to copy');
  }
  document.body.removeChild(textArea);
}
function CopyLink() {
  copyTextToClipboard(location.href);
}

// Using the Web Share API to share page on mobile devices
(() => {
    const webShareTestEl = document.querySelector('.web-share');

    // CHECK IF SHARE IS AVAILABLE
    if (!navigator.share) {
      document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('.fixed-action-btn');
        var instances = M.FloatingActionButton.init(elems);
      });
      return;
    }

    let resetTimeout;

    // METHODS
    const resetButton = () => {
        clearTimeout(resetTimeout);
        resetTimeout = setTimeout(() => {
            webShareTestEl.children[0].innerText = 'share';
        }, 1000);
    };

    const getOpenGraphData = function (property) {
        return document.querySelector(`meta[property="${property}"]`).getAttribute('content')
    };

    const sharePage = () => {
        navigator.share({
            title: getOpenGraphData('og:title'),
            text: getOpenGraphData('og:description'),
            url: getOpenGraphData('og:url')
        }).then(() => {
            webShareTestEl.children[0].innerText = 'done';
            resetButton();
        })
            .catch(error => {
                console.log('Error sharing:', error);

                webShareTestEl.children[0].innerText = 'error';
                resetButton();
            });
    };

    // EVENTS
    webShareTestEl.addEventListener('click', sharePage);
})();
