#!/usr/bin/env python3
"""Genera upsell2/index.html · Psicología Aplicada a la Vida (US$19,90). Uso: python3 src/build-upsell2.py ."""
import os, sys, runpy, tempfile
from html import escape as esc

OUT = sys.argv[1] if len(sys.argv) > 1 else "."
# Reutiliza estilos, scripts y bloques del primer upsell sin tocar sus archivos
_argv = sys.argv; sys.argv = ["x", tempfile.mkdtemp()]
L = runpy.run_path(os.path.join(os.path.dirname(__file__), "build-funnel.py"), run_name="lib")
sys.argv = _argv
CSS, JS, WIDGET, VIEWER, CLOCK = L["CSS"], L["JS"], L["WIDGET"], L["VIEWER"], L["CLOCK"]

A = "/upsell2/assets/"
GUIDES = [
    ("g01", "Psicología de la Persuasión e Influencia", "Los 7 principios que te hacen decir «sí» y cómo protegerte de la manipulación."),
    ("g02", "Lenguaje Corporal", "Mirada, gestos, postura y voz: lo que la ciencia confirma y lo que es mito."),
    ("g03", "Sesgos Cognitivos y Decisiones", "50 errores mentales del día a día y un método para decidir mejor."),
    ("g04", "Psicología del Dinero", "Por qué gastas como gastas y cómo ahorrar sin fuerza de voluntad."),
    ("g05", "Psicología del Consumidor y el Marketing", "Precios, tiendas, marcas e influencers: lo que hay detrás de cada compra."),
    ("g06", "Psicología Criminal", "Psicopatía, perfiles, testigos y confesiones falsas, más allá de las series."),
    ("g07", "Psicología de las Redes Sociales", "Comparación, FOMO, dopamina y un plan de 14 días para recuperar tu atención."),
    ("g08", "Psicología del Sueño y los Sueños", "Fases del sueño, por qué soñamos y cómo descansar mejor."),
    ("g09", "Psicología del Liderazgo y el Trabajo", "Motivación, equipos, jefes difíciles y prevención del burnout."),
    ("g10", "Psicología de la Crianza", "Vínculo, límites, rabietas, pantallas y adolescencia."),
    ("g11", "Psicología del Deporte y la Motivación", "Nervios, foco, visualización, estado de flujo y hábito de moverte."),
    ("g12", "Psicología de la Felicidad", "Lo que la ciencia del bienestar sabe sobre relaciones, gratitud y sentido."),
]
BONOS = [
    ("gb1", "Psicología del Color", "Qué transmiten los colores en marcas, diseño y espacios."),
    ("gb2", "Psicología de la Atracción", "Los experimentos clásicos sobre amistad, amor y cercanía."),
    ("gb3", "Retos de 21 Días", "Seis retos prácticos para aplicar todo lo aprendido."),
]
SAMPLES = [
    ("s01", "Sesgos de información", "Sesgos Cognitivos"), ("s02", "Reciprocidad", "Persuasión e Influencia"),
    ("s03", "La psicopatía, más allá de las películas", "Psicología Criminal"), ("s04", "El rostro y las emociones", "Lenguaje Corporal"),
    ("s05", "La psicología de los precios", "Consumidor y Marketing"), ("s06", "Qué ocurre cuando dormimos", "Sueño y Sueños"),
    ("s07", "¿Qué es la felicidad?", "Psicología de la Felicidad"), ("s08", "Las 36 preguntas", "Bono · Atracción"),
    ("s09", "Rabietas y emociones intensas", "Psicología de la Crianza"), ("s10", "Por qué cuesta dejar de deslizar", "Redes Sociales"),
]

