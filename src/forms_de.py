"""German forms and member-page wording (2026-11-20), applied after polish_de.

Forms follow the doc "Talentkreis: Gewinnung und Auswahl von Teammitgliedern":
the member form becomes the form for specialists ("Für Fachleute"), the client
form asks what qualifies a request in the German Mittelstand, the referrer form
asks how the referrer relates to the client (§ 299 StGB).

Every new field name must exist as a contact property and as a field in the
matching HubSpot form; infra/hubspot_forms.py creates both.
Every replacement must still match; otherwise the build stops.
"""
import re

PRIVACY = '<a href="https://www.amalor.ai/datenschutz.html">Datenschutz</a>'


def _sel(id_, name, label, options, required=False, hint=''):
    req = ' required' if required else ''
    h = f' <span class="hint">{hint}</span>' if hint else ''
    opts = '<option value="">Bitte wählen</option>' + ''.join(f'<option value="{v}">{t}</option>' for v, t in options)
    return f'<div><label for="{id_}">{label}{h}</label>\n          <select id="{id_}" name="{name}"{req}>{opts}</select></div>'


def _chips(prefix, name, label, options, hint='mehrere möglich'):
    chips = ''.join(f'<label class="chip"><input type="checkbox" id="{prefix}{i}" value="{v}"><span>{t}</span></label>'
                    for i, (v, t) in enumerate(options, 1))
    return (f'<fieldset>\n        <span class="lg">{label} <span class="hint">{hint}</span></span>\n'
            f'        <div class="chips" data-multi="{name}">{chips}</div>\n      </fieldset>')


INDUSTRIES = [('amb_care', 'Ambulante Pflege'), ('stat_care', 'Stationäre Pflege'), ('health', 'Gesundheit, Praxen, Therapie'),
              ('craft', 'Handwerk, SHK'), ('property', 'Hausverwaltung'), ('cleaning', 'Gebäudereinigung'),
              ('staffing', 'Zeitarbeit'), ('education', 'Bildung'), ('logistics', 'Logistik'), ('other', 'Sonstiges')]

