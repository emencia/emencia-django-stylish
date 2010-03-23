"""Utils for emencia.django.stylish"""
from BeautifulSoup import BeautifulSoup, Tag

def apply_styles(source, styles):
    """Apply styles to source"""
    soup = BeautifulSoup(source)

    for style in styles:
        for markup in soup.findAll(style.markup):
            markup['style'] = style.style.strip()

    return soup.prettify()

