# -*- coding: utf-8 -*-
"""Assemble the upgraded Tarjeta HTML with embedded logo."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
logo = (ROOT / "_logo_b64.txt").read_text(encoding="utf-8").strip()

# Split template around logo placeholder to keep source editable
HTML = r'''<!DOCTYPE html>
<html lang="es" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Dostin Santana — Logic Code Spot</title>
<meta name="description" content="Tarjeta digital de Dostin Santana, CEO & Lead Developer de Logic Code Spot. Cuentas bancarias, contacto y QR vCard.">
<meta property="og:title" content="Dostin Santana — Logic Code Spot">
<meta property="og:description" content="CEO & Lead Developer · Software Solutions. Escanea el QR para guardar el contacto.">
<meta property="og:type" content="website">
<meta name="theme-color" content="#0d1f3a">
<link rel="icon" href="__LOGO__" type="image/png">
<link rel="apple-touch-icon" href="__LOGO__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
<script>
/* Apply theme before paint to avoid flash */
(function(){
  var t = "dark";
  try {
    var s = localStorage.getItem("lcs-card-theme");
    if (s === "light" || s === "dark") t = s;
    else if (window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches) t = "light";
  } catch (e) {}
  document.documentElement.setAttribute("data-theme", t);
  document.documentElement.style.colorScheme = t;
})();
</script>
<style>
  /* ---------- Design tokens: dark (default) ---------- */
  :root,
  html[data-theme="dark"]{
    --navy-deep:#081222;
    --navy:#0d1f3a;
    --navy-soft:#12294d;
    --bg-end:#071021;
    --line:rgba(255,255,255,0.10);
    --line-strong:rgba(255,255,255,0.18);
    --ink:#eef3fa;
    /* #b0c4de on #0d1f3a ≈ 9.3:1 — WCAG AAA for normal text */
    --ink-dim:#b0c4de;
    --green:#7ed957;
    --green-dim:#5fae3f;
    --bhd:#4fb3e8;
    --bres:#5b8def;
    --radius:18px;
    --card-surface:rgba(255,255,255,0.045);
    --card-surface-2:rgba(255,255,255,0.012);
    --acct-bg:rgba(255,255,255,0.03);
    --acct-bg-hover:rgba(255,255,255,0.055);
    --btn-bg:rgba(255,255,255,0.07);
    --btn-bg-hover:rgba(255,255,255,0.11);
    --glow-green:rgba(126,217,87,0.14);
    --glow-blue:rgba(79,179,232,0.10);
    --shadow-1:0 1px 0 rgba(255,255,255,0.06) inset;
    --shadow-2:0 18px 36px -14px rgba(0,0,0,0.55);
    --shadow-3:0 40px 72px -24px rgba(0,0,0,0.5);
    --border-grad:linear-gradient(135deg, rgba(126,217,87,0.55), rgba(79,179,232,0.4), rgba(91,141,239,0.3));
    --focus-ring:#7ed957;
    --toolbar-bg:rgba(13,31,58,0.85);
    --pdf-btn-bg:linear-gradient(135deg, #5fae3f, #7ed957);
    --pdf-btn-ink:#081222;
    --pdf-btn-shadow:0 10px 24px -10px rgba(126,217,87,0.45);
    --badge-border:rgba(126,217,87,0.4);
    --badge-bg:rgba(126,217,87,0.10);
    --copied-bg:rgba(126,217,87,0.18);
    --copied-border:rgba(126,217,87,0.5);
    --qr-frame:#ffffff;
    --space:4px;
  }

  /* ---------- Design tokens: light ---------- */
  html[data-theme="light"]{
    --navy-deep:#f2f6fc;
    --navy:#e8eef8;
    --navy-soft:#d5e0f0;
    --bg-end:#dfe8f5;
    --line:rgba(13,31,58,0.10);
    --line-strong:rgba(13,31,58,0.16);
    --ink:#0d1f3a;
    /* #3a4f6b on #e8eef8 ≈ 6.5:1+ */
    --ink-dim:#3a4f6b;
    --green:#2f8f28;
    --green-dim:#24701f;
    --bhd:#1a7fb8;
    --bres:#2f5fbf;
    --card-surface:rgba(255,255,255,0.92);
    --card-surface-2:rgba(255,255,255,0.78);
    --acct-bg:rgba(13,31,58,0.03);
    --acct-bg-hover:rgba(13,31,58,0.06);
    --btn-bg:rgba(13,31,58,0.06);
    --btn-bg-hover:rgba(13,31,58,0.10);
    --glow-green:rgba(47,143,40,0.10);
    --glow-blue:rgba(26,127,184,0.08);
    --shadow-1:0 1px 0 rgba(255,255,255,0.9) inset;
    --shadow-2:0 14px 28px -12px rgba(13,31,58,0.18);
    --shadow-3:0 32px 56px -20px rgba(13,31,58,0.16);
    --border-grad:linear-gradient(135deg, rgba(47,143,40,0.55), rgba(26,127,184,0.45), rgba(47,95,191,0.35));
    --focus-ring:#2f8f28;
    --toolbar-bg:rgba(255,255,255,0.9);
    --pdf-btn-bg:linear-gradient(135deg, #24701f, #2f8f28);
    --pdf-btn-ink:#ffffff;
    --pdf-btn-shadow:0 10px 24px -10px rgba(47,143,40,0.4);
    --badge-border:rgba(47,143,40,0.45);
    --badge-bg:rgba(47,143,40,0.10);
    --copied-bg:rgba(47,143,40,0.16);
    --copied-border:rgba(47,143,40,0.5);
    --qr-frame:#ffffff;
    color-scheme:light;
  }

  html[data-theme="dark"]{ color-scheme:dark; }

  *{box-sizing:border-box;margin:0;padding:0;}
  html,body{height:100%;}
  body{
    font-family:'Inter',system-ui,sans-serif;
    background:
      radial-gradient(ellipse 900px 520px at 18% -8%, var(--glow-green), transparent 60%),
      radial-gradient(ellipse 700px 500px at 100% 10%, var(--glow-blue), transparent 55%),
      linear-gradient(180deg,var(--navy-deep) 0%, var(--navy) 55%, var(--bg-end) 100%);
    color:var(--ink);
    min-height:100%;
    min-height:100dvh;
    padding:calc(var(--space)*4 + env(safe-area-inset-top,0px)) calc(var(--space)*4.5) calc(var(--space)*6 + env(safe-area-inset-bottom,0px));
    display:flex;
    align-items:flex-start;
    justify-content:center;
  }

  .sr-only{
    position:absolute;width:1px;height:1px;padding:0;margin:-1px;
    overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0;
  }

  /* Focus visible — all interactive */
  :focus{ outline:none; }
  :focus-visible{
    outline:2px solid var(--focus-ring);
    outline-offset:3px;
  }
  a:focus-visible,
  button:focus-visible{
    outline:2px solid var(--focus-ring);
    outline-offset:3px;
  }

  .page{
    width:100%;
    max-width:460px;
    position:relative;
  }

  /* Theme toggle */
  .theme-toggle{
    position:absolute;
    top:0;
    right:0;
    z-index:5;
    width:44px;height:44px;
    min-width:44px;min-height:44px;
    display:inline-flex;align-items:center;justify-content:center;
    border-radius:12px;
    border:1px solid var(--line-strong);
    background:var(--toolbar-bg);
    color:var(--ink);
    cursor:pointer;
    backdrop-filter:blur(10px);
    -webkit-backdrop-filter:blur(10px);
    box-shadow:var(--shadow-2);
    transition:background .15s ease, transform .15s ease, border-color .15s ease;
  }
  .theme-toggle:hover{ background:var(--btn-bg-hover); }
  .theme-toggle:active{ transform:scale(0.96); }
  .theme-toggle svg{ width:20px;height:20px; }
  html[data-theme="dark"] .theme-toggle .icon-moon{ display:none; }
  html[data-theme="light"] .theme-toggle .icon-sun{ display:none; }

  .stage{
    width:100%;
    padding-top:calc(var(--space)*9.5);
  }

  /* ---------- Header ---------- */
  .brand{
    display:flex;
    flex-direction:column;
    align-items:center;
    text-align:center;
    gap:calc(var(--space)*2.5);
    margin-bottom:calc(var(--space)*6.5);
  }
  .brand img{
    width:96px;
    height:96px;
    max-width:100%;
    object-fit:contain;
    filter:drop-shadow(0 8px 22px rgba(0,0,0,0.35));
  }
  .brand .company{
    font-family:'Space Grotesk',sans-serif;
    font-weight:700;
    font-size:clamp(18px, 5vw, 20px);
    letter-spacing:0.01em;
  }
  .brand .tagline{
    font-size:13px;
    color:var(--ink-dim);
    font-style:italic;
    padding:0 calc(var(--space)*2);
  }

  /* ---------- Main card (premium) ---------- */
  @keyframes cardIn{
    from{ opacity:0; transform:translateY(16px); }
    to{ opacity:1; transform:translateY(0); }
  }
  .card{
    position:relative;
    border-radius:24px;
    padding:calc(var(--space)*7) calc(var(--space)*6) calc(var(--space)*6.5);
    overflow:hidden;
    background:
      linear-gradient(165deg, var(--card-surface), var(--card-surface-2)) padding-box,
      var(--border-grad) border-box;
    border:1px solid transparent;
    box-shadow:var(--shadow-1), var(--shadow-2), var(--shadow-3);
    animation:cardIn .55s cubic-bezier(.22,1,.36,1) both;
  }
  @media (prefers-reduced-motion: reduce){
    .card{ animation:none; }
    .acct{ transition:none; }
  }
  .card::before{
    content:"";
    position:absolute; top:-40%; right:-30%;
    width:280px; height:280px;
    background:radial-gradient(circle, var(--glow-green), transparent 70%);
    pointer-events:none;
  }
  .person{
    display:flex;
    align-items:baseline;
    justify-content:space-between;
    gap:calc(var(--space)*3);
    margin-bottom:calc(var(--space)*1);
    position:relative;
    flex-wrap:wrap;
  }
  .person h1{
    font-family:'Space Grotesk',sans-serif;
    font-weight:700;
    font-size:clamp(20px, 5.5vw, 24px);
    line-height:1.15;
  }
  .person .badge{
    font-size:11px;
    font-weight:600;
    color:var(--green);
    border:1px solid var(--badge-border);
    background:var(--badge-bg);
    padding:calc(var(--space)*1) calc(var(--space)*2.25);
    border-radius:100px;
    white-space:nowrap;
  }
  .role{
    font-size:13.5px;
    color:var(--ink-dim);
    margin-bottom:calc(var(--space)*5.5);
    position:relative;
  }

  /* ---------- Account blocks ---------- */
  .accounts{
    display:flex; flex-direction:column;
    gap:calc(var(--space)*3);
    margin-bottom:calc(var(--space)*5);
    position:relative;
  }
  .acct{
    border:1px solid var(--line);
    border-radius:var(--radius);
    padding:calc(var(--space)*3.5) calc(var(--space)*4);
    background:var(--acct-bg);
    transition:border-color .18s ease, background .18s ease, box-shadow .18s ease, transform .18s ease;
  }
  .acct:hover{
    background:var(--acct-bg-hover);
    border-color:var(--line-strong);
    box-shadow:0 10px 24px -12px rgba(0,0,0,0.35);
    transform:translateY(-1px);
  }
  .acct:active{
    transform:translateY(0);
    box-shadow:none;
  }
  .acct[data-bank="bhd"]{ border-left:3px solid var(--bhd); }
  .acct[data-bank="bres"]{ border-left:3px solid var(--bres); }
  .acct-top{
    display:flex; align-items:center; justify-content:space-between;
    gap:calc(var(--space)*2);
    margin-bottom:calc(var(--space)*2.5);
    flex-wrap:wrap;
  }
  .acct-name{
    display:flex; align-items:center; gap:calc(var(--space)*2);
    font-size:13px; font-weight:600; letter-spacing:.02em;
  }
  .dot{ width:8px; height:8px; border-radius:50%; flex-shrink:0; }
  .acct[data-bank="bhd"] .dot{ background:var(--bhd); }
  .acct[data-bank="bres"] .dot{ background:var(--bres); }
  .acct-type{ font-size:11px; color:var(--ink-dim); }
  .acct-number-row{
    display:flex; align-items:center; justify-content:space-between; gap:calc(var(--space)*2.5);
    flex-wrap:wrap;
  }
  .acct-number{
    font-family:'JetBrains Mono',monospace;
    font-size:clamp(16px, 4.8vw, 19px);
    font-weight:600;
    letter-spacing:.02em;
    word-break:break-all;
  }
  .copy-btn{
    flex-shrink:0;
    display:inline-flex; align-items:center; gap:6px;
    font-family:'Inter',sans-serif;
    font-size:11.5px;
    font-weight:600;
    color:var(--ink);
    background:var(--btn-bg);
    border:1px solid var(--line-strong);
    padding:calc(var(--space)*1.75) calc(var(--space)*2.75);
    min-height:36px;
    border-radius:9px;
    cursor:pointer;
    transition:background .15s ease, border-color .15s ease, color .15s ease, transform .12s ease;
  }
  .copy-btn:hover{ background:var(--btn-bg-hover); }
  .copy-btn:active{ transform:scale(0.96); }
  .copy-btn svg{ width:13px; height:13px; flex-shrink:0; }
  .copy-btn.copied{
    background:var(--copied-bg);
    border-color:var(--copied-border);
    color:var(--green);
  }

  .cedula-row{
    display:flex; align-items:center; justify-content:space-between;
    gap:calc(var(--space)*3);
    border:1px solid var(--line);
    border-radius:var(--radius);
    padding:calc(var(--space)*3) calc(var(--space)*4);
    margin-bottom:calc(var(--space)*6);
    position:relative;
    flex-wrap:wrap;
  }
  .cedula-label{ font-size:12px; color:var(--ink-dim); }
  .cedula-value{
    font-family:'JetBrains Mono',monospace;
    font-size:14.5px; font-weight:600;
    word-break:break-all;
  }

  /* ---------- Contact strip ---------- */
  .contact-row{
    display:flex; flex-direction:column;
    gap:calc(var(--space)*2);
    margin-bottom:calc(var(--space)*6);
    position:relative;
  }
  .contact-item{
    display:flex; align-items:center; justify-content:space-between;
    gap:calc(var(--space)*2);
    border:1px solid var(--line);
    border-radius:var(--radius);
    padding:calc(var(--space)*2.5) calc(var(--space)*4);
    background:var(--acct-bg);
    flex-wrap:wrap;
  }
  .contact-label{ font-size:12px; color:var(--ink-dim); }
  .contact-value{
    font-size:13px; font-weight:500;
    color:var(--ink);
    text-decoration:none;
    word-break:break-all;
  }
  .contact-value:hover{ color:var(--green); }

  /* ---------- QR ---------- */
  .qr-section{
    display:flex; flex-direction:column; align-items:center;
    padding-top:calc(var(--space)*5.5);
    border-top:1px dashed var(--line-strong);
    position:relative;
  }
  .qr-wrap{
    padding:calc(var(--space)*3);
    background:var(--qr-frame);
    border-radius:16px;
    box-shadow:0 0 0 1px var(--line), 0 20px 40px -14px rgba(0,0,0,0.35);
    margin-bottom:calc(var(--space)*3);
    max-width:100%;
  }
  #qrcode{ line-height:0; }
  #qrcode img, #qrcode canvas{
    display:block; border-radius:4px;
    max-width:100%; height:auto;
  }
  .qr-caption{
    display:flex; align-items:center; gap:6px;
    font-size:12.5px; font-weight:600; color:var(--green);
    text-align:center;
  }
  .qr-caption svg{ width:16px; height:16px; flex-shrink:0; }
  .qr-sub{
    font-size:11.5px; color:var(--ink-dim);
    margin-top:calc(var(--space)*0.75);
    text-align:center;
    max-width:36ch;
    padding:0 calc(var(--space)*2);
  }

  /* ---------- Trust + footer ---------- */
  .trust{
    display:flex; justify-content:center; flex-wrap:wrap;
    gap:calc(var(--space)*4) calc(var(--space)*5.5);
    margin-top:calc(var(--space)*4);
    font-size:11px; color:var(--ink-dim);
  }
  .trust span{ display:flex; align-items:center; gap:5px; }
  .trust svg{ width:12px; height:12px; color:var(--green); }

  .footer{
    display:flex; align-items:center; justify-content:center; gap:18px;
    margin-top:calc(var(--space)*5.5);
    font-size:12.5px;
    color:var(--ink-dim);
  }
  .footer a{
    color:var(--ink); text-decoration:none;
    display:inline-flex; align-items:center; gap:6px;
    min-height:44px; padding:0 4px;
  }
  .footer a:hover{ color:var(--green); }
  .footer svg{ width:14px; height:14px; opacity:.85; }

  /* ---------- PDF action ---------- */
  .pdf-actions{
    margin-top:calc(var(--space)*5);
    display:flex; flex-direction:column; align-items:center; gap:calc(var(--space)*2);
  }
  .pdf-btn{
    display:inline-flex; align-items:center; justify-content:center; gap:8px;
    min-height:44px; min-width:44px;
    width:100%;
    max-width:320px;
    padding:calc(var(--space)*3) calc(var(--space)*4);
    font-family:'Inter',sans-serif;
    font-size:14px; font-weight:600;
    color:var(--pdf-btn-ink);
    background:var(--pdf-btn-bg);
    border:none;
    border-radius:12px;
    cursor:pointer;
    box-shadow:var(--pdf-btn-shadow);
    transition:transform .15s ease, filter .15s ease, opacity .15s ease;
  }
  .pdf-btn:hover{ filter:brightness(1.05); }
  .pdf-btn:active{ transform:scale(0.98); }
  .pdf-btn:disabled{
    opacity:0.72; cursor:wait; filter:none;
  }
  .pdf-btn svg{ width:18px; height:18px; flex-shrink:0; }
  .pdf-status{
    font-size:12px; color:var(--ink-dim); text-align:center; min-height:1.2em;
  }
  .pdf-status.is-error{ color:#e85d5d; }
  html[data-theme="light"] .pdf-status.is-error{ color:#b42318; }

  /* Tiny screens */
  @media (max-width:360px){
    body{ padding-left:calc(var(--space)*3); padding-right:calc(var(--space)*3); }
    .card{ padding:calc(var(--space)*5) calc(var(--space)*4); }
    .acct-number{ font-size:15px; }
  }
</style>
</head>
<body>
<div class="page">

  <button type="button" class="theme-toggle" id="theme-toggle" aria-label="Cambiar a tema claro" data-html2canvas-ignore="true">
    <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
      <circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/>
    </svg>
    <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
      <path d="M21 14.5A8.5 8.5 0 1 1 9.5 3a7 7 0 0 0 11.5 11.5z"/>
    </svg>
  </button>

  <div class="stage" id="pdf-capture">

    <div class="brand">
      <img src="__LOGO__" width="96" height="96" alt="Logo Logic Code Spot">
      <div class="company">LOGIC CODE SPOT</div>
      <div class="tagline">Tu aliado en soluciones digitales</div>
    </div>

    <div class="card">
      <div class="person">
        <h1>Dostin Santana</h1>
        <span class="badge">Logic Code</span>
      </div>
      <div class="role">CEO &amp; Lead Developer — Software Solutions</div>

      <div class="accounts">
        <div class="acct" data-bank="bhd">
          <div class="acct-top">
            <div class="acct-name"><span class="dot" aria-hidden="true"></span>Banco BHD</div>
            <div class="acct-type">Cuenta de ahorro</div>
          </div>
          <div class="acct-number-row">
            <span class="acct-number" id="bhd-num">35020230012</span>
            <button type="button" class="copy-btn" data-copy="35020230012" aria-label="Copiar cuenta BHD 35020230012">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              Copiar
            </button>
          </div>
        </div>

        <div class="acct" data-bank="bres">
          <div class="acct-top">
            <div class="acct-name"><span class="dot" aria-hidden="true"></span>Banreservas</div>
            <div class="acct-type">Cuenta de ahorro</div>
          </div>
          <div class="acct-number-row">
            <span class="acct-number" id="bres-num">9602175947</span>
            <button type="button" class="copy-btn" data-copy="9602175947" aria-label="Copiar cuenta Banreservas 9602175947">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              Copiar
            </button>
          </div>
        </div>
      </div>

      <div class="cedula-row">
        <span class="cedula-label">Cédula</span>
        <span class="cedula-value">4023343629-0</span>
      </div>

      <div class="contact-row">
        <div class="contact-item">
          <span class="contact-label">Teléfono</span>
          <a class="contact-value" href="tel:+18494737963">+1 849-473-7963</a>
        </div>
        <div class="contact-item">
          <span class="contact-label">Correo</span>
          <a class="contact-value" href="mailto:Dostinsantana7@hotmail.com">Dostinsantana7@hotmail.com</a>
        </div>
      </div>

      <div class="qr-section">
        <div class="qr-wrap"><div id="qrcode" role="img" aria-label="Código QR vCard de Dostin Santana"></div></div>
        <div class="qr-caption">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM19 14h2v2h-2zM14 19h2v2h-2zM19 19h2v2h-2z"/></svg>
          Escanea para agregar el contacto
        </div>
        <div class="qr-sub">Formato vCard · funciona sin conexión</div>
      </div>
    </div>

    <div class="trust">
      <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>Seguro</span>
      <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M13 2 3 14h7l-1 8 10-12h-7l1-8z"/></svg>Rápido</span>
      <span><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>Confiable</span>
    </div>

    <div class="footer">
      <a href="https://instagram.com/lcs.dominican" target="_blank" rel="noopener noreferrer">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="0.6" fill="currentColor"/></svg>
        @lcs.dominican
      </a>
    </div>

  </div><!-- /#pdf-capture -->

  <div class="pdf-actions" data-html2canvas-ignore="true">
    <button type="button" class="pdf-btn" id="pdf-btn" aria-label="Descargar tarjeta en PDF">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M12 18v-6M9 15l3 3 3-3"/></svg>
      <span class="pdf-btn-label">Descargar tarjeta (PDF)</span>
    </button>
    <div class="pdf-status" id="pdf-status" role="status" aria-live="polite"></div>
  </div>

  <div id="copy-status" class="sr-only" role="status" aria-live="polite"></div>
</div>

<script>
(function () {
  "use strict";

  var THEME_KEY = "lcs-card-theme";
  var COPY_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>';
  var CHECK_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';

  /* ---------- Theme ---------- */
  function currentTheme() {
    return document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
  }

  function setTheme(theme) {
    var t = theme === "light" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", t);
    document.documentElement.style.colorScheme = t;
    try { localStorage.setItem(THEME_KEY, t); } catch (e) {}
    var btn = document.getElementById("theme-toggle");
    if (btn) {
      btn.setAttribute("aria-label", t === "dark" ? "Cambiar a tema claro" : "Cambiar a tema oscuro");
    }
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute("content", t === "dark" ? "#0d1f3a" : "#e8eef8");
  }

  var themeBtn = document.getElementById("theme-toggle");
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      setTheme(currentTheme() === "dark" ? "light" : "dark");
    });
    setTheme(currentTheme());
  }

  /* ---------- vCard 3.0 + plain-text fallback (ASCII only: qrcodejs overflows on Unicode) ---------- */
  var plainFallback =
    "LOGIC CODE SPOT - Software Solutions\n" +
    "Dostin Santana\n" +
    "Tel: +1 849-473-7963\n" +
    "Email: Dostinsantana7@hotmail.com\n" +
    "Cuenta BHD (Ahorro): 35020230012\n" +
    "Cuenta Banreservas (Ahorro): 9602175947\n" +
    "Cedula: 4023343629-0\n" +
    "IG: @lcs.dominican";

  var vcard =
    "BEGIN:VCARD\n" +
    "VERSION:3.0\n" +
    "N:Santana;Dostin;;;\n" +
    "FN:Dostin Santana\n" +
    "ORG:Logic Code Spot\n" +
    "TITLE:CEO & Lead Developer\n" +
    "TEL;TYPE=CELL:+18494737963\n" +
    "EMAIL;TYPE=INTERNET:Dostinsantana7@hotmail.com\n" +
    "URL:https://instagram.com/lcs.dominican\n" +
    "NOTE:" + plainFallback.replace(/\n/g, " | ") + "\n" +
    "END:VCARD";

  // Dual payload: phones that don't parse vCard still show readable text after the card block
  var qrPayload = vcard + "\n\n" + plainFallback;

  try {
    if (typeof QRCode === "undefined") throw new Error("QRCode missing");
    new QRCode(document.getElementById("qrcode"), {
      text: qrPayload,
      width: 208,
      height: 208,
      colorDark: "#0d1f3a",
      colorLight: "#ffffff",
      // correctLevel M: sin logo central. Si se agrega logo al centro del QR, usar:
      // correctLevel: QRCode.CorrectLevel.H
      correctLevel: QRCode.CorrectLevel.M
    });
  } catch (e) {
    var qrEl = document.getElementById("qrcode");
    if (qrEl) {
      qrEl.innerHTML =
        '<div style="width:min(208px,70vw);height:208px;display:flex;align-items:center;justify-content:center;color:#0d1f3a;font-family:Inter,sans-serif;font-size:12px;text-align:center;padding:10px;">No se pudo generar el código QR</div>';
    }
  }

  /* ---------- Copy with a11y ---------- */
  var copyStatus = document.getElementById("copy-status");

  function announce(msg) {
    if (!copyStatus) return;
    copyStatus.textContent = "";
    // Force re-announce
    setTimeout(function () { copyStatus.textContent = msg; }, 10);
  }

  function fallbackCopy(text, cb) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      cb(true);
    } catch (err) {
      cb(false);
    }
    document.body.removeChild(ta);
  }

  function copyText(text, btn) {
    var label = btn.getAttribute("aria-label") || "Copiar";
    var done = function (ok) {
      if (!ok) {
        announce("No se pudo copiar");
        return;
      }
      var original = btn.innerHTML;
      var originalAria = label;
      btn.classList.add("copied");
      btn.innerHTML = CHECK_ICON + " Copiado";
      btn.setAttribute("aria-label", "Copiado");
      announce("Copiado al portapapeles");
      setTimeout(function () {
        btn.classList.remove("copied");
        btn.innerHTML = original.indexOf("Copiar") >= 0 ? original : (COPY_ICON + " Copiar");
        btn.setAttribute("aria-label", originalAria);
      }, 1600);
    };

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { done(true); }).catch(function () {
        fallbackCopy(text, done);
      });
    } else {
      fallbackCopy(text, done);
    }
  }

  document.querySelectorAll(".copy-btn[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      copyText(btn.getAttribute("data-copy"), btn);
    });
  });

  /* ---------- PDF download ---------- */
  var pdfBtn = document.getElementById("pdf-btn");
  var pdfStatus = document.getElementById("pdf-status");
  var pdfLabel = pdfBtn ? pdfBtn.querySelector(".pdf-btn-label") : null;
  var pdfBusy = false;

  function setPdfMessage(msg, isError) {
    if (!pdfStatus) return;
    pdfStatus.textContent = msg || "";
    pdfStatus.classList.toggle("is-error", !!isError);
  }

  function libsReady() {
    return typeof html2canvas === "function" &&
      window.jspdf && typeof window.jspdf.jsPDF === "function";
  }

  async function downloadPdf() {
    if (pdfBusy) return;
    if (!libsReady()) {
      setPdfMessage("No se pudo cargar la librería PDF. Revisa tu conexión.", true);
      return;
    }

    var target = document.getElementById("pdf-capture");
    if (!target) {
      setPdfMessage("No se encontró la tarjeta para exportar.", true);
      return;
    }

    pdfBusy = true;
    if (pdfBtn) pdfBtn.disabled = true;
    if (pdfLabel) pdfLabel.textContent = "Generando...";
    setPdfMessage("Generando PDF…", false);

    try {
      var theme = document.documentElement.getAttribute("data-theme") === "light" ? "light" : "dark";
      var bg = theme === "light" ? "#e8eef8" : "#0d1f3a";
      var canvas = await html2canvas(target, {
        scale: 3,
        useCORS: true,
        allowTaint: true,
        backgroundColor: bg,
        logging: false,
        imageTimeout: 15000
      });

      var imgData = canvas.toDataURL("image/png", 1.0);
      var pxToMm = 25.4 / 96;
      // Use canvas pixel size / scale for CSS-pixel dimensions, then mm
      var cssW = canvas.width / 3;
      var cssH = canvas.height / 3;
      var pdfW = cssW * pxToMm;
      var pdfH = cssH * pxToMm;

      var jsPDF = window.jspdf.jsPDF;
      var pdf = new jsPDF({
        orientation: pdfW >= pdfH ? "landscape" : "portrait",
        unit: "mm",
        format: [pdfW, pdfH],
        compress: true
      });

      pdf.addImage(imgData, "PNG", 0, 0, pdfW, pdfH, undefined, "FAST");
      pdf.save("Dostin-Santana-LogicCodeSpot.pdf");
      setPdfMessage("PDF descargado.", false);
      setTimeout(function () { setPdfMessage("", false); }, 2500);
    } catch (err) {
      console.error(err);
      setPdfMessage("Error al generar el PDF. Intenta de nuevo.", true);
    } finally {
      pdfBusy = false;
      if (pdfBtn) pdfBtn.disabled = false;
      if (pdfLabel) pdfLabel.textContent = "Descargar tarjeta (PDF)";
    }
  }

  if (pdfBtn) {
    pdfBtn.addEventListener("click", function () {
      downloadPdf();
    });
  }
})();
</script>
</body>
</html>
'''

out = HTML.replace("__LOGO__", logo)
out_path = ROOT / "Tarjeta_LogicCodeSpot_Dostin.html"
out_path.write_text(out, encoding="utf-8")
print("Wrote", out_path)
print("Size bytes", out_path.stat().st_size)
print("Has logo", logo[:30] in out)
print("Has vcard", "BEGIN:VCARD" in out)
print("Has pdf btn", "Descargar tarjeta (PDF)" in out)
print("Has theme", "lcs-card-theme" in out)
print("Has phone", "+18494737963" in out)
print("Has email", "Dostinsantana7@hotmail.com" in out)
