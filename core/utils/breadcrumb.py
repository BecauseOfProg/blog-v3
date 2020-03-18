def breadcrumb(links):
  breadcrumb = '<p class="bop-breadcrumb"> \
                  <a href="/" class="black-text">BecauseOfProg</a>'

  for link in links:
    breadcrumb += '<i class="material-icons"><span class="iconify" data-icon="mdi-chevron-right"></span></i> \
                   <a href="#" class="black-text">%s</a>' % (link)

  breadcrumb += '</p>'

  return breadcrumb