document.addEventListener("DOMContentLoaded",function() {
  let theme = localStorage.getItem('theme')
  if (theme === undefined) {
    localStorage.setItem('theme', 'auto')
    setPreferredColorScheme('auto')
  } else {
    setPreferredColorScheme(theme)
  }
})

function setPreferredColorScheme(mode) {
  let rule
  for (let i = document.styleSheets[2].rules.length-1; i >= 0; i--) {
    rule = document.styleSheets[2].rules[i].media;
    if (rule !== undefined) {
      if (rule.mediaText.includes('prefers-color-scheme')) {
        switch (mode) {
          case 'light':
            localStorage.setItem('theme', 'light')
            rule.appendMedium('original-prefers-color-scheme')
            if (rule.mediaText.includes('light')) rule.deleteMedium('(prefers-color-scheme: light)')
            if (rule.mediaText.includes('dark')) rule.deleteMedium('(prefers-color-scheme: dark)')
            break
          case 'dark':
            localStorage.setItem('theme', 'dark')
            rule.appendMedium('(prefers-color-scheme: dark)')
            if (rule.mediaText.includes('light')) rule.deleteMedium('(prefers-color-scheme: light)')
            if (rule.mediaText.includes('original')) rule.deleteMedium('original-prefers-color-scheme')
            break
          default:
            localStorage.setItem('theme', 'auto')
            rule.appendMedium('(prefers-color-scheme: dark)')
            if (rule.mediaText.includes('light')) rule.deleteMedium('(prefers-color-scheme: light)')
            if (rule.mediaText.includes('original')) rule.deleteMedium('original-prefers-color-scheme')
        }
        break
      }
    }
  }
}