EXTRA_CSS = r"""
.fan{position:relative;height:clamp(250px,62vw,380px);max-width:560px;margin:26px auto 0}
.fan img{position:absolute;bottom:0;width:clamp(120px,30vw,190px);border-radius:6px;box-shadow:0 14px 30px rgba(14,36,43,.35);transform-origin:bottom center}
.fan img:nth-child(1){left:2%;transform:rotate(-14deg)}
.fan img:nth-child(2){left:17%;transform:rotate(-7deg)}
.fan img:nth-child(3){left:50%;margin-left:calc(clamp(120px,30vw,190px)/-2);z-index:3;transform:translateY(-14px)}
.fan img:nth-child(4){right:17%;transform:rotate(7deg)}
.fan img:nth-child(5){right:2%;transform:rotate(14deg)}
.fan .count{position:absolute;z-index:4;left:50%;bottom:-14px;transform:translateX(-50%);background:var(--clay);color:#fff;font:800 13px/1 var(--body);padding:9px 14px;border-radius:999px;white-space:nowrap;box-shadow:0 6px 16px rgba(0,0,0,.2)}
.lib{padding:56px 0;background:var(--paper-2)}
.cgrid{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.cgrid li{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;display:flex;flex-direction:column}
.cgrid img{width:100%;aspect-ratio:520/735;object-fit:cover}
.cgrid .t{padding:10px 12px 12px}
.cgrid h3{font:700 15px/1.3 var(--body);color:var(--ink)}
.cgrid p{font-size:13px;color:var(--muted);margin-top:4px;line-height:1.45}
.cgrid .bono{position:relative}
.cgrid .bono::after{content:"BONO";position:absolute;top:8px;left:8px;background:var(--amber);color:var(--ink-deep);font:800 10.5px/1 var(--body);letter-spacing:.1em;padding:5px 8px;border-radius:999px}
.sub-h{font:700 13px/1 var(--body);letter-spacing:.14em;text-transform:uppercase;color:var(--clay);text-align:center;margin:30px 0 14px}
.card{width:min(64vw,240px)}
.card img{aspect-ratio:1000/1414}
.why2{padding:46px 0 10px}
.why2 ul{list-style:none;padding:0;margin:0 auto;max-width:720px;display:grid;gap:10px}
.why2 li{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px 14px 48px;position:relative;font-size:16px}
.why2 li::before{content:"✓";position:absolute;left:16px;top:13px;width:22px;height:22px;border-radius:50%;background:var(--ok);color:#fff;font-size:13px;font-weight:900;display:grid;place-items:center}
.pain2{background:var(--paper-2);padding:40px 0}
.pain2 h2{text-align:center}
.pain2 ul{list-style:none;padding:0;margin:20px auto 0;max-width:680px;display:grid;gap:10px}
.pain2 li{background:#fff;border:1px solid var(--line);border-radius:12px;padding:13px 16px 13px 44px;position:relative;font-size:16px}
.pain2 li::before{content:"✕";position:absolute;left:16px;top:12px;color:var(--clay);font-weight:900}
.turn2{text-align:center;margin:18px auto 0;max-width:640px;font:600 21px/1.35 var(--display);color:var(--ink)}
.turn2 em{color:var(--clay)}
.get{padding:42px 0 20px}
.glist{list-style:none;padding:0;margin:0 auto;max-width:960px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.glist li{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden;min-width:0}
.glist img{width:100%;aspect-ratio:1/1;object-fit:cover;display:block}
.glist div{min-width:0;padding:12px 14px 14px}
.glist h3{font:700 15px/1.3 var(--body);color:var(--ink)}
.glist p{font-size:13px;color:var(--muted);margin-top:2px;line-height:1.4}
.bt{display:inline-block;background:var(--amber);color:var(--ink-deep);font:800 10px/1 var(--body);letter-spacing:.08em;padding:4px 6px;border-radius:999px;vertical-align:middle;margin-left:4px}
.hero-media .ribbon{top:auto;bottom:16px}
@media (max-width:640px){.glist{grid-template-columns:repeat(2,1fr);gap:10px}.glist li:last-child:nth-child(odd){grid-column:span 2;flex-direction:row}.glist li:last-child:nth-child(odd) img{width:46%;flex:0 0 46%}.glist li:last-child:nth-child(odd) div{align-self:center}.glist div{padding:9px 10px 11px}.glist h3{font-size:13.5px}.glist p{font-size:12px}}
@media (max-width:860px){.cgrid{grid-template-columns:repeat(3,1fr)}}
@media (max-width:560px){.cgrid{grid-template-columns:repeat(3,1fr);gap:8px}.cgrid p{display:none}.cgrid .t{padding:7px 7px 9px}.cgrid h3{font-size:11.5px;line-height:1.25}.cgrid .bono::after{font-size:9px;padding:4px 6px;top:5px;left:5px}}
.hero{overflow:hidden}
"""

def card(f, t, c):
    return (f'<figure class="card"><button type="button" data-full="{A}{f}.webp" data-title="{esc(t)}" data-col="{esc(c)}" aria-label="Ampliar: {esc(t)}">'
            f'<img src="{A}{f}-t.webp" width="440" height="622" loading="lazy" decoding="async" draggable="false" alt="Página interior: {esc(t)}"></button>'
            f'<figcaption>{esc(t)}<small>{esc(c)}</small></figcaption></figure>')