MEMBER_FORM = f'''<form data-form="member" novalidate>
      <input type="hidden" name="lgt_role" value="member">
      <input type="hidden" name="lgt_lang_primary" value="de">
      <div class="row">
        <div><label for="m-name">Name</label><input id="m-name" name="firstname" type="text" autocomplete="name" required></div>
        <div><label for="m-email">E-Mail</label><input id="m-email" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div class="row">
        <div><label for="m-link">LinkedIn-Profil oder Website</label><input id="m-link" name="lgt_linkedin" type="text" inputmode="url" autocomplete="url" placeholder="linkedin.com/in/…" required></div>
        <div><label for="m-city">Stadt <span class="hint">optional</span></label><input id="m-city" name="city" type="text" autocomplete="address-level2" placeholder="Leipzig"></div>
      </div>
      <div class="row">
        {_sel('m-status', 'lgt_work_status', 'Wie arbeitest du heute?', [('freelancer', 'Freelancer'), ('employed', 'Angestellt'), ('transition', 'Im Umbruch: Elternzeit, Kündigungsfrist, Neuorientierung'), ('owner', 'Inhaber einer Firma'), ('retired', 'Im Ruhestand')], True)}
        {_sel('m-time', 'lgt_commitment', 'Wie viel Zeit kannst du einbringen?', [('side', 'Nebenbei, 5–10 h pro Woche'), ('part', 'Teilzeit, 15–20 h pro Woche'), ('full', 'Vollzeit, 30–40 h pro Woche')], True)}
      </div>
      <div class="row">
        {_sel('m-role', 'lgt_team_role', 'Welche Rolle passt zu dir?', [('process', 'Abläufe einer Branche verstehen und verbessern'), ('build', 'Software bauen'), ('clients', 'Kunden gewinnen und begleiten'), ('product', 'Produkt verantworten'), ('rhythm', 'Team und Rhythmus halten'), ('open', 'Noch offen')], True)}
        {_sel('m-side', 'lgt_side_work', 'Falls angestellt: Darfst du nebenbei arbeiten?', [('yes', 'Ja, angezeigt oder erlaubt'), ('unsure', 'Muss ich klären'), ('no', 'Nein'), ('na', 'Trifft nicht zu')])}
      </div>
      <div class="row">
        {_sel('m-ind', 'lgt_industry', 'In welcher Branche kennst du dich von innen aus?', INDUSTRIES + [('none', 'Keine bestimmte')], True)}
        {_sel('m-years', 'lgt_industry_years', 'Wie lange?', [('y0_2', 'Bis 2 Jahre'), ('y2_5', '2–5 Jahre'), ('y5_10', '5–10 Jahre'), ('y10_plus', 'Mehr als 10 Jahre')])}
      </div>
      {_chips('m-sk', 'lgt_skills', 'Was du kannst', [('process', 'Prozessanalyse'), ('dev', 'Entwicklung'), ('lowcode', 'Low-Code und Automatisierung'), ('data_ai', 'Daten und KI'), ('design', 'Design'), ('sales', 'Vertrieb'), ('pm', 'Projektleitung'), ('qm', 'Qualitätsmanagement'), ('legal', 'Recht'), ('finance', 'Finanzen')])}
      {_sel('m-ai', 'lgt_ai_level', 'Wie arbeitest du mit KI?', [('1', 'Kaum'), ('2', 'Im Alltag, im Chat'), ('3', 'Mit eigenen Abläufen und Vorlagen'), ('4', 'Ich baue Agenten und Automationen')])}
      {_chips('m-ad', 'lgt_adizes_self', 'Was liegt dir am meisten?', [('P', 'Liefern und fertig machen'), ('A', 'Ordnung und Genauigkeit'), ('E', 'Neue Ideen und Richtung'), ('I', 'Menschen verbinden')], 'höchstens zwei')}
      {_chips('m-mo', 'lgt_motive_start', 'Was suchst du vor allem?', [('income', 'Einkommen'), ('experience', 'Erfahrung'), ('team', 'Ein Team'), ('meaning', 'Sinnvolle Arbeit'), ('equity', 'Anteil an einem Produkt')])}
      <div class="row">
        <div><label for="m-ref">Wer hat dich empfohlen? <span class="hint">optional</span></label><input id="m-ref" name="lgt_referred_by" type="text"></div>
        <div><label for="m-know">Welche Unternehmer kennst du? <span class="hint">optional, ohne Namen</span></label><input id="m-know" name="lgt_knows_owners" type="text" placeholder="2 Pflegedienste, ein Handwerksbetrieb"></div>
      </div>
      <div><label for="m-problem">Welches Problem siehst du in deiner Branche? <span class="hint">optional</span></label>
        <textarea id="m-problem" name="lgt_member_problem" placeholder="Zum Beispiel: Die Tourenplanung kostet jede Woche Stunden, weil …"></textarea></div>
      <label class="consent"><input type="checkbox" id="m-consent" data-consent><span>Ich bin einverstanden, dass meine Angaben für die Auswahl und Einladungen zu den Runden gespeichert werden. Auf Wunsch sofort gelöscht. {PRIVACY}</span></label>
      <p class="err" role="alert"></p>
      <div><button class="btn" type="submit">Im Team mitarbeiten</button></div>
    </form>'''

