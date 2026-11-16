"""German content for the multi-page site; merged into the dicts of content_extra."""
from content_extra import NAV, TITLE, PAGE_TITLES, DESC, HOME_MORE, LADDER, TEAM, INVESTORS, BOOK

NAV['de'] = [('clients/', 'Auftraggeber'), ('members/', 'Mitglieder'), ('team/', 'So arbeitet ein Team'),
             ('guides/', 'Vermittler'), ('investors/', 'Investoren'), ('principles/', 'Prinzipien'), ('book/', 'Buch')]
TITLE['de'] = 'Team der letzten Generation'
PAGE_TITLES['de'] = {'index': 'Team der letzten Generation', 'clients': 'Auftraggeber — Team der letzten Generation',
                     'members': 'Mitglieder — Team der letzten Generation', 'team': 'So arbeitet ein Team — Team der letzten Generation',
                     'guides': 'Vermittler — Team der letzten Generation', 'principles': 'Prinzipien — Team der letzten Generation',
                     'investors': 'Investoren — Team der letzten Generation', 'book': 'Buch — Team der letzten Generation'}
DESC['de'] = {
    'clients': 'Abgestimmte Arbeit in Etappen bis zum Ergebnis: ein kleines Team von Fachleuten, Diagnose zum Festpreis, Bezahlung pro Etappe. Dubai und remote.',
    'members': 'Im Team arbeiten, nicht allein: sinnvolle Aufgaben, Einkommen nach Beitrag, ein Weg vom Mitglied zum Mentor.',
    'team': 'Der Wochenrhythmus, der sechswöchige Zyklus, die Teamvereinbarung und wie sich der Prozess selbst verbessert.',
    'guides': 'Stellen Sie uns einen Auftraggeber vor und erhalten Sie 10 % des ersten Projekts.',
    'principles': 'Was das Team zusammenhält, welche Aufgaben wir übernehmen und wie das Geld geteilt wird.',
    'investors': 'Der Weg für Investoren: zuerst Beteiligung, Geld erst nach Beweisen.',
    'book': 'Das Buch „Team der letzten Generation. Wie ein Bündel Schilfrohr“ – bald.'}

HOME_MORE['de'] = '''<section>
  <div class="head"><h2>So funktioniert es</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Aufgabe</h3><p class="when">Ein Auftraggeber bringt eine Aufgabe, oder ein Mitglied des Kreises findet sie. Wir prüfen sie mit unserem Filter.</p></div></li>
    <li><span class="num">2</span><div><h3>Team</h3><p class="when">Für die Aufgabe stellen wir ein kleines Team aus Menschen zusammen, die sich in der Praxis bewährt haben.</p></div></li>
    <li><span class="num">3</span><div><h3>Arbeit in Etappen</h3><p class="when">Jede Etappe sieht und nimmt der Auftraggeber ab. Für das Ergebnis steht das ganze Team ein.</p></div></li>
    <li><span class="num">4</span><div><h3>Wachstum</h3><p class="when">Starke Lösungen können zu einem Produkt werden – und das Team zu seinen Miteigentümern.</p></div></li>
  </ol>
  <p class="more"><a href="{L}team/">So arbeitet ein Team →</a> · <a href="{L}principles/">Prinzipien →</a></p>
</section>'''

LADDER['de'] = '''<section>
  <div class="head">
    <h2>Man kommt wegen des Geldes. Man bleibt wegen des Teams</h2>
    <p class="lead">Die Motivation wächst mit dem Menschen: vom Verdienst und der Erfahrung hin zu Anerkennung und dem Wunsch, etwas zurückzugeben.</p>
  </div>
  <ol class="ladder">
    <li><span class="num">1</span><div><h3>Mitglied</h3><p class="when">Motiv: Geld und Erfahrung</p></div></li>
    <li><span class="num">2</span><div><h3>Teammitglied</h3><p class="when">Motiv: Anteil und Anerkennung des Auftraggebers</p></div></li>
    <li><span class="num">3</span><div><h3>Kern</h3><p class="when">Motiv: Anerkennung für den Beitrag zum Ganzen</p></div></li>
    <li><span class="num">4</span><div><h3>Mentor</h3><p class="when">Motiv: zurückgeben und andere wachsen lassen</p></div></li>
  </ol>
  <p class="rule"><b>Die Basis auf jeder Stufe:</b> faire Bezahlung und ein Anteil nach Beitrag.</p>
</section>'''