def glist(items, bono=False):
    return "".join(f'<li><img src="{A}{img}.webp" width="640" height="640" loading="lazy" decoding="async" alt="Portada: {esc(t)}"><div><h3>{esc(t)}{" <span class=\'bt\'>BONO</span>" if bono else ""}</h3><p>{esc(d)}</p></div></li>' for img, t, d in items)

def cgrid(items, bono=False):
    return "".join(f'<li{" class=\"bono\"" if bono else ""}><img src="{A}{img}.webp" width="520" height="735" loading="lazy" decoding="async" alt="Portada: {esc(t)}"><div class="t"><h3>{esc(t)}</h3><p>{esc(d)}</p></div></li>' for img, t, d in items)

PIXEL = """<script>
window.PAGE='upsell2';
(function(){
if(window.__NO_TRACK||location.protocol==='file:')return;
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init','973045345819425');
fbq('track','PageView');
fbq('trackCustom','VerUpsell2',{value:19.90,currency:'USD',content_name:'Psicología Aplicada a la Vida'});
})();
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id=973045345819425&ev=PageView&noscript=1" alt=""></noscript>"""

stack = ('<ul class="stack">'
         '<li><span class="ck">✓</span><span><strong>12 guías completas</strong> de psicología aplicada (más de 200 páginas)</span></li>'
         '<li><span class="ck">✓</span><span><strong>3 bonos:</strong> Color, Atracción y Retos de 21 Días</span><span class="b">BONO</span></li>'
         '<li><span class="ck">✓</span><span>Acceso inmediato en el email de tu compra</span></li>'
         '<li><span class="ck">✓</span><span>Para leer en el celular o imprimir</span></li></ul>')

html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="#0E242B">
<title>Psicología Aplicada a la Vida · Oferta final</title>
<meta name="description" content="12 guías + 3 bonos de psicología aplicada al día a día con precio especial. Pago único.">
<link rel="icon" href="https://biblipsicologia1.vercel.app/favicon.svg">
<link rel="preload" as="image" href="{A}mockup.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600;1,700&family=Figtree:wght@400;500;600;700;800&display=swap" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600;1,700&family=Figtree:wght@400;500;600;700;800&display=swap"></noscript>
<link rel="dns-prefetch" href="https://checkout.hotmart.com">
<script>window.TIMER_MIN=10;window.TIMER_DONE='<strong>Tiempo agotado.</strong> La oferta desaparece al cerrar esta página.';</script>
{PIXEL}
<style>{CSS}{EXTRA_CSS}</style>
</head>
<body>
<div class="topbar" role="status"><div class="in"><span class="msg" data-timer-msg><strong>Oferta final · solo hoy.</strong> Este precio se mantiene durante:</span>{CLOCK}</div></div>
<div class="steps" aria-label="Progreso del pedido"><span class="done"><i>✓</i>Compra</span><b></b><span class="now"><i>2</i>Oferta final</span><b></b><span><i>3</i>Acceso</span></div>
<main>
<section class="hero" id="inicio"><div class="wrap">
<p class="eyebrow">Una última cosa antes de tu acceso</p>
<h1>La psicología que usas <em>todos los días</em>, explicada en 12 guías.</h1>
<p class="sub">Persuasión, lenguaje corporal, dinero, sesgos, redes sociales, sueño, psicología criminal y más. <strong>12 guías + 3 bonos</strong> para entender a las personas y decidir mejor, con <strong>80% de descuento</strong>.</p>
<div class="hero-media"><img src="{A}mockup.webp" width="1254" height="1254" fetchpriority="high" alt="Psicología Aplicada a la Vida: 12 guías + 3 bonos"></div>
<p class="pricehint">Precio especial para clientes · <strong>80% de descuento</strong></p>
<a class="btn" href="#oferta" data-go="hero">Sí, quiero las 12 guías</a>
<p class="micro">Pago único · Se añade a tu pedido en segundos · Garantía de 7 días</p>
</div></section>

<section class="pain2" id="dolor"><div class="wrap">
<h2>¿Te ha pasado esto?</h2>
<ul>
<li>Compras algo por impulso y a los dos días te arrepientes.</li>
<li>Alguien te convence de algo y después sientes que te manipularon.</li>
<li>Pasas horas en el móvil y terminas peor que antes.</li>
<li>No entiendes por qué decides, gastas o reaccionas como lo haces.</li>
</ul>
<p class="turn2">No es falta de voluntad: es psicología. <em>Y se puede entender.</em></p>
</div></section>

