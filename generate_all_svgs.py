import base64
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

# 1. Base64 encoding for avatars
with open('banner_avatar_cutout.webp', 'rb') as f:
    banner_avatar_b64 = base64.b64encode(f.read()).decode('ascii')

with open('id_avatar_crop.png', 'rb') as f:
    id_avatar_b64 = base64.b64encode(f.read()).decode('ascii')

# 2. Extract letter paths for "Vishal Gangwar"
font = TTFont('Pacifico.ttf')
glyph_set = font.getGlyphSet()
cmap = font.getBestCmap()

def get_text_paths(text, scale=0.05200, start_delay=1.60, delay_step=0.08, space_width=24.0):
    pos_x = 0.0
    items = []
    for i, ch in enumerate(text):
        if ch == ' ':
            pos_x += space_width
            continue
        code = ord(ch)
        glyph_name = cmap.get(code)
        glyph = glyph_set[glyph_name]
        pen = SVGPathPen(glyph_set)
        glyph.draw(pen)
        d = pen.getCommands()
        delay = start_delay + i * delay_step
        items.append((ch, pos_x, d, delay))
        pos_x += glyph.width * scale
    return items, pos_x

banner_letters, _ = get_text_paths("Vishal Gangwar", scale=0.05200, start_delay=1.60, delay_step=0.08)
lanyard_letters, _ = get_text_paths("Vishal Gangwar", scale=0.03000, start_delay=1.60, delay_step=0.05, space_width=14.0)

# Build letter SVG groups for banner
banner_letters_xml = ""
for ch, px, d, delay in banner_letters:
    banner_letters_xml += f'      <g class="ltr" style="animation-delay:{delay:.2f}s"><path transform="translate({px:.1f},0) scale(0.05200,-0.05200)" d="{d}"/></g>\n'

# Build letter SVG groups for lanyard
lanyard_letters_xml = ""
for ch, px, d, delay in lanyard_letters:
    lanyard_letters_xml += f'    <path transform="translate({px:.1f},0) scale(0.03000,-0.03000)" d="{d}"/>\n'