CLIENT_FORM = f'''<form data-form="client" novalidate>
      <input type="hidden" name="lgt_role" value="client">
      <input type="hidden" name="lgt_lang_primary" value="de">
      <div class="row">
        <div><label for="c-name">Name</label><input id="c-name" name="firstname" type="text" autocomplete="name" required></div>
        <div><label for="c-company">Unternehmen</label><input id="c-company" name="company" type="text" autocomplete="organization" required></div>
      </div>
      <div class="row">
        <div><label for="c-email">E-Mail</label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
        <div><label for="c-phone">Telefon <span class="hint">optional</span></label><input id="c-phone" name="phone" type="tel" autocomplete="tel"></div>
      </div>
      <div class="row">
        {_sel('c-role', 'lgt_decision_role', 'Ihre Rolle', [('owner', 'Inhaber'), ('md', 'Geschäftsführung'), ('lead', 'Leitung eines Bereichs'), ('other', 'Andere')], True)}
        {_sel('c-size', 'lgt_company_size', 'Mitarbeitende', [('s1_9', '1–9'), ('s10_49', '10–49'), ('s50_249', '50–249'), ('s250_plus', '250 und mehr')], True)}
      </div>
      <div class="row">
        {_sel('c-ind', 'lgt_industry', 'Branche', INDUSTRIES, True)}
        <div><label for="c-sw">Welche Software nutzen Sie heute? <span class="hint">optional</span></label><input id="c-sw" name="lgt_current_software" type="text" placeholder="Branchenprogramm, Excel, Papier …"></div>
      </div>
      <div><label for="c-pain">Was möchten Sie lösen?</label>
        <textarea id="c-pain" name="lgt_client_pain" placeholder="Was passiert gerade und was kostet es Sie an Zeit oder Geld" required></textarea></div>
      <div class="row">
        {_sel('c-when', 'lgt_timeline', 'Wann brauchen Sie das Ergebnis?', [('month', 'Innerhalb eines Monats'), ('quarter', '1–3 Monate'), ('later', 'Später'), ('exploring', 'Ich informiere mich erst')])}
        {_sel('c-shared', 'lgt_shared_interest', 'Gemeinsame Lösung mit anderen Betrieben denkbar?', [('yes', 'Ja'), ('maybe', 'Vielleicht, mehr erfahren'), ('no', 'Nein, nur für uns')])}
      </div>
      <label class="consent"><input type="checkbox" id="c-consent" data-consent><span>Ich bin einverstanden, dass meine Anfragedaten gespeichert werden, damit Sie mich kontaktieren können. Auf Wunsch sofort gelöscht. {PRIVACY}</span></label>
      <p class="err" role="alert"></p>
      <div><button class="btn" type="submit">Anfrage senden</button></div>
    </form>'''

GUIDE_FORM = f'''<form data-form="guide" novalidate>
      <input type="hidden" name="lgt_role" value="guide">
      <div class="row">
        <div><label for="g-name">Ihr Name</label><input id="g-name" name="firstname" type="text" autocomplete="name" required></div>
        <div><label for="g-email">Ihre E-Mail</label><input id="g-email" name="email" type="email" autocomplete="email" required></div>
      </div>
      <div class="row">
        <div><label for="g-client">Unternehmen des Auftraggebers</label><input id="g-client" name="lgt_ref_company" type="text" required></div>
        <div><label for="g-contact">Wie wir ihn erreichen</label><input id="g-contact" name="lgt_ref_contact" type="text" placeholder="Name, Rolle, Telefon oder E-Mail" required></div>
      </div>
      {_sel('g-rel', 'lgt_ref_relation', 'Ihre Beziehung zum Auftraggeber', [('contact', 'Bekannte, Kollegen, Netzwerk'), ('own_client', 'Er ist mein Kunde, ich arbeite nicht für ihn'), ('employee', 'Ich bin dort angestellt'), ('advisor', 'Ich berate ihn bei der Auswahl von Dienstleistern'), ('other', 'Andere')], True, 'Angestellte und Berater, die für ihn auswählen, erhalten keine Prämie')}
      <div><label for="g-pain">Wobei braucht er Unterstützung?</label>
        <textarea id="g-pain" name="lgt_ref_pain" placeholder="Was Sie gesehen haben oder was er erzählt hat" required></textarea></div>
      <label class="consent"><input type="checkbox" id="g-ok" data-bool="lgt_ref_consent" data-consent data-msg="Bitte bestätigen Sie, dass der Auftraggeber einverstanden ist – sonst dürfen wir ihn nicht kontaktieren."><span>Der Auftraggeber ist einverstanden, dass ich seinen Kontakt weitergebe.</span></label>
      <label class="consent"><input type="checkbox" id="g-consent" data-consent><span>Ich bin einverstanden, dass meine Daten zur Berechnung der Prämie gespeichert werden. Auf Wunsch sofort gelöscht. {PRIVACY}</span></label>
      <p class="err" role="alert"></p>
      <div><button class="btn" type="submit">Auftraggeber vorstellen</button></div>
    </form>'''