<section class="get" id="recibes"><div class="wrap">
<div class="head"><p class="eyebrow">Lo que vas a recibir</p><h2>12 guías + 3 bonos</h2></div>
<ul class="glist">{glist(GUIDES)}</ul>
<p class="sub-h">+ 3 bonos incluidos</p>
<ul class="glist">{glist(BONOS, True)}</ul>
</div></section>

<section class="offer" id="oferta" style="padding-top:10px"><div class="wrap"><div class="offer-card">
<span class="badge">Oferta final · solo hoy</span>
<h2>Psicología Aplicada a la Vida</h2>
<img class="mock" src="{A}mockup.webp" width="1254" height="1254" loading="lazy" decoding="async" alt="Psicología Aplicada a la Vida">
{stack}
<div class="price"><div class="old">Precio especial para clientes</div><div class="now">−80%</div><div class="save">Tu precio final aparece abajo, en tu moneda</div><div class="terms">Pago único · Acceso inmediato · Sin mensualidades</div></div>
<div class="offer-timer">Este precio termina en {CLOCK}</div>
<div class="widget">
{WIDGET}
</div>
<p class="oneclick">Se añade a tu pedido en segundos · Garantía de 7 días en Hotmart. Si sales de esta página, la oferta desaparece.</p>
</div></div></section>

</main>
<footer><div class="wrap">Psicología Aplicada a la Vida · Material educativo y de divulgación. No sustituye la atención de profesionales de la salud, la psicología, las finanzas ni el derecho.</div></footer>
{VIEWER}
<script>{JS}</script>
</body>
</html>
"""
os.makedirs(os.path.join(OUT, "upsell2"), exist_ok=True)
with open(os.path.join(OUT, "upsell2", "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("upsell2", len(html))

# ======================================================================= DOWNSELL 2 (US$ 9,90)
import re as _re
d = html
REPL = [
    ("window.PAGE='upsell2';", "window.PAGE='downsell2';"),
    ("fbq('trackCustom','VerUpsell2',{value:19.90,", "fbq('trackCustom','VerDownsell2',{value:9.90,"),
    ("<title>Psicología Aplicada a la Vida · Oferta final</title>", "<title>Psicología Aplicada a la Vida · Última oportunidad</title>"),
    ("12 guías + 3 bonos de psicología aplicada al día a día con precio especial. Pago único.", "Última oportunidad: 12 guías + 3 bonos de psicología aplicada a mitad de precio. Pago único."),
    ("<strong>Oferta final · solo hoy.</strong> Este precio se mantiene durante:", "<strong>Espera · última oportunidad.</strong> Este precio solo se mantiene durante:"),
    ("<i>2</i>Oferta final</span>", "<i>2</i>Última oferta</span>"),
    ('<p class="eyebrow">Una última cosa antes de tu acceso</p>', '<p class="eyebrow">Precio especial · solo una vez</p>'),
    ("<h1>La psicología que usas <em>todos los días</em>, explicada en 12 guías.</h1>", "<h1>Lo entendemos. Por eso te dejamos las 12 guías <em>a mitad de precio</em>.</h1>"),
    ('alt="Psicología Aplicada a la Vida: 12 guías + 3 bonos"></div>', 'alt="Psicología Aplicada a la Vida: 12 guías + 3 bonos"><span class="ribbon">−50%</span></div>'),
    ('Precio especial para clientes · <strong>80% de descuento</strong>', 'Última oportunidad · <strong>50% menos</strong> que la oferta anterior'),
    ('data-go="hero">Sí, quiero las 12 guías</a>', 'data-go="hero">Sí, las quiero a mitad de precio</a>'),
    ('<span class="badge">Oferta final · solo hoy</span>', '<span class="badge">Última oportunidad</span>'),
    ('<div class="old">Precio especial para clientes</div><div class="now">−80%</div>', '<div class="old">Mitad de precio · solo aquí</div><div class="now">−50%</div>'),
    ("La oferta desaparece al cerrar esta página.';", "Esta es tu última oportunidad.';"),
]
for a, b in REPL:
    assert a in d, a
    d = d.replace(a, b)
d = _re.sub(r'<p class="sub">.*?</p>', '<p class="sub">Las mismas <strong>12 guías + 3 bonos</strong>, sin quitar nada, por la mitad del precio. Esta oferta no vuelve a aparecer.</p>', d, count=1, flags=_re.S)
d = _re.sub(r'<section class="pain2".*?</section>\s*', '', d, count=1, flags=_re.S)
os.makedirs(os.path.join(OUT, "downsell2"), exist_ok=True)
with open(os.path.join(OUT, "downsell2", "index.html"), "w", encoding="utf-8") as f:
    f.write(d)
print("downsell2", len(d))