# ==========================================
# 1. vishal-banner.svg (Dark Theme)
# ==========================================
banner_dark_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="1280" height="740" role="img" aria-label="Vishal Gangwar - Full Stack Developer">
<title>Vishal Gangwar — Full Stack Developer</title>
<defs>
<style type="text/css"><![CDATA[
text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes popIn{{0%{{opacity:0;transform:translateY(14px) scale(.7)}}70%{{opacity:1;transform:translateY(-3px) scale(1.06)}}100%{{opacity:1;transform:translateY(0) scale(1)}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes floaty{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-9px)}}}}
@keyframes floaty2{{0%,100%{{transform:translateY(0) rotate(0deg)}}50%{{transform:translateY(-12px) rotate(6deg)}}}}
@keyframes neonFlicker{{0%{{opacity:0}}5%{{opacity:.7}}7%{{opacity:.1}}10%{{opacity:.9}}12%{{opacity:.3}}16%,100%{{opacity:1}}}}
@keyframes neonPulse{{0%,100%{{opacity:.65}}50%{{opacity:1}}}}
@keyframes twinkle{{0%,100%{{opacity:0;transform:scale(.4)}}50%{{opacity:1;transform:scale(1)}}}}
@keyframes rise{{0%{{transform:translateY(0);opacity:0}}12%{{opacity:.55}}88%{{opacity:.55}}100%{{transform:translateY(-46px);opacity:0}}}}
.ltr{{opacity:0;animation:popIn .5s cubic-bezier(.2,.8,.3,1.3) forwards;transform-box:fill-box;transform-origin:center bottom}}
.ii,.pill,.soc,.st,.cl{{opacity:0}}
.pill{{transition:transform .2s ease,filter .2s ease;transform-box:fill-box;transform-origin:center;cursor:pointer}}
.pill:hover{{transform:scale(1.08);filter:brightness(1.35)}}
.cur{{animation:blink 1s step-end infinite}}
.tw{{transform-box:fill-box;transform-origin:center;animation:twinkle 2.6s ease-in-out infinite}}
.fl{{animation:floaty 5s ease-in-out infinite}}
.fl2{{transform-box:fill-box;transform-origin:center;animation:floaty2 4.2s ease-in-out infinite}}
.neon-on{{animation:neonFlicker 2.4s ease 3.2s backwards}}
.np{{animation:neonPulse 2.6s ease-in-out infinite}}
.rp{{animation:rise linear infinite}}
.sep{{stroke:#1e293b;stroke-width:1;opacity:.8}}
]]></style>

<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#060c18"/><stop offset="55%" stop-color="#0b172a"/><stop offset="100%" stop-color="#050a14"/>
</linearGradient>
<linearGradient id="nameg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#38bdf8;#60a5fa;#22d3ee" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="55%"><animate attributeName="stop-color" values="#38bdf8;#818cf8;#22d3ee;#38bdf8" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#60a5fa;#22d3ee;#38bdf8;#60a5fa" dur="7s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="borderg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity=".45"/>
  <stop offset="50%" stop-color="#38bdf8" stop-opacity=".35"/>
  <stop offset="100%" stop-color="#60a5fa" stop-opacity=".45"/>
</linearGradient>
<radialGradient id="orbCyan"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".14"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<radialGradient id="orbBlue"><stop offset="0%" stop-color="#3b82f6" stop-opacity=".13"/><stop offset="100%" stop-color="#3b82f6" stop-opacity="0"/></radialGradient>
<radialGradient id="orbIndigo"><stop offset="0%" stop-color="#6366f1" stop-opacity=".10"/><stop offset="100%" stop-color="#6366f1" stop-opacity="0"/></radialGradient>
<radialGradient id="avatarGlow"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".22"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<filter id="glow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowBig"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="dots" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="15" cy="15" r=".7" fill="#38bdf8" opacity=".18"/></pattern>

<clipPath id="cPrompt"><rect x="48" y="48" width="0" height="32"><animate attributeName="width" from="0" to="370" dur="1.2s" begin=".2s" fill="freeze"/></rect></clipPath>
<clipPath id="cHi"><rect x="48" y="86" width="0" height="42"><animate attributeName="width" from="0" to="180" dur=".8s" begin="1.2s" fill="freeze"/></rect></clipPath>
<clipPath id="q1"><rect x="76" y="258" width="0" height="46"><animate attributeName="width" from="0" to="340" dur="1.4s" begin="3.3s" fill="freeze"/></rect></clipPath>
<clipPath id="q2"><rect x="76" y="284" width="0" height="46"><animate attributeName="width" from="0" to="340" dur="1.4s" begin="3.5s" fill="freeze"/></rect></clipPath>

<!-- Cycling roles: 4 roles, 24s -->
<clipPath id="r1"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;280;280;0;0;0;0;0" keyTimes="0;.04;.21;.25;.251;.999;1" dur="24s" repeatCount="indefinite"/></rect></clipPath>
<clipPath id="r2"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;290;290;0;0;0;0" keyTimes="0;.25;.29;.46;.50;.501;.999;1" dur="24s" repeatCount="indefinite"/></rect></clipPath>
<clipPath id="r3"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;280;280;0;0;0;0" keyTimes="0;.50;.54;.71;.75;.751;.999;1" dur="24s" repeatCount="indefinite"/></rect></clipPath>
<clipPath id="r4"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;250;250;0;0" keyTimes="0;.75;.79;.96;1" dur="24s" repeatCount="indefinite"/></rect></clipPath>

<linearGradient id="scanEdge" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/><stop offset="18%" stop-color="#22d3ee"/>
  <stop offset="50%" stop-color="#38bdf8"/><stop offset="82%" stop-color="#60a5fa"/>
  <stop offset="100%" stop-color="#60a5fa" stop-opacity="0"/>
</linearGradient>
<linearGradient id="scanTrail" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#22d3ee" stop-opacity="0"/><stop offset="100%" stop-color="#22d3ee" stop-opacity=".22"/>
</linearGradient>

<clipPath id="avatarReveal"><rect x="722" y="152" width="558" height="0">
  <animate attributeName="height" from="0" to="522" dur="1.8s" begin=".5s" fill="freeze"/>
</rect></clipPath>
<clipPath id="avatarBox"><rect x="722" y="152" width="558" height="522" rx="20"/></clipPath>
<clipPath id="bannerBox"><rect x="1" y="1" width="1278" height="738" rx="22"/></clipPath>
</defs>

<!-- ================= BACKGROUND ================= -->
<rect width="1280" height="740" rx="22" fill="url(#bg)"/>
<rect width="1280" height="740" rx="22" fill="url(#dots)"/>
<circle cx="230" cy="220" r="260" fill="url(#orbCyan)"><animate attributeName="r" values="260;290;260" dur="6s" repeatCount="indefinite"/></circle>
<circle cx="1000" cy="520" r="300" fill="url(#orbBlue)"><animate attributeName="r" values="300;330;300" dur="7s" repeatCount="indefinite"/></circle>
<circle cx="700" cy="120" r="200" fill="url(#orbIndigo)"><animate attributeName="r" values="200;225;200" dur="5s" repeatCount="indefinite"/></circle>
<rect x="1" y="1" width="1278" height="738" rx="22" fill="none" stroke="url(#borderg)" stroke-width="1.5"/>

<!-- rising particles -->
<circle class="rp" cx="140" cy="620" r="1.4" fill="#22d3ee" style="animation-duration:5s"/>
<circle class="rp" cx="420" cy="700" r="1.1" fill="#38bdf8" style="animation-duration:6s;animation-delay:1s"/>
<circle class="rp" cx="620" cy="660" r="1.3" fill="#60a5fa" style="animation-duration:4.6s;animation-delay:2s"/>
<circle class="rp" cx="1180" cy="690" r="1.2" fill="#22d3ee" style="animation-duration:5.4s;animation-delay:.6s"/>
<circle class="rp" cx="1240" cy="360" r="1" fill="#38bdf8" style="animation-duration:6.4s;animation-delay:1.6s"/>
<circle class="rp" cx="70" cy="420" r="1" fill="#818cf8" style="animation-duration:5.8s;animation-delay:2.4s"/>

<!-- sparkles -->
<g class="tw" style="animation-delay:.4s"><path d="M470 120l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#38bdf8"/></g>
<g class="tw" style="animation-delay:1.5s"><path d="M880 120l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#22d3ee"/></g>
<g class="tw" style="animation-delay:2.6s"><path d="M1245 250l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#7dd3fc"/></g>

<!-- ================= LEFT: CONTENT ================= -->
<!-- Terminal prompt -->
<text clip-path="url(#cPrompt)" x="48" y="69" font-size="14"><tspan fill="#4ade80" font-weight="bold">vishal@full-stack-dev:~$</tspan><tspan fill="#e6edf3"> cat README.md</tspan></text>
<rect x="360" y="56" width="8" height="16" fill="#4ade80" opacity="0"><animate attributeName="opacity" values="1;1;0;0" dur="1s" repeatCount="indefinite"/></rect>

<!-- Hi, I'm -->
<text clip-path="url(#cHi)" x="48" y="114" font-size="24" font-weight="bold" fill="#e6edf3">Hi, I'm 👋</text>

<!-- Name: Vishal Gangwar (Pacifico outlines, per-letter pop, animated cyan/blue gradient) -->
<g transform="translate(48,196)" fill="url(#nameg)" filter="url(#glow)">
{banner_letters_xml}</g>
<g class="tw" style="animation-delay:3s"><path d="M435 168 l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#22d3ee" filter="url(#glow)"/></g>

<!-- Cycling roles -->
<text clip-path="url(#r1)" x="48" y="241" font-size="17" fill="#38bdf8" filter="url(#glow)">&lt; Full-Stack Developer /&gt;</text>
<text clip-path="url(#r2)" x="48" y="241" font-size="17" fill="#38bdf8" filter="url(#glow)">&lt; Open Source Enthusiast /&gt;</text>
<text clip-path="url(#r3)" x="48" y="241" font-size="17" fill="#38bdf8" filter="url(#glow)">&lt; AI &amp; Systems Builder /&gt;</text>
<text clip-path="url(#r4)" x="48" y="241" font-size="17" fill="#38bdf8" filter="url(#glow)">&lt; Problem Solver /&gt;</text>
<rect x="48" y="228" width="2.5" height="16" fill="#22d3ee" opacity="0"><animate attributeName="opacity" values="0;1;0" dur="1s" repeatCount="indefinite"/></rect>

<!-- Quote box -->
<g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
  <rect x="48" y="262" width="410" height="72" rx="8" fill="#0f1d36" stroke="#1e3a5f" stroke-width="1"/>
  <rect x="48" y="266" width="3.5" height="64" rx="1.5" fill="#22d3ee"/>
</g>
<text clip-path="url(#q1)" x="76" y="292" font-size="14.5" font-weight="600" fill="#f1f5f9">Turning ideas into scalable products,</text>
<text clip-path="url(#q2)" x="76" y="318" font-size="14.5" font-weight="600"><tspan fill="#f1f5f9">one commit at a </tspan><tspan fill="#22d3ee" font-weight="bold">time.</tspan></text>
<g class="tw" style="animation-delay:.9s"><path d="M425 288l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#38bdf8"/></g>

<!-- Tech I Know -->
<text class="ii" x="48" y="374" font-size="15" fill="#38bdf8" font-weight="bold" style="animation:fadeIn .4s ease 4.6s forwards">⚡ Tech I Know</text>

<!-- Row 1: HTML, CSS, JavaScript, React, Node.js -->
<g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><rect x="48" y="388" width="70" height="26" rx="13" fill="#0e223d" stroke="#0284c7" stroke-width="1"/><text x="83" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#7dd3fc">HTML</text></g>
<g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><rect x="126" y="388" width="64" height="26" rx="13" fill="#0e223d" stroke="#0284c7" stroke-width="1"/><text x="158" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#7dd3fc">CSS</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.0s forwards"><rect x="198" y="388" width="104" height="26" rx="13" fill="#0e223d" stroke="#38bdf8" stroke-width="1"/><text x="250" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#fde047">JavaScript</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><rect x="310" y="388" width="76" height="26" rx="13" fill="#0e223d" stroke="#22d3ee" stroke-width="1"/><text x="348" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#22d3ee">React</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.2s forwards"><rect x="394" y="388" width="86" height="26" rx="13" fill="#0e223d" stroke="#10b981" stroke-width="1"/><text x="437" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#4ade80">Node.js</text></g>

<!-- Row 2: Python, C++, MongoDB, SQL -->
<g class="pill" style="animation:fadeIn .3s ease 5.3s forwards"><rect x="48" y="422" width="80" height="26" rx="13" fill="#0e223d" stroke="#3b82f6" stroke-width="1"/><text x="88" y="439" text-anchor="middle" font-size="12" font-weight="bold" fill="#93c5fd">Python</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.4s forwards"><rect x="136" y="422" width="64" height="26" rx="13" fill="#0e223d" stroke="#6366f1" stroke-width="1"/><text x="168" y="439" text-anchor="middle" font-size="12" font-weight="bold" fill="#a5b4fc">C++</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.5s forwards"><rect x="208" y="422" width="94" height="26" rx="13" fill="#0e223d" stroke="#10b981" stroke-width="1"/><text x="255" y="439" text-anchor="middle" font-size="12" font-weight="bold" fill="#4ade80">MongoDB</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.6s forwards"><rect x="310" y="422" width="64" height="26" rx="13" fill="#0e223d" stroke="#0284c7" stroke-width="1"/><text x="342" y="439" text-anchor="middle" font-size="12" font-weight="bold" fill="#38bdf8">SQL</text></g>

<!-- About Me -->
<text class="ii" x="48" y="490" font-size="15" fill="#22d3ee" font-weight="bold" style="animation:fadeIn .4s ease 5.7s forwards">💻 About Me</text>
<text class="ii" x="48" y="516" font-size="13.5" style="animation:fadeIn .4s ease 5.9s forwards"><tspan fill="#4ade80">&gt;_ </tspan><tspan fill="#c9d1d9">I build full-stack apps that are </tspan><tspan fill="#38bdf8">fast, scalable</tspan><tspan fill="#c9d1d9"> and user-focused.</tspan></text>
<text class="ii" x="48" y="540" font-size="13.5" style="animation:fadeIn .4s ease 6.1s forwards"><tspan fill="#fde047">💡 </tspan><tspan fill="#c9d1d9">Always learning, always shipping real-world products.</tspan></text>
<text class="ii" x="48" y="564" font-size="13.5" style="animation:fadeIn .4s ease 6.3s forwards"><tspan fill="#38bdf8">🚀 </tspan><tspan fill="#c9d1d9">Turning ideas into impactful software solutions.</tspan></text>

<!-- Stats card -->
<g class="st" style="animation:fadeIn .5s ease 6.5s forwards">
  <rect x="48" y="586" width="560" height="66" rx="12" fill="#0d1b33" stroke="#1e3a5f" stroke-width="1"/>
  <line x1="188" y1="598" x2="188" y2="640" class="sep"/>
  <line x1="328" y1="598" x2="328" y2="640" class="sep"/>
  <line x1="468" y1="598" x2="468" y2="640" class="sep"/>
  <text x="118" y="612" text-anchor="middle" font-size="11.5" fill="#94a3b8">📦 Repos</text>
  <text x="258" y="612" text-anchor="middle" font-size="11.5" fill="#94a3b8">💻 Commits</text>
  <text x="398" y="612" text-anchor="middle" font-size="11.5" fill="#94a3b8">⭐ Stars</text>
  <text x="538" y="612" text-anchor="middle" font-size="11.5" fill="#94a3b8">👥 Followers</text>
</g>
<text class="st" x="118" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#22d3ee" style="animation:fadeIn .5s ease 6.7s forwards">12+</text>
<text class="st" x="258" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#38bdf8" style="animation:fadeIn .5s ease 6.7s forwards">300+</text>
<text class="st" x="398" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#fde047" style="animation:fadeIn .5s ease 6.7s forwards">20+</text>
<text class="st" x="538" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#818cf8" style="animation:fadeIn .5s ease 6.7s forwards">15+</text>

<!-- ================= CENTER-TOP: product.jsx ================= -->
<g class="cl" style="animation:fadeIn .5s ease 1.4s forwards">
  <rect x="552" y="40" width="286" height="212" rx="12" fill="#0b172a" fill-opacity=".95" stroke="#1e3a5f" stroke-width="1.2"/>
  <rect x="552" y="40" width="286" height="28" rx="12" fill="#0f223d"/>
  <rect x="552" y="56" width="286" height="12" fill="#0f223d"/>
  <circle cx="572" cy="54" r="4.5" fill="#ef4444"/><circle cx="588" cy="54" r="4.5" fill="#f59e0b"/><circle cx="604" cy="54" r="4.5" fill="#10b981"/>
  <text x="695" y="58" text-anchor="middle" font-size="11" fill="#94a3b8">product.jsx</text>
</g>
<g font-size="12">
  <text class="cl" x="568" y="90" style="animation:fadeIn .3s ease 1.8s forwards"><tspan fill="#38bdf8">function</tspan><tspan fill="#22d3ee"> buildProduct</tspan><tspan fill="#e6edf3">() {{</tspan></text>
  <text class="cl" x="582" y="110" style="animation:fadeIn .3s ease 2.1s forwards"><tspan fill="#38bdf8">return</tspan><tspan fill="#e6edf3"> (</tspan></text>
  <text class="cl" x="596" y="130" style="animation:fadeIn .3s ease 2.4s forwards"><tspan fill="#94a3b8">&lt;</tspan><tspan fill="#4ade80">div</tspan><tspan fill="#38bdf8"> className</tspan><tspan fill="#e6edf3">=</tspan><tspan fill="#fde047">"product"</tspan><tspan fill="#94a3b8">&gt;</tspan></text>
  <text class="cl" x="610" y="150" style="animation:fadeIn .3s ease 2.7s forwards"><tspan fill="#94a3b8">&lt;</tspan><tspan fill="#22d3ee">Idea</tspan><tspan fill="#94a3b8"> /&gt;</tspan></text>
  <text class="cl" x="610" y="168" style="animation:fadeIn .3s ease 2.95s forwards"><tspan fill="#94a3b8">&lt;</tspan><tspan fill="#fde047">Code</tspan><tspan fill="#94a3b8"> /&gt;</tspan></text>
  <text class="cl" x="610" y="186" style="animation:fadeIn .3s ease 3.2s forwards"><tspan fill="#94a3b8">&lt;</tspan><tspan fill="#38bdf8">Deploy</tspan><tspan fill="#94a3b8"> /&gt;</tspan></text>
  <text class="cl" x="610" y="204" style="animation:fadeIn .3s ease 3.45s forwards"><tspan fill="#94a3b8">&lt;</tspan><tspan fill="#4ade80">Impact</tspan><tspan fill="#94a3b8"> /&gt;</tspan></text>
  <text class="cl" x="596" y="222" style="animation:fadeIn .3s ease 3.65s forwards"><tspan fill="#94a3b8">&lt;/</tspan><tspan fill="#4ade80">div</tspan><tspan fill="#94a3b8">&gt;</tspan><tspan fill="#e6edf3">);</tspan></text>
  <text class="cl" x="568" y="242" style="animation:fadeIn .3s ease 3.85s forwards"><tspan fill="#e6edf3">}}</tspan><tspan fill="#94a3b8"> // export default</tspan></text>
</g>

<!-- Neon sign -->
<g class="neon-on">
  <rect x="1012" y="42" width="238" height="128" rx="14" fill="#0b172a" stroke="#22d3ee" stroke-width="1.8" filter="url(#glow)"/>
  <text class="np" x="1131" y="86" text-anchor="middle" font-size="30" font-weight="bold" fill="#22d3ee" filter="url(#glowBig)" style="animation-delay:.2s">&lt;/&gt;</text>
  <text class="np" x="1131" y="118" text-anchor="middle" font-size="18" font-weight="bold" fill="#38bdf8" filter="url(#glow)" letter-spacing="2">KEEP BUILDING</text>
  <text class="np" x="1131" y="146" text-anchor="middle" font-size="18" font-weight="bold" fill="#818cf8" filter="url(#glow)" letter-spacing="2">KEEP SHIPPING</text>
</g>

<!-- ================= RIGHT: ILLUSTRATION ================= -->
<circle cx="980" cy="430" r="280" fill="url(#avatarGlow)"><animate attributeName="r" values="280;310;280" dur="5s" repeatCount="indefinite"/></circle>

<g class="fl">
  <!-- Seamless floating character illustration (no boxed panel) -->
  <image x="715" y="140" width="545" height="556" href="data:image/webp;base64,{banner_avatar_b64}"/>

  <!-- Floating Tech Orbits -->
  <g class="fl2" style="animation-delay:.3s">
    <g transform="translate(680, 290)">
      <circle cx="22" cy="22" r="22" fill="#0a192f" stroke="#22d3ee" stroke-width="1.5" filter="url(#glow)"/>
      <text x="22" y="27" text-anchor="middle" font-size="12" font-weight="bold" fill="#22d3ee">SQL</text>
    </g>
  </g>
  <g class="fl2" style="animation-delay:1.2s">
    <g transform="translate(660, 420)">
      <circle cx="22" cy="22" r="22" fill="#0a192f" stroke="#fde047" stroke-width="1.5" filter="url(#glow)"/>
      <text x="22" y="27" text-anchor="middle" font-size="13" font-weight="bold" fill="#fde047">JS</text>
    </g>
  </g>
  <g class="fl2" style="animation-delay:2.1s">
    <g transform="translate(1220, 520)">
      <circle cx="22" cy="22" r="22" fill="#0a192f" stroke="#60a5fa" stroke-width="1.5" filter="url(#glow)"/>
      <text x="22" y="27" text-anchor="middle" font-size="12" font-weight="bold" fill="#60a5fa">C++</text>
    </g>
  </g>
</g>

<!-- ================= FOOTER ================= -->
<line x1="48" y1="676" x2="1232" y2="676" class="sep" stroke-dasharray="1184" stroke-dashoffset="1184">
  <animate attributeName="stroke-dashoffset" from="1184" to="0" dur=".7s" begin="7.0s" fill="freeze"/>
</line>
<g class="soc" style="animation:fadeIn .5s ease 7.2s forwards">
  <!-- GitHub -->
  <g transform="translate(48,692) scale(.8)">
    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" fill="#22d3ee"/>
  </g>
  <text x="74" y="707" font-size="12.5" fill="#cbd5e1">vishalgangwar176</text>

  <!-- Email -->
  <g transform="translate(240,693) scale(.8)">
    <rect x="1" y="3" width="22" height="17" rx="3.5" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
    <path d="M2 6l10 7 10-7" fill="none" stroke="#38bdf8" stroke-width="1.8"/>
  </g>
  <text x="266" y="707" font-size="12.5" fill="#cbd5e1">vishalgangwar176@gmail.com</text>

  <!-- LinkedIn -->
  <g transform="translate(500,692) scale(.8)">
    <rect width="24" height="24" rx="4" fill="#0077b5"/>
    <path d="M6 9h3v10H6zm1.5-5a1.8 1.8 0 110 3.6 1.8 1.8 0 010-3.6zM11 9h2.8v1.4h.04c.4-.7 1.4-1.5 2.8-1.5 3 0 3.6 2 3.6 4.5V19h-3v-4.8c0-1.1 0-2.6-1.6-2.6s-1.8 1.2-1.8 2.5V19H11z" fill="#fff"/>
  </g>
  <text x="526" y="707" font-size="12.5" fill="#cbd5e1">vishal-gangwar</text>
</g>

<!-- Status & Quote -->
<text class="soc" x="780" y="707" font-size="11.5" style="animation:fadeIn .5s ease 7.4s forwards"><tspan fill="#4ade80">● </tspan><tspan fill="#94a3b8">open to collaborate</tspan></text>
<text class="soc" x="1232" y="707" text-anchor="end" font-size="13" style="animation:fadeIn .5s ease 7.5s forwards"><tspan fill="#38bdf8">“Code today, deploy tomorrow.” </tspan><tspan fill="#22d3ee">⚡</tspan></text>

<!-- full-banner scanner sweep -->
<g clip-path="url(#bannerBox)" opacity="0">
  <animate attributeName="opacity" from="0" to="1" dur=".6s" begin="3s" fill="freeze"/>
  <g>
    <animateTransform attributeName="transform" type="translate" values="0,-40;0,780" dur="3.5s" begin="3.2s" repeatCount="indefinite"/>
    <rect x="0" y="-34" width="1280" height="34" fill="url(#scanTrail)"/>
    <rect x="0" y="0" width="1280" height="2.6" fill="url(#scanEdge)" opacity=".6" filter="url(#glow)"/>
  </g>
</g>
</svg>'''

with open('vishal-banner-dark.svg', 'w') as f:
    f.write(banner_dark_svg)

print("Generated vishal-banner-dark.svg successfully!")

# ==========================================
# 2. vishal-banner-light.svg (High-Contrast Light Theme)
# ==========================================
banner_light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="1280" height="740" role="img" aria-label="Vishal Gangwar - Full Stack Developer">
<title>Vishal Gangwar — Full Stack Developer</title>
<defs>
<style type="text/css"><![CDATA[
text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
@keyframes popIn{{0%{{opacity:0;transform:translateY(14px) scale(.7)}}70%{{opacity:1;transform:translateY(-3px) scale(1.06)}}100%{{opacity:1;transform:translateY(0) scale(1)}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes floaty{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-9px)}}}}
@keyframes floaty2{{0%,100%{{transform:translateY(0) rotate(0deg)}}50%{{transform:translateY(-12px) rotate(6deg)}}}}
@keyframes neonFlicker{{0%{{opacity:0}}5%{{opacity:.7}}7%{{opacity:.1}}10%{{opacity:.9}}12%{{opacity:.3}}16%,100%{{opacity:1}}}}
@keyframes neonPulse{{0%,100%{{opacity:.65}}50%{{opacity:1}}}}
@keyframes twinkle{{0%,100%{{opacity:0;transform:scale(.4)}}50%{{opacity:1;transform:scale(1)}}}}
@keyframes rise{{0%{{transform:translateY(0);opacity:0}}12%{{opacity:.55}}88%{{opacity:.55}}100%{{transform:translateY(-46px);opacity:0}}}}
.ltr{{opacity:0;animation:popIn .5s cubic-bezier(.2,.8,.3,1.3) forwards;transform-box:fill-box;transform-origin:center bottom}}
.ii,.pill,.soc,.st,.cl{{opacity:0}}
.pill{{transition:transform .2s ease,filter .2s ease;transform-box:fill-box;transform-origin:center;cursor:pointer}}
.pill:hover{{transform:scale(1.08);filter:brightness(1.15)}}
.cur{{animation:blink 1s step-end infinite}}
.tw{{transform-box:fill-box;transform-origin:center;animation:twinkle 2.6s ease-in-out infinite}}
.fl{{animation:floaty 5s ease-in-out infinite}}
.fl2{{transform-box:fill-box;transform-origin:center;animation:floaty2 4.2s ease-in-out infinite}}
.neon-on{{animation:neonFlicker 2.4s ease 3.2s backwards}}
.np{{animation:neonPulse 2.6s ease-in-out infinite}}
.rp{{animation:rise linear infinite}}
.sep{{stroke:#cbd5e1;stroke-width:1;opacity:.8}}
]]></style>

<linearGradient id="bgl" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#f0f9ff"/><stop offset="55%" stop-color="#e0f2fe"/><stop offset="100%" stop-color="#f8fafc"/>
</linearGradient>
<linearGradient id="namegl" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#0284c7;#0ea5e9;#2563eb;#0284c7" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="55%"><animate attributeName="stop-color" values="#0ea5e9;#6366f1;#0284c7;#0ea5e9" dur="7s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#2563eb;#0284c7;#0ea5e9;#2563eb" dur="7s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="bordergl" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0284c7" stop-opacity=".45"/>
  <stop offset="50%" stop-color="#38bdf8" stop-opacity=".35"/>
  <stop offset="100%" stop-color="#0284c7" stop-opacity=".45"/>
</linearGradient>
<radialGradient id="orbCyanL"><stop offset="0%" stop-color="#0284c7" stop-opacity=".12"/><stop offset="100%" stop-color="#0284c7" stop-opacity="0"/></radialGradient>
<radialGradient id="orbBlueL"><stop offset="0%" stop-color="#38bdf8" stop-opacity=".15"/><stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
<radialGradient id="orbIndigoL"><stop offset="0%" stop-color="#818cf8" stop-opacity=".12"/><stop offset="100%" stop-color="#818cf8" stop-opacity="0"/></radialGradient>
<radialGradient id="avatarGlowL"><stop offset="0%" stop-color="#38bdf8" stop-opacity=".25"/><stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/></radialGradient>
<filter id="glow"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="glowBig"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<pattern id="dotsL" width="30" height="30" patternUnits="userSpaceOnUse"><circle cx="15" cy="15" r=".7" fill="#0284c7" opacity=".14"/></pattern>

<clipPath id="cPrompt"><rect x="48" y="48" width="0" height="32"><animate attributeName="width" from="0" to="370" dur="1.2s" begin=".2s" fill="freeze"/></rect></clipPath>
<clipPath id="cHi"><rect x="48" y="86" width="0" height="42"><animate attributeName="width" from="0" to="180" dur=".8s" begin="1.2s" fill="freeze"/></rect></clipPath>
<clipPath id="q1"><rect x="76" y="258" width="0" height="46"><animate attributeName="width" from="0" to="340" dur="1.4s" begin="3.3s" fill="freeze"/></rect></clipPath>
<clipPath id="q2"><rect x="76" y="284" width="0" height="46"><animate attributeName="width" from="0" to="340" dur="1.4s" begin="3.5s" fill="freeze"/></rect></clipPath>

<!-- Cycling roles: 4 roles, 24s -->
<clipPath id="r1"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;280;280;0;0;0;0;0" keyTimes="0;.04;.21;.25;.251;.999;1" dur="24s" repeatCount="indefinite"/></rect></clipPath>
<clipPath id="r2"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;290;290;0;0;0;0" keyTimes="0;.25;.29;.46;.50;.501;.999;1" dur="24s" repeatCount="indefinite"/></rect></clipPath>
<clipPath id="r3"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;280;280;0;0;0;0" keyTimes="0;.50;.54;.71;.75;.751;.999;1" dur="24s" repeatCount="indefinite"/></rect></clipPath>
<clipPath id="r4"><rect x="48" y="216" width="0" height="36"><animate attributeName="width" values="0;0;250;250;0;0" keyTimes="0;.75;.79;.96;1" dur="24s" repeatCount="indefinite"/></rect></clipPath>

<linearGradient id="scanEdgeL" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#0284c7" stop-opacity="0"/><stop offset="18%" stop-color="#0284c7"/>
  <stop offset="50%" stop-color="#0ea5e9"/><stop offset="82%" stop-color="#2563eb"/>
  <stop offset="100%" stop-color="#2563eb" stop-opacity="0"/>
</linearGradient>
<linearGradient id="scanTrailL" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#0284c7" stop-opacity="0"/><stop offset="100%" stop-color="#0284c7" stop-opacity=".15"/>
</linearGradient>
<clipPath id="bannerBox"><rect x="1" y="1" width="1278" height="738" rx="22"/></clipPath>
</defs>

<!-- ================= BACKGROUND ================= -->
<rect width="1280" height="740" rx="22" fill="url(#bgl)"/>
<rect width="1280" height="740" rx="22" fill="url(#dotsL)"/>
<circle cx="230" cy="220" r="260" fill="url(#orbCyanL)"><animate attributeName="r" values="260;290;260" dur="6s" repeatCount="indefinite"/></circle>
<circle cx="1000" cy="520" r="300" fill="url(#orbBlueL)"><animate attributeName="r" values="300;330;300" dur="7s" repeatCount="indefinite"/></circle>
<circle cx="700" cy="120" r="200" fill="url(#orbIndigoL)"><animate attributeName="r" values="200;225;200" dur="5s" repeatCount="indefinite"/></circle>
<rect x="1" y="1" width="1278" height="738" rx="22" fill="none" stroke="url(#bordergl)" stroke-width="1.5"/>

<!-- sparkles -->
<g class="tw" style="animation-delay:.4s"><path d="M470 120l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#0284c7"/></g>
<g class="tw" style="animation-delay:1.5s"><path d="M880 120l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#0ea5e9"/></g>
<g class="tw" style="animation-delay:2.6s"><path d="M1245 250l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#38bdf8"/></g>

<!-- ================= LEFT: CONTENT ================= -->
<!-- Terminal prompt -->
<text clip-path="url(#cPrompt)" x="48" y="69" font-size="14"><tspan fill="#16a34a" font-weight="bold">vishal@full-stack-dev:~$</tspan><tspan fill="#0f172a" font-weight="600"> cat README.md</tspan></text>
<rect x="360" y="56" width="8" height="16" fill="#16a34a" opacity="0"><animate attributeName="opacity" values="1;1;0;0" dur="1s" repeatCount="indefinite"/></rect>

<!-- Hi, I'm -->
<text clip-path="url(#cHi)" x="48" y="114" font-size="24" font-weight="bold" fill="#0f172a">Hi, I'm 👋</text>

<!-- Name: Vishal Gangwar (Pacifico outlines, animated blue/cyan gradient) -->
<g transform="translate(48,196)" fill="url(#namegl)" filter="url(#glow)">
{banner_letters_xml}</g>
<g class="tw" style="animation-delay:3s"><path d="M435 168 l3 8 8 3-8 3-3 8-3-8-8-3 8-3z" fill="#0284c7" filter="url(#glow)"/></g>

<!-- Cycling roles -->
<text clip-path="url(#r1)" x="48" y="241" font-size="17" font-weight="bold" fill="#0284c7">&lt; Full-Stack Developer /&gt;</text>
<text clip-path="url(#r2)" x="48" y="241" font-size="17" font-weight="bold" fill="#0284c7">&lt; Open Source Enthusiast /&gt;</text>
<text clip-path="url(#r3)" x="48" y="241" font-size="17" font-weight="bold" fill="#0284c7">&lt; AI &amp; Systems Builder /&gt;</text>
<text clip-path="url(#r4)" x="48" y="241" font-size="17" font-weight="bold" fill="#0284c7">&lt; Problem Solver /&gt;</text>
<rect x="48" y="228" width="2.5" height="16" fill="#0284c7" opacity="0"><animate attributeName="opacity" values="0;1;0" dur="1s" repeatCount="indefinite"/></rect>

<!-- Quote box: Solid dark gray/black text clearly readable against white box -->
<g class="cl" style="animation:fadeIn .5s ease 3.2s forwards">
  <rect x="48" y="262" width="410" height="72" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <rect x="48" y="266" width="4" height="64" rx="2" fill="#0284c7"/>
</g>
<text clip-path="url(#q1)" x="76" y="292" font-size="14.5" font-weight="600" fill="#0f172a">Turning ideas into scalable products,</text>
<text clip-path="url(#q2)" x="76" y="318" font-size="14.5" font-weight="600"><tspan fill="#0f172a">one commit at a </tspan><tspan fill="#0284c7" font-weight="bold">time.</tspan></text>
<g class="tw" style="animation-delay:.9s"><path d="M425 288l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#0284c7"/></g>

<!-- Tech I Know -->
<text class="ii" x="48" y="374" font-size="15" fill="#0284c7" font-weight="bold" style="animation:fadeIn .4s ease 4.6s forwards">⚡ Tech I Know</text>

<!-- Row 1: HTML, CSS, JavaScript, React, Node.js (Pastel pills, darkened high-contrast bold text) -->
<g class="pill" style="animation:fadeIn .3s ease 4.8s forwards"><rect x="48" y="388" width="70" height="26" rx="13" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.2"/><text x="83" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#0369a1">HTML</text></g>
<g class="pill" style="animation:fadeIn .3s ease 4.9s forwards"><rect x="126" y="388" width="64" height="26" rx="13" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.2"/><text x="158" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">CSS</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.0s forwards"><rect x="198" y="388" width="104" height="26" rx="13" fill="#fef9c3" stroke="#facc15" stroke-width="1.2"/><text x="250" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#854d0e">JavaScript</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.1s forwards"><rect x="310" y="388" width="76" height="26" rx="13" fill="#e0f2fe" stroke="#22d3ee" stroke-width="1.2"/><text x="348" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">React</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.2s forwards"><rect x="394" y="388" width="86" height="26" rx="13" fill="#dcfce7" stroke="#4ade80" stroke-width="1.2"/><text x="437" y="405" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d">Node.js</text></g>

<!-- Row 2: Python, C++, MongoDB, SQL -->
<g class="pill" style="animation:fadeIn .3s ease 5.3s forwards"><rect x="48" y="422" width="80" height="26" rx="13" fill="#dbeafe" stroke="#60a5fa" stroke-width="1.2"/><text x="88" y="439" text-anchor="middle" font-size="12" font-weight="bold" fill="#1d4ed8">Python</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.4s forwards"><rect x="136" y="422" width="64" height="26" rx="13" fill="#e0e7ff" stroke="#818cf8" stroke-width="1.2"/><text x="168" y="439" text-anchor="middle" font-size="12" font-weight="bold" fill="#4338ca">C++</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.5s forwards"><rect x="208" y="422" width="94" height="26" rx="13" fill="#dcfce7" stroke="#4ade80" stroke-width="1.2"/><text x="255" y="439" text-anchor="middle" font-size="12" font-weight="bold" fill="#15803d">MongoDB</text></g>
<g class="pill" style="animation:fadeIn .3s ease 5.6s forwards"><rect x="310" y="422" width="64" height="26" rx="13" fill="#e0f2fe" stroke="#38bdf8" stroke-width="1.2"/><text x="342" y="439" text-anchor="middle" font-size="12" font-weight="bold" fill="#0369a1">SQL</text></g>

<!-- About Me: Darkened to strong dark-gray/black tone -->
<text class="ii" x="48" y="490" font-size="15" fill="#0284c7" font-weight="bold" style="animation:fadeIn .4s ease 5.7s forwards">💻 About Me</text>
<text class="ii" x="48" y="516" font-size="13.5" font-weight="500" style="animation:fadeIn .4s ease 5.9s forwards"><tspan fill="#16a34a" font-weight="bold">&gt;_ </tspan><tspan fill="#0f172a">I build full-stack apps that are </tspan><tspan fill="#0284c7" font-weight="bold">fast, scalable</tspan><tspan fill="#0f172a"> and user-focused.</tspan></text>
<text class="ii" x="48" y="540" font-size="13.5" font-weight="500" style="animation:fadeIn .4s ease 6.1s forwards"><tspan fill="#ca8a04">💡 </tspan><tspan fill="#0f172a">Always learning, always shipping real-world products.</tspan></text>
<text class="ii" x="48" y="564" font-size="13.5" font-weight="500" style="animation:fadeIn .4s ease 6.3s forwards"><tspan fill="#0284c7">🚀 </tspan><tspan fill="#0f172a">Turning ideas into impactful software solutions.</tspan></text>

<!-- Stats card -->
<g class="st" style="animation:fadeIn .5s ease 6.5s forwards">
  <rect x="48" y="586" width="560" height="66" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
  <line x1="188" y1="598" x2="188" y2="640" stroke="#e2e8f0" stroke-width="1"/>
  <line x1="328" y1="598" x2="328" y2="640" stroke="#e2e8f0" stroke-width="1"/>
  <line x1="468" y1="598" x2="468" y2="640" stroke="#e2e8f0" stroke-width="1"/>
  <text x="118" y="612" text-anchor="middle" font-size="11.5" fill="#64748b">📦 Repos</text>
  <text x="258" y="612" text-anchor="middle" font-size="11.5" fill="#64748b">💻 Commits</text>
  <text x="398" y="612" text-anchor="middle" font-size="11.5" fill="#64748b">⭐ Stars</text>
  <text x="538" y="612" text-anchor="middle" font-size="11.5" fill="#64748b">👥 Followers</text>
</g>
<text class="st" x="118" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#0284c7" style="animation:fadeIn .5s ease 6.7s forwards">12+</text>
<text class="st" x="258" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#0284c7" style="animation:fadeIn .5s ease 6.7s forwards">300+</text>
<text class="st" x="398" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#b45309" style="animation:fadeIn .5s ease 6.7s forwards">20+</text>
<text class="st" x="538" y="640" text-anchor="middle" font-size="18" font-weight="bold" fill="#4338ca" style="animation:fadeIn .5s ease 6.7s forwards">15+</text>

<!-- ================= CENTER-TOP: product.jsx ================= -->
<g class="cl" style="animation:fadeIn .5s ease 1.4s forwards">
  <rect x="552" y="40" width="286" height="212" rx="12" fill="#ffffff" fill-opacity=".96" stroke="#cbd5e1" stroke-width="1.2"/>
  <rect x="552" y="40" width="286" height="28" rx="12" fill="#f1f5f9"/>
  <rect x="552" y="56" width="286" height="12" fill="#f1f5f9"/>
  <circle cx="572" cy="54" r="4.5" fill="#ef4444"/><circle cx="588" cy="54" r="4.5" fill="#f59e0b"/><circle cx="604" cy="54" r="4.5" fill="#10b981"/>
  <text x="695" y="58" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">product.jsx</text>
</g>
<g font-size="12">
  <text class="cl" x="568" y="90" style="animation:fadeIn .3s ease 1.8s forwards"><tspan fill="#0284c7">function</tspan><tspan fill="#0f172a" font-weight="bold"> buildProduct</tspan><tspan fill="#0f172a">() {{</tspan></text>
  <text class="cl" x="582" y="110" style="animation:fadeIn .3s ease 2.1s forwards"><tspan fill="#0284c7">return</tspan><tspan fill="#0f172a"> (</tspan></text>
  <text class="cl" x="596" y="130" style="animation:fadeIn .3s ease 2.4s forwards"><tspan fill="#64748b">&lt;</tspan><tspan fill="#16a34a" font-weight="bold">div</tspan><tspan fill="#0284c7"> className</tspan><tspan fill="#0f172a">=</tspan><tspan fill="#b45309" font-weight="bold">"product"</tspan><tspan fill="#64748b">&gt;</tspan></text>
  <text class="cl" x="610" y="150" style="animation:fadeIn .3s ease 2.7s forwards"><tspan fill="#64748b">&lt;</tspan><tspan fill="#0284c7" font-weight="bold">Idea</tspan><tspan fill="#64748b"> /&gt;</tspan></text>
  <text class="cl" x="610" y="168" style="animation:fadeIn .3s ease 2.95s forwards"><tspan fill="#64748b">&lt;</tspan><tspan fill="#b45309" font-weight="bold">Code</tspan><tspan fill="#64748b"> /&gt;</tspan></text>
  <text class="cl" x="610" y="186" style="animation:fadeIn .3s ease 3.2s forwards"><tspan fill="#64748b">&lt;</tspan><tspan fill="#0284c7" font-weight="bold">Deploy</tspan><tspan fill="#64748b"> /&gt;</tspan></text>
  <text class="cl" x="610" y="204" style="animation:fadeIn .3s ease 3.45s forwards"><tspan fill="#64748b">&lt;</tspan><tspan fill="#16a34a" font-weight="bold">Impact</tspan><tspan fill="#64748b"> /&gt;</tspan></text>
  <text class="cl" x="596" y="222" style="animation:fadeIn .3s ease 3.65s forwards"><tspan fill="#64748b">&lt;/</tspan><tspan fill="#16a34a" font-weight="bold">div</tspan><tspan fill="#64748b">&gt;</tspan><tspan fill="#0f172a">);</tspan></text>
  <text class="cl" x="568" y="242" style="animation:fadeIn .3s ease 3.85s forwards"><tspan fill="#0f172a">}}</tspan><tspan fill="#64748b"> // export default</tspan></text>
</g>

<!-- Neon sign -->
<g class="neon-on">
  <rect x="1012" y="42" width="238" height="128" rx="14" fill="#ffffff" stroke="#0284c7" stroke-width="1.8" filter="url(#glow)"/>
  <text class="np" x="1131" y="86" text-anchor="middle" font-size="30" font-weight="bold" fill="#0284c7" filter="url(#glowBig)" style="animation-delay:.2s">&lt;/&gt;</text>
  <text class="np" x="1131" y="118" text-anchor="middle" font-size="18" font-weight="bold" fill="#0369a1" filter="url(#glow)" letter-spacing="2">KEEP BUILDING</text>
  <text class="np" x="1131" y="146" text-anchor="middle" font-size="18" font-weight="bold" fill="#4338ca" filter="url(#glow)" letter-spacing="2">KEEP SHIPPING</text>
</g>

<!-- ================= RIGHT: ILLUSTRATION ================= -->
<circle cx="980" cy="430" r="280" fill="url(#avatarGlowL)"><animate attributeName="r" values="280;310;280" dur="5s" repeatCount="indefinite"/></circle>

<g class="fl">
  <!-- Seamless floating character illustration (no boxed panel) -->
  <image x="715" y="140" width="545" height="556" href="data:image/webp;base64,{banner_avatar_b64}"/>

  <!-- Floating Tech Orbits -->
  <g class="fl2" style="animation-delay:.3s">
    <g transform="translate(680, 290)">
      <circle cx="22" cy="22" r="22" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" filter="url(#glow)"/>
      <text x="22" y="27" text-anchor="middle" font-size="12" font-weight="bold" fill="#0284c7">SQL</text>
    </g>
  </g>
  <g class="fl2" style="animation-delay:1.2s">
    <g transform="translate(660, 430)">
      <circle cx="22" cy="22" r="22" fill="#ffffff" stroke="#facc15" stroke-width="1.5" filter="url(#glow)"/>
      <text x="22" y="27" text-anchor="middle" font-size="13" font-weight="bold" fill="#854d0e">JS</text>
    </g>
  </g>
  <g class="fl2" style="animation-delay:2.1s">
    <g transform="translate(1210, 520)">
      <circle cx="22" cy="22" r="22" fill="#ffffff" stroke="#818cf8" stroke-width="1.5" filter="url(#glow)"/>
      <text x="22" y="27" text-anchor="middle" font-size="12" font-weight="bold" fill="#4338ca">C++</text>
    </g>
  </g>
</g>

<!-- ================= FOOTER ================= -->
<line x1="48" y1="676" x2="1232" y2="676" class="sep" stroke-dasharray="1184" stroke-dashoffset="1184">
  <animate attributeName="stroke-dashoffset" from="1184" to="0" dur=".7s" begin="7.0s" fill="freeze"/>
</line>
<g class="soc" style="animation:fadeIn .5s ease 7.2s forwards">
  <!-- GitHub -->
  <g transform="translate(48,692) scale(.8)">
    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z" fill="#0284c7"/>
  </g>
  <text x="74" y="707" font-size="12.5" font-weight="600" fill="#0f172a">vishalgangwar176</text>

  <!-- Email -->
  <g transform="translate(240,693) scale(.8)">
    <rect x="1" y="3" width="22" height="17" rx="3.5" fill="none" stroke="#0284c7" stroke-width="1.8"/>
    <path d="M2 6l10 7 10-7" fill="none" stroke="#0284c7" stroke-width="1.8"/>
  </g>
  <text x="266" y="707" font-size="12.5" font-weight="600" fill="#0f172a">vishalgangwar176@gmail.com</text>

  <!-- LinkedIn -->
  <g transform="translate(500,692) scale(.8)">
    <rect width="24" height="24" rx="4" fill="#0077b5"/>
    <path d="M6 9h3v10H6zm1.5-5a1.8 1.8 0 110 3.6 1.8 1.8 0 010-3.6zM11 9h2.8v1.4h.04c.4-.7 1.4-1.5 2.8-1.5 3 0 3.6 2 3.6 4.5V19h-3v-4.8c0-1.1 0-2.6-1.6-2.6s-1.8 1.2-1.8 2.5V19H11z" fill="#fff"/>
  </g>
  <text x="526" y="707" font-size="12.5" font-weight="600" fill="#0f172a">vishal-gangwar</text>
</g>

<!-- Status & Quote -->
<text class="soc" x="780" y="707" font-size="11.5" font-weight="600" style="animation:fadeIn .5s ease 7.4s forwards"><tspan fill="#16a34a">● </tspan><tspan fill="#475569">open to collaborate</tspan></text>
<text class="soc" x="1232" y="707" text-anchor="end" font-size="13" font-weight="bold" style="animation:fadeIn .5s ease 7.5s forwards"><tspan fill="#0284c7">“Code today, deploy tomorrow.” </tspan><tspan fill="#0ea5e9">⚡</tspan></text>

<!-- full-banner scanner sweep -->
<g clip-path="url(#bannerBox)" opacity="0">
  <animate attributeName="opacity" from="0" to="1" dur=".6s" begin="3s" fill="freeze"/>
  <g>
    <animateTransform attributeName="transform" type="translate" values="0,-40;0,780" dur="3.5s" begin="3.2s" repeatCount="indefinite"/>
    <rect x="0" y="-34" width="1280" height="34" fill="url(#scanTrailL)"/>
    <rect x="0" y="0" width="1280" height="2.6" fill="url(#scanEdgeL)" opacity=".5" filter="url(#glow)"/>
  </g>
</g>
</svg>'''

with open('vishal-banner.svg', 'w') as f:
    f.write(banner_light_svg)

with open('vishal-banner-light.svg', 'w') as f:
    f.write(banner_light_svg)

print("Generated vishal-banner.svg and vishal-banner-light.svg successfully!")

# ==========================================
# 3. vishal-lanyard.svg (Developer ID Badge)
# ==========================================
lanyard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 420 660" width="420" height="660" role="img" aria-label="Vishal Gangwar ID card lanyard">
<title>Vishal Gangwar — swinging ID badge</title>
<defs>
<style type="text/css"><![CDATA[
text{{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}}
@keyframes sway{{0%,100%{{transform:rotate(-2.8deg)}}50%{{transform:rotate(2.8deg)}}}}
@keyframes cardWobble{{0%,100%{{transform:rotate(1.2deg)}}50%{{transform:rotate(-1.2deg)}}}}
@keyframes shine{{0%{{transform:translateX(-340px) skewX(-18deg)}}55%,100%{{transform:translateX(420px) skewX(-18deg)}}}}
@keyframes twinkle{{0%,100%{{opacity:0.3;transform:scale(.7)}}50%{{opacity:1;transform:scale(1.1)}}}}
.sway{{transform-origin:210px 6px;animation:sway 4.6s ease-in-out infinite}}
.wob{{transform-origin:210px 300px;animation:cardWobble 4.6s ease-in-out infinite}}
.shine{{animation:shine 4.5s ease-in-out infinite}}
.tw{{transform-box:fill-box;transform-origin:center;animation:twinkle 2.8s ease-in-out infinite}}
]]></style>

<linearGradient id="strapg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#0369a1"/><stop offset="50%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#0369a1"/>
</linearGradient>
<linearGradient id="cardg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#0f1d36"/><stop offset="100%" stop-color="#070e1c"/>
</linearGradient>
<linearGradient id="cardborder" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#38bdf8;#60a5fa;#22d3ee" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#60a5fa;#22d3ee;#38bdf8;#60a5fa" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="metal" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0%" stop-color="#c8ccd6"/><stop offset="45%" stop-color="#8a90a0"/><stop offset="55%" stop-color="#6a7080"/><stop offset="100%" stop-color="#9aa0b0"/>
</linearGradient>
<linearGradient id="shineg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".15"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/>
</linearGradient>
<linearGradient id="nameg2" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#38bdf8;#22d3ee" dur="5s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#38bdf8;#60a5fa;#38bdf8" dur="5s" repeatCount="indefinite"/></stop>
</linearGradient>
<radialGradient id="lglow"><stop offset="0%" stop-color="#22d3ee" stop-opacity=".20"/><stop offset="100%" stop-color="#22d3ee" stop-opacity="0"/></radialGradient>
<filter id="glow2"><feGaussianBlur stdDeviation="1.8" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="cardShadow"><feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#000" flood-opacity=".55"/></filter>
<clipPath id="cardclip"><rect x="82" y="298" width="256" height="330" rx="20"/></clipPath>
<clipPath id="avatarclip"><circle cx="210" cy="412" r="59"/></clipPath>
</defs>

<!-- ambient background glow behind badge -->
<circle cx="210" cy="450" r="160" fill="url(#lglow)"/>

<!-- sparkles -->
<g class="tw" style="animation-delay:.5s"><path d="M52 350l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#22d3ee"/></g>
<g class="tw" style="animation-delay:1.8s"><path d="M365 370l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#38bdf8"/></g>
<g class="tw" style="animation-delay:2.7s"><path d="M52 480l2.4 6.4 6.4 2.4-6.4 2.4-2.4 6.4-2.4-6.4-6.4-2.4 6.4-2.4z" fill="#818cf8"/></g>

<!-- pendulum sway (guaranteed in-viewport from frame 0) -->
<g class="sway">

  <!-- Strap -->
  <g>
    <path d="M191 -6 L229 -6 L226 236 L194 236 Z" fill="url(#strapg)"/>
    <line x1="196" y1="0" x2="198.5" y2="234" stroke="#fff" stroke-opacity=".55" stroke-width="1" stroke-dasharray="4 3"/>
    <line x1="224" y1="0" x2="221.5" y2="234" stroke="#fff" stroke-opacity=".55" stroke-width="1" stroke-dasharray="4 3"/>
    <text x="0" y="0" font-size="10.5" font-weight="bold" fill="#fff" opacity=".92" letter-spacing="2" transform="translate(214,18) rotate(90)">VISHAL.DEV ⚡ CODE ⚡ VISHAL.DEV</text>
  </g>

  <!-- Clasp + ring -->
  <rect x="188" y="232" width="44" height="26" rx="6" fill="url(#metal)" stroke="#334155" stroke-width="1"/>
  <rect x="199" y="238" width="22" height="7" rx="3.5" fill="#1e293b"/>
  <circle cx="210" cy="272" r="14" fill="none" stroke="url(#metal)" stroke-width="5.5"/>

  <!-- Card (secondary wobble) -->
  <g class="wob">
    <rect x="82" y="298" width="256" height="330" rx="20" fill="url(#cardg)" stroke="url(#cardborder)" stroke-width="2" filter="url(#cardShadow)"/>
    <!-- slot -->
    <rect x="180" y="310" width="60" height="10" rx="5" fill="#040914" stroke="#1e3a5f" stroke-width="1"/>

    <g clip-path="url(#cardclip)">
      <!-- header band -->
      <rect x="82" y="298" width="256" height="34" fill="#0b172a" opacity=".85"/>
      <text x="98" y="345" font-size="9" fill="#94a3b8" letter-spacing="1.5">DEVELOPER ID</text>
      <text x="322" y="345" text-anchor="end" font-size="9" font-weight="bold" fill="#22d3ee" letter-spacing="1.5">VG-176</text>

      <!-- Avatar: Perfectly centered circular crop with even padding -->
      <circle cx="210" cy="412" r="59" fill="#0f172a" stroke="url(#cardborder)" stroke-width="2.5"/>
      <image x="151" y="353" width="118" height="118" clip-path="url(#avatarclip)" href="data:image/png;base64,{id_avatar_b64}" xlink:href="data:image/png;base64,{id_avatar_b64}"/>

      <!-- Name: Vishal Gangwar (Pacifico vector outlines, centered at x=103) -->
      <g transform="translate(103,516)" fill="url(#nameg2)" filter="url(#glow2)">
{lanyard_letters_xml}      </g>
      <text x="210" y="540" text-anchor="middle" font-size="11" fill="#38bdf8" font-weight="bold" letter-spacing="2.5">FULL STACK DEVELOPER</text>
      <text x="210" y="558" text-anchor="middle" font-size="10.5" fill="#94a3b8">@vishalgangwar176</text>

      <line x1="100" y1="572" x2="320" y2="572" stroke="#1e293b" stroke-width="1"/>

      <!-- barcode + tag -->
      <g transform="translate(100,584)">
        <rect x="0" y="0" width="2.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="5.0" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="9.0" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="12.0" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="16.0" y="0" width="4" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="21.5" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="26.0" y="0" width="4" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="31.5" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="34.5" y="0" width="4" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="41.0" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="45.5" y="0" width="2.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="50.5" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="54.5" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="58.5" y="0" width="2.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="63.5" y="0" width="2.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="67.5" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="72.0" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="76.5" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="81.0" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="84.0" y="0" width="2.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="89.0" y="0" width="1.5" height="26" fill="#e2e8f0" opacity=".85"/>
        <rect x="93.5" y="0" width="4" height="26" fill="#e2e8f0" opacity=".85"/>
      </g>
      <text x="320" y="600" text-anchor="end" font-size="8.5" fill="#94a3b8">REACT • NODE.JS</text>
      <text x="320" y="612" text-anchor="end" font-size="8.5" fill="#94a3b8">PYTHON • SQL</text>

      <!-- holo shine sweep -->
      <rect class="shine" x="82" y="288" width="120" height="360" fill="url(#shineg)"/>
    </g>
  </g>
</g>

<text x="210" y="652" text-anchor="middle" font-size="10" fill="#94a3b8" opacity="0.85">— swinging ID badge ⚡ —</text>
</svg>'''

with open('vishal-lanyard.svg', 'w') as f:
    f.write(lanyard_svg)

print("Generated vishal-lanyard.svg successfully!")

# ==========================================
# 4. vishal-stats.svg (Stats Card)
# ==========================================
stats_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 232" width="500" height="232" role="img" aria-label="Vishal Gangwar's GitHub stats">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeSlide{from{opacity:0;transform:translateX(-14px)}to{opacity:1;transform:translateX(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes rankPulse{0%,100%{opacity:.85}50%{opacity:1}}
@keyframes shineX{0%{transform:translateX(-160px) skewX(-15deg)}60%,100%{transform:translateX(560px) skewX(-15deg)}}
.row{opacity:0;animation:fadeSlide .5s ease forwards}
.rk{animation:rankPulse 2.4s ease-in-out infinite}
.sh{animation:shineX 4.5s ease-in-out 2.4s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#38bdf8;#22d3ee" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#38bdf8;#60a5fa;#38bdf8" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="ringg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0%" stop-color="#22d3ee"/><stop offset="100%" stop-color="#3b82f6"/>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".07"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cc"><rect x="1" y="1" width="498" height="230" rx="14"/></clipPath>
<filter id="g"><feGaussianBlur stdDeviation="2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect x="1" y="1" width="498" height="230" rx="14" fill="#0b172a" stroke="url(#tg)" stroke-width="1.5"/>
<text x="24" y="38" font-size="16" font-weight="bold" fill="url(#tg)">⚡ Vishal Gangwar's GitHub Stats</text>

  <g class="row" style="animation-delay:0.50s">
    <text x="24" y="74" font-size="14">⭐</text>
    <text x="52" y="74" font-size="13.5" fill="#c9d1d9">Total Stars Earned:</text>
    <text x="316" y="74" text-anchor="end" font-size="14" font-weight="bold" fill="#fde047">20+</text>
  </g>
  <g class="row" style="animation-delay:0.72s">
    <text x="24" y="105" font-size="14">💻</text>
    <text x="52" y="105" font-size="13.5" fill="#c9d1d9">Total Commits:</text>
    <text x="316" y="105" text-anchor="end" font-size="14" font-weight="bold" fill="#38bdf8">300+</text>
  </g>
  <g class="row" style="animation-delay:0.94s">
    <text x="24" y="136" font-size="14">📦</text>
    <text x="52" y="136" font-size="13.5" fill="#c9d1d9">Public Repositories:</text>
    <text x="316" y="136" text-anchor="end" font-size="14" font-weight="bold" fill="#4ade80">12+</text>
  </g>
  <g class="row" style="animation-delay:1.16s">
    <text x="24" y="167" font-size="14">👥</text>
    <text x="52" y="167" font-size="13.5" fill="#c9d1d9">Total Followers:</text>
    <text x="316" y="167" text-anchor="end" font-size="14" font-weight="bold" fill="#818cf8">15+</text>
  </g>
  <g class="row" style="animation-delay:1.38s">
    <text x="24" y="198" font-size="14">🚀</text>
    <text x="52" y="198" font-size="13.5" fill="#c9d1d9">Hackathons &amp; Challenges:</text>
    <text x="316" y="198" text-anchor="end" font-size="14" font-weight="bold" fill="#22d3ee">4</text>
  </g>

<!-- Rank ring -->
<g transform="translate(408,138)">
  <circle r="52" fill="none" stroke="#1e293b" stroke-width="9"/>
  <circle r="52" fill="none" stroke="url(#ringg)" stroke-width="9" stroke-linecap="round"
    stroke-dasharray="270 326.7" stroke-dashoffset="270" transform="rotate(-90)">
    <animate attributeName="stroke-dashoffset" from="270" to="0" dur="1.6s" begin=".6s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
  </circle>
  <text class="rk" y="14" text-anchor="middle" font-size="36" font-weight="bold" fill="#22d3ee" filter="url(#g)">A+</text>
  <text y="76" text-anchor="middle" font-size="10.5" fill="#94a3b8" opacity="0" style="animation:fadeIn .5s ease 1.8s forwards">RANK</text>
</g>

<g clip-path="url(#cc)"><rect class="sh" x="0" y="0" width="120" height="232" fill="url(#shg)"/></g>
</svg>'''

with open('vishal-stats.svg', 'w') as f:
    f.write(stats_svg)

print("Generated vishal-stats.svg successfully!")

# ==========================================
# 5. vishal-langs.svg (Top Languages)
# ==========================================
langs_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 282" width="420" height="282" role="img" aria-label="Top languages">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes fadeUp{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes shineX{0%{transform:translateX(-140px)}60%,100%{transform:translateX(460px)}}
.row{opacity:0;animation:fadeUp .5s ease forwards}
.sh{animation:shineX 4s ease-in-out 2.2s infinite}
]]></style>
<linearGradient id="tg" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0%"><animate attributeName="stop-color" values="#22d3ee;#38bdf8;#22d3ee" dur="6s" repeatCount="indefinite"/></stop>
  <stop offset="100%"><animate attributeName="stop-color" values="#38bdf8;#60a5fa;#38bdf8" dur="6s" repeatCount="indefinite"/></stop>
