/* AMALOR site chrome (all pages): header states, progress bar, back to top, phone dock and menu with product switch,
   scroll marker in the sections bar, remembered language. No dependencies. */
(function(){
  var d=document,root=d.documentElement,body=d.body;
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hdr=d.getElementById('hdr'),prog=d.getElementById('progress'),top=d.getElementById('totop'),mm=d.getElementById('mmenu');
  if(!hdr)return;
  var hasSub=!!hdr.querySelector('.subnav'),ticking=false;

  /* header: solid once you scroll; on desktop the first row moves away and the sections bar stays */
  function onScroll(){
    var y=window.scrollY,h=root.scrollHeight-innerHeight;
    hdr.classList.toggle('scrolled',y>20);
    hdr.classList.toggle('compact',hasSub&&y>120&&!body.classList.contains('menu-open'));
    if(prog)prog.style.transform='scaleX('+(h>0?y/h:0)+')';
    if(top)top.classList.toggle('show',y>innerHeight*1.2);
    ticking=false;
  }
  addEventListener('scroll',function(){if(!ticking){requestAnimationFrame(onScroll);ticking=true}},{passive:true});
  onScroll();
  if(top)top.addEventListener('click',function(){scrollTo({top:0,behavior:reduce?'auto':'smooth'})});

  /* phone menu: opens from the dock at the bottom centre, shows the sections of the chosen product */
  if(mm){
    var tabs=[].slice.call(mm.querySelectorAll('.mseg [role=tab]')),panels=[].slice.call(mm.querySelectorAll('.mpanel'));
    var cur=(panels.filter(function(p){return !p.hidden})[0]||{dataset:{p:'0'}}).dataset.p;
    var showPanel=function(i){panels.forEach(function(p){p.hidden=p.dataset.p!==i});tabs.forEach(function(t){t.setAttribute('aria-selected',t.dataset.p===i)})};
    tabs.forEach(function(t){t.addEventListener('click',function(){showPanel(t.dataset.p)})});
    var dm=d.getElementById('dockMenu'),dl=dm&&dm.querySelector('.lbl'),dlText=dl&&dl.textContent;
    var setMenu=function(open){
      body.classList.toggle('menu-open',open);
      if(open)showPanel(cur);
      mm.setAttribute('aria-hidden',!open);
      if(dm){dm.setAttribute('aria-expanded',open);dl.textContent=open?dl.dataset.close:dlText}
      if(open)hdr.classList.add('scrolled');else onScroll();
    };
    if(dm)dm.addEventListener('click',function(){setMenu(!body.classList.contains('menu-open'))});
    d.querySelectorAll('.dock-cta').forEach(function(a){a.addEventListener('click',function(){setMenu(false)})});
    mm.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){setMenu(false)})});
    addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});
    addEventListener('resize',function(){if(innerWidth>1080)setMenu(false)});
  }

  /* sections bar: the section in view is marked */
  var links=[].slice.call(d.querySelectorAll('.subnav a.nl[href^="#"]'));
  if(links.length&&'IntersectionObserver' in window){
    var so=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(l){var on=l.getAttribute('href')==='#'+e.target.id;l.classList.toggle('active',on);if(on)l.setAttribute('aria-current','location');else l.removeAttribute('aria-current')})}})},{rootMargin:'-45% 0px -50% 0px'});
    links.forEach(function(l){var s=d.getElementById(l.getAttribute('href').slice(1));if(s)so.observe(s)});
  }

  /* the chosen language is remembered, so the English page does not send German browsers to /de/ again */
  d.querySelectorAll('.langsw a').forEach(function(a){a.addEventListener('click',function(){try{localStorage.setItem('amalor-lang',a.dataset.l)}catch(e){}})});
})();