FORMS = {'members': ('member', MEMBER_FORM), 'clients': ('client', CLIENT_FORM), 'guides': ('guide', GUIDE_FORM)}

# (old, new, pages) – pages None = every German page
PAIRS = [
    ('>Mitglieder<', '>Für Fachleute<', None),
    ('Mitglieder — Team der letzten Generation', 'Für Fachleute — Team der letzten Generation', ['members']),
    ('Für Auftraggeber, Mitglieder und Vermittler', 'Für Auftraggeber, Fachleute und Vermittler', ['index']),
    ('Für Mitglieder →', 'Für Fachleute →', ['index']),
    ('Für Mitglieder', 'Für Fachleute', ['members']),
    ('ein Weg vom Mitglied zum Mentor', 'ein Weg vom Kreis bis zum Mentor', ['members']),
    ('Melde dich als Mitglied an', 'Trag dich als Fachkraft ein', ['book']),
    ('Mitglied → Teammitglied → Kern → Mentor', 'Kreis → Team → Brückenbauer → Mentor', ['members']),
    ('<li><b>Weg des Wachstums:</b>', '<li><b>Feste Fünf.</b> Du arbeitest mit etwa fünf Menschen fest zusammen. Die Rollen wechseln je nach Etappe, und das Netzwerk hilft, wenn ihr hängt.</li>\n      <li><b>Weg des Wachstums:</b>', ['members']),
    ('<h3>Mitglied</h3>', '<h3>Im Kreis</h3>', ['members']),
    ('<h3>Anmeldung als Mitglied</h3>', '<h3>Im Team mitarbeiten</h3>', ['members']),
    ('<h3>Prüfwoche</h3>', '<h3>Gespräch und Probeaufgabe</h3>', ['members']),
    ('zu zweit, etwa 5 Gespräche mit Kunden', '30 Minuten über Werte, dann eine bezahlte Probeaufgabe', ['members']),
    ('<h3>Team und Projekt</h3>', '<h3>Probeetappe und Team</h3>', ['members']),
    ('ihr wählt eine Teamleitung – jemanden, der den Rhythmus hält und dem Team dient',
     '2–3 bezahlte Wochen im gemischten Team; danach bestätigt das Team, wer fest dazugehört', ['members']),
]


def apply(html, page):
    for old, new, pages in PAIRS:
        if pages is None or page in pages:
            if old not in html:
                raise SystemExit(f'forms_de: "{old}" not found on {page} (text changed?)')
            html = html.replace(old, new)
    if page in FORMS:
        kind, form = FORMS[page]
        html, n = re.subn(rf'<form data-form="{kind}" novalidate>.*?</form>', lambda m: form, html, count=1, flags=re.S)
        if n != 1:
            raise SystemExit(f'forms_de: form {kind} not found on {page}')
        if page == 'clients':   # the AI-assistant hint no longer needs to mention only three fields
            html = html.replace('Name, E-Mail und eine Beschreibung der Aufgabe genügen.',
                                'Name, Unternehmen, E-Mail, Rolle, Größe, Branche und eine Beschreibung der Aufgabe.')
    return html