</linearGradient>
<linearGradient id="shg" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".08"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="cardc"><rect x="1" y="1" width="418" height="280" rx="14"/></clipPath>
<clipPath id="stackc"><rect x="20" y="58" width="0" height="11" rx="5.5"><animate attributeName="width" from="0" to="380" dur="1.4s" begin=".4s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/></rect></clipPath>
</defs>
<rect x="1" y="1" width="418" height="280" rx="14" fill="#0b172a" stroke="url(#tg)" stroke-width="1.5"/>
<text x="20" y="34" font-size="16" font-weight="bold" fill="url(#tg)">📊 Top Languages</text>
<g clip-path="url(#stackc)">
  <rect x="20.0" y="58" width="144.4" height="11" fill="#fde047"/>
  <rect x="164.4" y="58" width="102.6" height="11" fill="#38bdf8"/>
  <rect x="267.0" y="58" width="68.4" height="11" fill="#3b82f6"/>
  <rect x="335.4" y="58" width="45.6" height="11" fill="#6366f1"/>
  <rect x="381.0" y="58" width="19.0" height="11" fill="#22d3ee"/>
</g>

  <g class="row" style="animation-delay:0.90s">
    <circle cx="26" cy="91" r="5" fill="#fde047"/>
    <text x="40" y="96" font-size="13" fill="#e6edf3" font-weight="bold">JavaScript</text>
    <text x="396" y="96" text-anchor="end" font-size="13" fill="#fde047" font-weight="bold">38.0%</text>
    <rect x="40" y="104" width="268" height="9" rx="4.5" fill="#1e293b"/>
    <rect class="bar" x="40" y="104" width="101.8" height="9" rx="4.5" fill="#fde047">
      <animate attributeName="width" from="0" to="101.8" dur="1.1s" begin="1.05s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.25s">
    <circle cx="26" cy="133" r="5" fill="#38bdf8"/>
    <text x="40" y="138" font-size="13" fill="#e6edf3" font-weight="bold">TypeScript</text>
    <text x="396" y="138" text-anchor="end" font-size="13" fill="#38bdf8" font-weight="bold">27.0%</text>
    <rect x="40" y="146" width="268" height="9" rx="4.5" fill="#1e293b"/>
    <rect class="bar" x="40" y="146" width="72.3" height="9" rx="4.5" fill="#38bdf8">
      <animate attributeName="width" from="0" to="72.3" dur="1.1s" begin="1.40s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.60s">
    <circle cx="26" cy="175" r="5" fill="#3b82f6"/>
    <text x="40" y="180" font-size="13" fill="#e6edf3" font-weight="bold">Python</text>
    <text x="396" y="180" text-anchor="end" font-size="13" fill="#3b82f6" font-weight="bold">18.0%</text>
    <rect x="40" y="188" width="268" height="9" rx="4.5" fill="#1e293b"/>
    <rect class="bar" x="40" y="188" width="48.2" height="9" rx="4.5" fill="#3b82f6">
      <animate attributeName="width" from="0" to="48.2" dur="1.1s" begin="1.75s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
  <g class="row" style="animation-delay:1.95s">
    <circle cx="26" cy="217" r="5" fill="#6366f1"/>
    <text x="40" y="222" font-size="13" fill="#e6edf3" font-weight="bold">C++</text>
    <text x="396" y="222" text-anchor="end" font-size="13" fill="#6366f1" font-weight="bold">12.0%</text>
    <rect x="40" y="230" width="268" height="9" rx="4.5" fill="#1e293b"/>
    <rect class="bar" x="40" y="230" width="32.1" height="9" rx="4.5" fill="#6366f1">
      <animate attributeName="width" from="0" to="32.1" dur="1.1s" begin="2.10s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
