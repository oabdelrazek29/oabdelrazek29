"""Render the original android avatar as real SVG binary typography."""
from pathlib import Path
from PIL import Image, ImageOps, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
source = Image.open(ROOT / 'assets/android-avatar.jpg').convert('RGB')


def android(x, y, size):
    cols, rows = 116, 78
    gray = ImageOps.autocontrast(ImageOps.grayscale(source), cutoff=1)
    gray = gray.resize((cols, rows), Image.Resampling.LANCZOS)
    edge = gray.filter(ImageFilter.FIND_EDGES)
    color = source.resize((cols, rows), Image.Resampling.LANCZOS)
    dx, dy = size / cols, size / rows
    parts = [f'<g font-family="monospace" font-size="{dy * .94:.2f}" font-weight="600" text-anchor="middle">']
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            v = gray.getpixel((col, row))
            e = edge.getpixel((col, row))
            ink = max((235 - v) / 220, e / 330)
            if ink < .12:
                continue
            r, g, b = color.getpixel((col, row))
            fill = '#367b73' if g > r * 1.08 and g > b * .98 else '#202b2a'
            opacity = min(.98, max(.17, ink * 1.65))
            digit = '1' if (col * 17 + row * 31) % 7 < 3 else '0'
            parts.append(f'<text x="{x + col * dx:.2f}" y="{y + row * dy:.2f}" fill="{fill}" opacity="{opacity:.2f}">{digit}</text>')
    parts.append('</g>')
    return '\n'.join(parts)


head = '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="600" viewBox="0 0 1200 600" role="img" aria-labelledby="title desc">'
art = head + '''
<title id="title">Omar — from a sketch to a working system</title>
<desc id="desc">A futuristic android portrait composed entirely of zeroes and ones, with numbered engineering annotations on ivory paper.</desc>
<rect width="1200" height="600" rx="20" fill="#f4f1e8"/>
<g stroke="#367b73" fill="none" opacity=".15">
<path d="M32 40h1136M32 560h1136M560 40v520"/>
<circle cx="900" cy="295" r="245" stroke-dasharray="3 7"/>
</g>
<g fill="#367b73" font-family="monospace" font-size="17" letter-spacing="2">
<text x="48" y="79">OMAR / 029</text>
<text x="48" y="535">SCIENCE · SOFTWARE · DESIGN</text>
</g>
<g fill="#202b2a" font-family="Georgia, serif" font-size="76">
<text x="46" y="214">From a sketch</text>
<text x="46" y="300">to a working</text>
<text x="46" y="386" font-style="italic">system.</text>
</g>
<path d="M48 436h64" stroke="#367b73" stroke-width="4"/>
<text x="48" y="478" fill="#65736e" font-family="monospace" font-size="19">MIRA / ARC</text>
'''
art += android(591, 36, 540)
art += '''
<g stroke="#367b73" fill="none" stroke-width="1.2"><path d="M1090 92h58v57M640 462h-35v48"/><circle cx="1090" cy="92" r="3"/><circle cx="640" cy="462" r="3"/></g>
<g fill="#367b73" font-family="monospace" font-size="15"><text x="1128" y="80">01</text><text x="590" y="533">02</text><text x="1055" y="565">01001111</text></g>
</svg>'''
(ROOT / 'assets/android-binary.svg').write_text(art)
print(f'Created android-binary.svg ({len(art):,} bytes)')