TEAM['de'] = '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">So arbeitet ein Team</p>
    <h1>Ein Rhythmus, der Menschen zusammenhält</h1>
    <p class="lead">Etwa drei Stunden Meetings pro Woche – vereinbar mit einem Hauptjob. Jedes Meeting beginnt mit einem Ziel und endet mit einer Entscheidung.</p>
  </div>
</header>
<section>
  <div class="head"><h2>Die Woche</h2></div>
  <div class="week">
    <div><p class="when">Mo · 30 Minuten</p><h3>Kreis</h3><p>Das Ziel in einem Satz. Alle sprechen reihum, etwa eine Minute, ohne Diskussion. Jede Person nennt ihre wichtigste Aufgabe und wo sie Hilfe braucht.</p></div>
    <div><p class="when">Di–Do · ohne Meetings</p><h3>Arbeit und Kundentermine</h3><p>Ein kurzes Update im Chat: was ich gemacht habe, wo ich feststecke. Wer feststeckt, bekommt Hilfe – und alle sehen es.</p></div>
    <div><p class="when">Fr · 45 Minuten</p><h3>Demo und Anerkennungsrunde</h3><p>Was wir von Kunden gelernt und was wir gebaut haben. Jede Person nennt etwas Wertvolles, das jemand anderes getan hat.</p></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>Der Zyklus – 6 Wochen Arbeit und eine Pause</h2>
    <p class="lead">Am Ende jedes Zyklus entscheidet das Team: weitermachen, Kurs ändern oder auseinandergehen.</p>
  </div>
  <div class="cycle" aria-label="Sechs Wochen Arbeit, dann eine große Retrospektive und eine Pause">
    <span>Wo. 1</span><span>Wo. 2</span><span>Wo. 3</span><span>Wo. 4</span><span>Wo. 5</span><span>Wo. 6</span><span class="retro">Retro · 90 Min.</span><span class="pause">Pause 1–2 Wo.</span>
  </div>
  <div class="cols" style="margin-top:20px">
    <div><h3>Die große Retrospektive</h3>
      <ul class="ticks"><li>Was ich von jedem gelernt habe</li><li>Mein Fehler und was ich daraus mache</li><li>Wo ich genommen, wo ich gegeben habe</li><li>Eine Änderung am Prozess</li></ul></div>
    <div><h3>Einmal im Quartal – der große Kreis</h3>
      <ul class="ticks"><li>Rollen und Team Lead werden im Konsens bestätigt – nach dem, was getan wurde, nicht nach Sympathie</li><li>Anerkennung für Hilfe an andere ist der wichtigste Grund für Ehre</li><li>Ein Beitrag in den gemeinsamen Fonds, der neue Teams startet</li></ul></div>
  </div>
</section>
<section>
  <div class="head">
    <h2>Die Teamvereinbarung</h2>
    <p class="lead">Wird am ersten Tag unterschrieben und bei jeder großen Retrospektive neu gelesen.</p>
  </div>
  <ol class="contract">
    <li>Wir stehen gemeinsam für das Ergebnis ein: Steckt einer fest, ist es die Aufgabe aller.</li>
    <li>Über andere sprechen wir über das Wertvolle. Über eigene Fehler spricht jeder selbst.</li>
    <li>Im Meeting sind wir ganz da: ohne Handy und ohne parallele Arbeit.</li>
    <li>Wir entscheiden im Konsens: Eine Entscheidung gilt, wenn es keine begründeten Einwände gibt.</li>
    <li>Im Streit geben wir zuerst die Position des anderen so wieder, dass er zustimmt.</li>
    <li>Hilfe für andere ist sichtbar und zählt mehr als persönliche Erfolge.</li>
    <li>Das Signal „Mir geht es gerade schwer“ ist normal und sicher. Zwei übernehmen die Aufgaben.</li>
    <li>Rollen, auch der Team Lead, werden vom Team einmal im Quartal bestätigt.</li>
  </ol>