<g clip-path="url(#cardc)"><rect class="sh" x="0" y="0" width="100" height="282" fill="url(#shg)" transform="skewX(-15)"/></g>
</svg>'''

with open('vishal-langs.svg', 'w') as f:
    f.write(langs_svg)

print("Generated vishal-langs.svg successfully!")

# ==========================================
# 6. vishal-trophies.svg (Trophies Row)
# ==========================================
trophies_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1092 168" width="1092" height="168" role="img" aria-label="GitHub trophies">
<defs><style><![CDATA[
text{font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
@keyframes popCell{0%{opacity:0;transform:translateY(16px) scale(.85)}70%{opacity:1;transform:translateY(-3px) scale(1.03)}100%{opacity:1;transform:translateY(0) scale(1)}}
@keyframes rankGlow{0%,100%{opacity:.75}50%{opacity:1}}
@keyframes shineX2{0%{transform:translateX(-200px) skewX(-15deg)}60%,100%{transform:translateX(1172px) skewX(-15deg)}}
.cell{opacity:0;animation:popCell .55s cubic-bezier(.2,.8,.3,1.2) forwards;transform-box:fill-box;transform-origin:center}
.rk{animation:rankGlow 2.2s ease-in-out infinite}
.sh2{animation:shineX2 5s ease-in-out 2s infinite}
]]></style>
<linearGradient id="shg2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#fff" stop-opacity="0"/><stop offset="50%" stop-color="#fff" stop-opacity=".07"/><stop offset="100%" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="tc"><rect x="0" y="0" width="1092" height="168" rx="14"/></clipPath>
</defs>

  <!-- Cell 1: Full Stack Architect -->
  <g class="cell" style="animation-delay:0.30s">
    <rect x="12" y="12" width="168" height="144" rx="14" fill="#0b172a" stroke="#22d3ee" stroke-opacity=".6" stroke-width="1.3"/>
    <text x="96.0" y="52" text-anchor="middle" font-size="30">⚡</text>
    <text class="rk" x="164" y="40" text-anchor="end" font-size="24" font-weight="bold" fill="#22d3ee" style="animation-delay:0.70s">SSS</text>
    <text x="96.0" y="90" text-anchor="middle" font-size="13" font-weight="bold" fill="#e6edf3">Full-Stack Dev</text>
    <text x="96.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8">Web Apps x8</text>
    <rect x="30" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="30" y="124" width="0" height="5" rx="2.5" fill="#22d3ee">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.60s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 2: Starstruck -->
  <g class="cell" style="animation-delay:0.48s">
    <rect x="192" y="12" width="168" height="144" rx="14" fill="#0b172a" stroke="#fde047" stroke-opacity=".6" stroke-width="1.3"/>
    <text x="276.0" y="52" text-anchor="middle" font-size="30">🌟</text>
    <text class="rk" x="344" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#fde047" style="animation-delay:0.88s">S</text>
    <text x="276.0" y="90" text-anchor="middle" font-size="13" font-weight="bold" fill="#e6edf3">Starstruck</text>
    <text x="276.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8">Stars 20+</text>
    <rect x="210" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="210" y="124" width="0" height="5" rx="2.5" fill="#fde047">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.78s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 3: TrackShift Innovator -->
  <g class="cell" style="animation-delay:0.66s">
    <rect x="372" y="12" width="168" height="144" rx="14" fill="#0b172a" stroke="#38bdf8" stroke-opacity=".6" stroke-width="1.3"/>
    <text x="456.0" y="52" text-anchor="middle" font-size="30">🏎️</text>
    <text class="rk" x="524" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#38bdf8" style="animation-delay:1.06s">S</text>
    <text x="456.0" y="90" text-anchor="middle" font-size="13" font-weight="bold" fill="#e6edf3">DEGRAD-X</text>
    <text x="456.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8">TrackShift AI</text>
    <rect x="390" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="390" y="124" width="0" height="5" rx="2.5" fill="#38bdf8">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="0.96s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 4: Security Vanguard -->
  <g class="cell" style="animation-delay:0.84s">
    <rect x="552" y="12" width="168" height="144" rx="14" fill="#0b172a" stroke="#60a5fa" stroke-opacity=".6" stroke-width="1.3"/>
    <text x="636.0" y="52" text-anchor="middle" font-size="30">🛡️</text>
    <text class="rk" x="704" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#60a5fa" style="animation-delay:1.24s">A</text>
    <text x="636.0" y="90" text-anchor="middle" font-size="13" font-weight="bold" fill="#e6edf3">CipherShield</text>
    <text x="636.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8">3D IAM Security</text>
    <rect x="570" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="570" y="124" width="0" height="5" rx="2.5" fill="#60a5fa">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.14s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 5: Committer -->
  <g class="cell" style="animation-delay:1.02s">
    <rect x="732" y="12" width="168" height="144" rx="14" fill="#0b172a" stroke="#22d3ee" stroke-opacity=".6" stroke-width="1.3"/>
    <text x="816.0" y="52" text-anchor="middle" font-size="30">💻</text>
    <text class="rk" x="884" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#22d3ee" style="animation-delay:1.42s">A</text>
    <text x="816.0" y="90" text-anchor="middle" font-size="13" font-weight="bold" fill="#e6edf3">Committer</text>
    <text x="816.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8">Commits 300+</text>
    <rect x="750" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="750" y="124" width="0" height="5" rx="2.5" fill="#22d3ee">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.32s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>

  <!-- Cell 6: Open Source Creator -->
  <g class="cell" style="animation-delay:1.20s">
    <rect x="912" y="12" width="168" height="144" rx="14" fill="#0b172a" stroke="#4ade80" stroke-opacity=".6" stroke-width="1.3"/>
    <text x="996.0" y="52" text-anchor="middle" font-size="30">📦</text>
    <text class="rk" x="1064" y="40" text-anchor="end" font-size="30" font-weight="bold" fill="#4ade80" style="animation-delay:1.60s">A</text>
    <text x="996.0" y="90" text-anchor="middle" font-size="13" font-weight="bold" fill="#e6edf3">Creator</text>
    <text x="996.0" y="112" text-anchor="middle" font-size="11" fill="#94a3b8">Repos 12+</text>
    <rect x="930" y="124" width="132" height="5" rx="2.5" fill="#1e293b"/>
    <rect x="930" y="124" width="0" height="5" rx="2.5" fill="#4ade80">
      <animate attributeName="width" from="0" to="132" dur="1s" begin="1.50s" fill="freeze" calcMode="spline" keySplines=".2 .8 .3 1"/>
    </rect>
  </g>
<g clip-path="url(#tc)"><rect class="sh2" x="0" y="0" width="140" height="168" fill="url(#shg2)"/></g>
</svg>'''

