"""Build self-contained SVG covers for GitHub's image renderer."""
from pathlib import Path
from math import sin, cos, pi

ROOT = Path(__file__).resolve().parents[1]

def cover(name, number, subtitle, drawing):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="440" viewBox="0 0 1000 440" role="img" aria-labelledby="title desc">
<title id="title">{name} / {subtitle}</title>
<desc id="desc">Engineering sketchbook project cover in graphite and muted teal on ivory.</desc>
<defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#367b73" stroke-opacity=".045"/></pattern></defs>
<rect width="1000" height="440" rx="18" fill="#f4f1e8"/>
<rect width="1000" height="440" rx="18" fill="url(#grid)"/>
<path d="M32 36H968M32 404H968M510 36V404" stroke="#367b73" stroke-opacity=".2" fill="none"/>
<text x="42" y="80" font-family="monospace" font-size="21" letter-spacing="2" fill="#367b73">FIELD NOTES / {number}</text>
<text x="38" y="226" font-family="Georgia,serif" font-size="114" fill="#202b2a">{name}</text>
<path d="M42 263H104" stroke="#367b73" stroke-width="3"/>
<text x="42" y="316" font-family="Georgia,serif" font-size="30" fill="#202b2a">{subtitle}</text>
<text x="42" y="379" font-family="monospace" font-size="19" letter-spacing="1" fill="#536b64">OMAR ABDELRAZEK</text>
{drawing}
</svg>'''

mira = '<g fill="none" stroke="#202b2a">'
for radius in (64,68,100,146):
    mira += f'<ellipse cx="748" cy="208" rx="{radius}" ry="{radius*.46}" transform="rotate(-28 748 208)" stroke-opacity=".35"/>'
mira += '<circle cx="748" cy="208" r="64"/><ellipse cx="748" cy="208" rx="23" ry="64"/><ellipse cx="748" cy="208" rx="64" ry="23"/>'
for t in range(-4,5):
    yy=208+t*11
    span=(64**2-(t*11)**2)**.5
    mira+=f'<path d="M{748-span:.1f} {yy}h{span*2:.1f}" stroke-opacity=".12"/>'
mira += '<path d="M815 120l45-38h62M671 245l-43 58h-52" stroke="#367b73"/><circle cx="815" cy="120" r="4" fill="#367b73"/><circle cx="671" cy="245" r="4" fill="#367b73"/></g><g fill="#367b73" font-family="monospace" font-size="20"><text x="885" y="72">01</text><text x="560" y="328">02</text><text x="625" y="378">IDEAS TAKE SHAPE</text></g>'

arc='<g fill="none" stroke="#202b2a" stroke-width="1.4"><path d="M600 257Q665 127 746 185Q824 111 908 226M600 257L672 307L746 185L831 306L908 226M600 257L746 185L908 226M672 307L831 306"/><path d="M582 348H928M590 105V354" stroke="#367b73" stroke-opacity=".2" stroke-dasharray="4 6"/></g>'
for x,y,n in [(600,257,'01'),(672,307,'02'),(746,185,'03'),(831,306,'04'),(908,226,'05')]:
    arc+=f'<circle cx="{x}" cy="{y}" r="12" fill="#f4f1e8" stroke="#367b73" stroke-width="2"/><circle cx="{x}" cy="{y}" r="4" fill="#367b73"/><text x="{x-12}" y="{y-24}" fill="#536b64" font-family="monospace" font-size="18">{n}</text>'
arc+='<text x="620" y="378" fill="#367b73" font-family="monospace" font-size="20">CONNECT THE CONCEPTS</text>'

for name,number,subtitle,drawing in [('MIRA','01','A workspace for discovery.',mira),('ARC','02','A clearer path to learning.',arc)]:
    path=ROOT/'assets'/f'{name.lower()}-cover.svg'
    path.write_text(cover(name,number,subtitle,drawing))
    print(path.name)