</section>
<section>
  <div class="head"><h2>Der Prozess verbessert sich selbst</h2></div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Team-Retro</h3><p class="when">muss eine Änderung hervorbringen</p></div></li>
    <li><span class="num">2</span><div><h3>Prüfung im Zyklus</h3><p class="when">haben sich die Gesundheitswerte des Teams verbessert?</p></div></li>
    <li><span class="num">3</span><div><h3>Kreis der Teams</h3><p class="when">monatlich: was bei anderen funktioniert hat</p></div></li>
    <li><span class="num">4</span><div><h3>Gemeinsames Playbook</h3><p class="when">eine neue Version für alle Teams</p></div></li>
  </ol>
  <div class="metrics">
    <div><b>Lerngeschwindigkeit</b><span>wie viele Hypothesen pro Woche mit Kunden geprüft wurden</span></div>
    <div><b>Verlässlichkeit</b><span>Anteil eingehaltener Zusagen</span></div>
    <div><b>Sicherheit</b><span>eine kurze Umfrage pro Zyklus</span></div>
    <div><b>Gleiche Stimme</b><span>wie gleichmäßig in Meetings gesprochen wird</span></div>
  </div>
</section>'''

INVESTORS['de'] = '''<header class="hero small">
  <div class="stack">
    <p class="eyebrow">Investoren</p>
    <h1>Zuerst Beteiligung. Geld erst nach Beweisen</h1>
    <p class="lead">Wir bitten nicht darum, in eine Idee zu investieren. Wir laden ein, früh dabei zu sein – und zu investieren, wenn ein Pilot Ergebnisse zeigt. Wir finden ein Problem, für dessen Lösung ein Auftraggeber zahlt, stellen ein Team aus bewährten Menschen zusammen und zeigen dem Investor keinen Pitch, sondern einen Team-Pass mit dem ersten Kunden.</p>
  </div>
</header>
<section>
  <div class="head"><h2>Der Weg für Investoren</h2></div>
  <ol class="ladder">
    <li><span class="num">0</span><div><h3>Mentor und Jury</h3><p class="when">jetzt, vor dem Pilot</p><p>Sie begleiten ein Team, sitzen in der Jury des Demo-Days und geben eine weiche Zusage: „Wenn X eintritt, investiere ich Y.“ Sie sehen die Teams am frühesten – ohne Geld und ohne Risiko.</p></div></li>
    <li><span class="num">1</span><div><h3>Angel-Club</h3><p class="when">nach dem Pilot</p><p>Ein kleines Ticket gemeinsam mit 5–10 Angels. Erstes Ansichts- und Co-Investmentrecht bei jedem Team.</p></div></li>
    <li><span class="num">2</span><div><h3>Fonds und Partner</h3><p class="when">im großen Maßstab</p><p>Beteiligung an einem Fonds neben Programmen aus Dubai und Impact-Investoren. Ein Portfolio von Teams mit bewiesener Zusammenarbeit und echten Kunden.</p></div></li>
  </ol>