with open('vishal-trophies.svg', 'w') as f:
    f.write(trophies_svg)

print("Generated vishal-trophies.svg successfully!")

# ==========================================
# 7. github-snake-blue.svg (Local Animated Snake SVG)
# ==========================================
# We can adapt megha's snake SVG colors from pink/purple to cyan/blue:
# Snake body: #ff7eb6 -> #22d3ee
# Dots/track: #170e28 -> #0b172a, #2d1b4e -> #0e294d, #5b2a86 -> #0284c7, #8b5cf6 -> #0ea5e9, #c084fc -> #38bdf8, #ff7eb6 -> #22d3ee
# github-snake-blue.svg already exists or downloaded

if os.path.exists('Screenshot_2026-09-27_at_11.00.27_PM.png'):
    # Let's read raw github-snake-pink.svg from meghamittal0920 if available
    try:
        import urllib.request
        snake_url = "https://raw.githubusercontent.com/Meghamittal0920/Meghamittal0920/output/github-snake-pink.svg"
        req = urllib.request.Request(snake_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp:
            pink_snake = resp.read().decode('utf-8')
            # Transform palette
            blue_snake = pink_snake.replace('#ff7eb6', '#22d3ee')
            blue_snake = blue_snake.replace('#c084fc', '#38bdf8')
            blue_snake = blue_snake.replace('#8b5cf6', '#0ea5e9')
            blue_snake = blue_snake.replace('#5b2a86', '#0284c7')
            blue_snake = blue_snake.replace('#2d1b4e', '#0e294d')
            blue_snake = blue_snake.replace('#170e28', '#0b172a')
            with open('github-snake-blue.svg', 'w') as sf:
                sf.write(blue_snake)
            print("Generated github-snake-blue.svg from source with cyan/blue palette!")
    except Exception as e:
        print("Could not download remote snake, generating fallback:", e)