</section>
<section>
  <div class="head"><h2>Was der Investor bekommt</h2></div>
  <ul class="prin plain">
    <li><b>Einen Strom geprüfter Teams</b><span>Teams kommen mit Pass und erstem Kunden – keine Suche nach Deals.</span></li>
    <li><b>Geringeres Risiko</b><span>Das Team hat schon zusammengearbeitet, die Nachfrage ist vom Auftraggeber bestätigt – die zwei größten Risiken sind vor dem Ticket geschlossen.</span></li>
    <li><b>Daten</b><span>Jeder Zyklus zeigt, welche Signale ein starkes Team vorhersagen.</span></li>
  </ul>
</section>
<section>
  <div class="head"><h2>Team-Pass</h2><p class="lead">Ein Beispiel dafür, was ein Investor sieht.</p></div>
  <div class="passport">
    <div><span>Auftraggeber</span><b>Absichtserklärung ✓</b></div>
    <div><span>Gemeinsame Zyklen</span><b>2 von 2 abgeschlossen</b></div>
    <div><span>Team Lead</span><b>vom Team bestätigt</b></div>
    <div><span>Kundengespräche</span><b>[Anzahl]</b></div>
    <div><span>Verlässlichkeit</span><b>Anteil eingehaltener Zusagen</b></div>
    <div><span>Beitrag</span><b>Produkt · Technik · Vertrieb</b></div>
  </div>
  <p class="more">Möchten Sie einer der ersten Mentoren werden? Schreiben Sie an <b>hello@amalor.ai</b></p>
</section>'''

BOOK['de'] = '''<section class="book">
  <img src="{R}assets/book-cover-ru.jpg" width="659" height="988" alt="Cover des Buches „Team der letzten Generation. Wie ein Bündel Schilfrohr“ (russische Ausgabe)">
  <div class="stack">
    <p class="eyebrow">Buch · bald</p>
    <h1>Team der letzten Generation</h1>
    <p class="sub">Wie ein Bündel Schilfrohr</p>
    <p class="lead">Wie man gemeinsam mehr erreicht als allein – und tut, was die Welt braucht. Ein Buch darüber, wie ein kleines Team seine Aufgaben wählt, sich selbst organisiert und wächst – vom ersten Auftrag bis zu einem Netzwerk von Teams.</p>
    <p class="when">Das Buch ist in Vorbereitung, zuerst auf Russisch. Melde dich als Mitglied an, und wir sagen Bescheid, wenn es erscheint.</p>
    <div><a class="btn" href="{L}members/#join">Anmelden</a></div>
  </div>
</section>'''

from content_extra import PRODUCT_HOME, PRODUCT_CLIENT, PRODUCT_MEMBER, PIPELINE

PRODUCT_HOME['de'] = '''<section id="product">
  <div class="head">
    <h2>Von der Aufgabe zum Produkt</h2>
    <p class="lead">Manchmal ist die Aufgabe eines Unternehmens die Aufgabe einer ganzen Branche. Dann wird die Lösung zum Produkt – und das Produkt bekommt Miteigentümer: das Team, das es gebaut hat, und den Auftraggeber, der es mitgestaltet hat.</p>
  </div>
  <ol class="flow">
    <li><b>Aufgabe</b><span>eines Auftraggebers</span></li>
    <li><b>Lösung</b><span>in Etappen, mit Abnahme</span></li>
    <li><b>Von vielen gebraucht</b><span>bei anderen Unternehmen geprüft</span></li>
    <li><b>Produkt</b><span>Lizenzen für die Branche</span></li>
  </ol>
  <div class="owners">
    <div><b>Team</b><span>Anteile nach Beitrag</span></div>
    <div><b>Partner-Auftraggeber</b><span>ein Anteil und eine kostenlose Lizenz für sich</span></div>
    <div><b>Organisator</b><span>ein Anteil für Aufbau und Start</span></div>
    <div><b>Investoren</b><span>steigen ein, wenn das Produkt Nachfrage bewiesen hat</span></div>
  </div>
  <p class="more"><a href="{L}clients/#product-client">Für Auftraggeber →</a> · <a href="{L}investors/">Für Investoren →</a></p>
</section>'''

PRODUCT_CLIENT['de'] = '''<section id="product-client">
  <div class="head">
    <h2>Ihr Fall kann zum Produkt werden</h2>
    <p class="lead">Sie lösen Ihre eigene Aufgabe – und können daran verdienen, dass andere sie auch brauchen. Zeigt sich nach der Lösung, dass andere Unternehmen dasselbe Problem haben, entscheiden Sie, wie es weitergeht.</p>
  </div>
  <div class="tbl"><table>
    <thead><tr><th></th><th>Normaler Auftrag</th><th class="us">Partner-Auftraggeber</th></tr></thead>
    <tbody>
      <tr><td>Was Sie bekommen</td><td>eine fertige Lösung für Ihr Unternehmen</td><td class="us">eine Lösung für sich und einen Anteil am Produkt für andere</td></tr>
      <tr><td>Rechte</td><td>die Lösung gehört Ihnen, Sie nutzen sie frei</td><td class="us">eine unbefristete kostenlose Lizenz für Ihr Unternehmen und ein Anteil an den Lizenzerlösen von anderen</td></tr>
      <tr><td>Was Sie einbringen</td><td>Bezahlung der Etappen</td><td class="us">Bezahlung der Etappen, Branchenwissen, Mitarbeit an der Weiterentwicklung und Empfehlungen als erster Kunde</td></tr>
      <tr><td>Risiko</td><td>—</td><td class="us">wächst das Produkt nicht, bleibt Ihnen trotzdem eine funktionierende Lösung</td></tr>
    </tbody>
  </table></div>
  <p class="when" style="margin-top:12px">Die Höhe des Anteils richtet sich nach dem Beitrag und wird vertraglich festgelegt, bevor die Arbeit am Produkt beginnt.</p>
</section>'''

PRODUCT_MEMBER['de'] = '<p class="more"><a href="{L}#product">Wie ein Projekt zu einem Produkt mit Miteigentümern wird →</a></p>'

PIPELINE['de'] = '''<section>
  <div class="head">
    <h2>Zuerst Nachfrage. Dann Menschen. Geld zuletzt</h2>
    <p class="lead">Der erste Pilot liegt noch vor uns. Jetzt laden wir Mentoren ein, die die Teams von Anfang an sehen wollen.</p>
  </div>
  <ol class="steps">
    <li><span class="num">1</span><div><h3>Nachfrage finden</h3><p class="when">Aufgaben von Auftraggebern und Mitgliedern, Ausschreibungen, Kundenbeschwerden, neue Regeln</p></div></li>
    <li><span class="num">2</span><div><h3>Nachfrage prüfen</h3><p class="when">10–20 Gespräche und ein Auftraggeber, der für einen Pilot zahlt</p></div></li>
    <li><span class="num">3</span><div><h3>Probearbeit</h3><p class="when">1–2 Wochen in gemischten Paaren an einer echten Aufgabe</p></div></li>
    <li><span class="num">4</span><div><h3>Team bilden</h3><p class="when">3–5 Personen, Anteile nach Beitrag, Teamvereinbarung, Team Lead im Konsens</p></div></li>
    <li><span class="num">5</span><div><h3>Lösung mit dem Auftraggeber</h3><p class="when">erste Nutzer und erstes Geld – vor jeder Finanzierungsrunde</p></div></li>
    <li><span class="num">6</span><div><h3>Team-Pass</h3><p class="when">Geschichte der Zusammenarbeit, Rollen, Kundengespräche, Kennzahlen</p></div></li>
    <li><span class="num">7</span><div><h3>Demo für Investoren</h3><p class="when">ein Team, das bewiesen hat, dass es funktioniert, mit einem Partner-Auftraggeber an der Seite</p></div></li>
  </ol>
  <p class="rule"><b>Kein Auftraggeber – kein Team.</b> Passt es menschlich nicht, stellen wir aus demselben Kreis neu zusammen.</p>
</section>'''
