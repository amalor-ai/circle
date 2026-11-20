#!/usr/bin/env python3
"""Create the HubSpot contact properties and form fields the German forms send (src/forms_de.py).

The HubSpot Forms API rejects submissions with fields that are not in the form,
so every new field has to exist (1) as a contact property and (2) as a field in
the matching HubSpot form. This script does both and changes nothing else:
existing properties keep their options (new options are only added), existing
form fields stay as they are.

Run locally, no GitHub Actions needed:
    export HUBSPOT_TOKEN=...          # private app, scopes: crm.schemas.contacts.write, forms
    python3 infra/hubspot_forms.py            # dry run: shows what would change
    python3 infra/hubspot_forms.py --apply    # makes the changes
"""
import json, os, sys, urllib.error, urllib.request

API = 'https://api.hubapi.com'
FORMS = {'client': '0fe9bdc2-8762-487e-9594-b1ebd3a91384',
         'member': '11628041-93d6-40d9-b4af-c73b732fce86',
         'guide': 'dcfdd777-5a17-4f14-ab9a-3f82c239e5b8'}

E = 'enumeration'
# name: (type, fieldType, label, options[(value, label)])
PROPS = {
    'lgt_linkedin': ('string', 'text', 'LinkedIn-Profil oder Website', []),
    'lgt_work_status': (E, 'select', 'Wie arbeitet die Person heute', [
        ('freelancer', 'Freelancer'), ('employed', 'Angestellt'), ('transition', 'Im Umbruch'),
        ('owner', 'Inhaber einer Firma'), ('retired', 'Im Ruhestand')]),
    'lgt_commitment': (E, 'select', 'Zeitliches Commitment', [
        ('side', 'Nebenbei, 5–10 h'), ('part', 'Teilzeit, 15–20 h'), ('full', 'Vollzeit, 30–40 h')]),
    'lgt_team_role': (E, 'select', 'Rolle im Team', [
        ('process', 'Prozesskenner'), ('build', 'Umsetzer'), ('clients', 'Kunden gewinnen und begleiten'), ('open', 'Noch offen')]),
    'lgt_side_work': (E, 'select', None, [('na', 'Trifft nicht zu')]),
    'lgt_industry': (E, 'select', None, [
        ('amb_care', 'Ambulante Pflege'), ('stat_care', 'Stationäre Pflege'), ('craft', 'Handwerk, SHK'),
        ('property', 'Hausverwaltung'), ('cleaning', 'Gebäudereinigung'), ('staffing', 'Zeitarbeit'), ('none', 'Keine bestimmte')]),
    'lgt_industry_years': (E, 'select', 'Jahre in der Branche', [
        ('y0_2', 'Bis 2'), ('y2_5', '2–5'), ('y5_10', '5–10'), ('y10_plus', 'Mehr als 10')]),
    'lgt_skills': (E, 'checkbox', None, [
        ('process', 'Prozessanalyse'), ('lowcode', 'Low-Code und Automatisierung'), ('pm', 'Projektleitung'), ('qm', 'Qualitätsmanagement')]),
    'lgt_ai_level': (E, 'select', 'KI-Level (Selbsteinschätzung)', [
        ('1', 'Kaum'), ('2', 'Im Alltag'), ('3', 'Eigene Abläufe'), ('4', 'Agenten und Automationen')]),
    'lgt_adizes_self': (E, 'checkbox', 'Adizes (Selbsteinschätzung)', [
        ('P', 'P – Macher'), ('A', 'A – Ordner'), ('E', 'E – Gestalter'), ('I', 'I – Verbinder')]),
    'lgt_motive_start': (E, 'checkbox', 'Motiv bei der Anmeldung', [
        ('income', 'Einkommen'), ('experience', 'Erfahrung'), ('team', 'Ein Team'), ('meaning', 'Sinnvolle Arbeit'), ('equity', 'Anteil an einem Produkt')]),
    'lgt_referred_by': ('string', 'text', 'Empfohlen von', []),
    'lgt_decision_role': (E, 'select', 'Rolle beim Auftraggeber', [
        ('owner', 'Inhaber'), ('md', 'Geschäftsführung'), ('lead', 'Leitung eines Bereichs'), ('other', 'Andere')]),
    'lgt_company_size': (E, 'select', 'Mitarbeitende', [
        ('s1_9', '1–9'), ('s10_49', '10–49'), ('s50_249', '50–249'), ('s250_plus', '250 und mehr')]),
    'lgt_current_software': ('string', 'text', 'Software heute', []),
    'lgt_shared_interest': (E, 'select', 'Interesse an gemeinsamer Branchenlösung', [
        ('yes', 'Ja'), ('maybe', 'Vielleicht'), ('no', 'Nein, nur für uns')]),
    'lgt_ref_relation': (E, 'select', 'Beziehung des Vermittlers zum Auftraggeber', [
        ('contact', 'Bekannte, Netzwerk'), ('own_client', 'Eigener Kunde'), ('employee', 'Dort angestellt'),
        ('advisor', 'Berät bei der Auswahl'), ('other', 'Andere')]),
}

FIELDS = {
    'member': ['lgt_linkedin', 'city', 'lgt_work_status', 'lgt_commitment', 'lgt_team_role', 'lgt_side_work',
               'lgt_industry', 'lgt_industry_years', 'lgt_skills', 'lgt_ai_level', 'lgt_adizes_self', 'lgt_motive_start',
               'lgt_referred_by', 'lgt_knows_owners', 'lgt_member_problem', 'lgt_lang_primary'],
    'client': ['lgt_decision_role', 'lgt_company_size', 'lgt_industry', 'lgt_current_software', 'lgt_shared_interest',
               'lgt_client_pain', 'lgt_timeline', 'lgt_lang_primary'],
    'guide': ['lgt_ref_relation'],
}
FORM_FIELD_TYPE = {'text': 'single_line_text', 'textarea': 'multi_line_text', 'select': 'dropdown', 'checkbox': 'multiple_checkboxes'}

TOKEN = os.environ.get('HUBSPOT_TOKEN')
APPLY = '--apply' in sys.argv


def call(method, path, body=None):
    req = urllib.request.Request(API + path, method=method, data=json.dumps(body).encode() if body is not None else None,
                                 headers={'Authorization': f'Bearer {TOKEN}', 'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise SystemExit(f'{method} {path}: {e.code} {e.read().decode()[:500]}')


def write(method, path, body, what):
    print(('  APPLY ' if APPLY else '  would ') + what)
    if APPLY:
        call(method, path, body)


def opts(pairs, start=0):
    return [{'value': v, 'label': l, 'displayOrder': start + i, 'hidden': False} for i, (v, l) in enumerate(pairs)]


def ensure_properties():
    group = (call('GET', '/crm/v3/properties/contacts/lgt_role') or {}).get('groupName', 'contactinformation')
    for name, (ptype, ftype, label, options) in PROPS.items():
        cur = call('GET', f'/crm/v3/properties/contacts/{name}')
        if cur is None:
            if label is None:
                raise SystemExit(f'{name} should exist already but is missing')
            body = {'name': name, 'label': label, 'type': ptype, 'fieldType': ftype, 'groupName': group}
            if options:
                body['options'] = opts(options)
            write('POST', '/crm/v3/properties/contacts', body, f'create property {name}')
            continue
        have = {o['value'] for o in cur.get('options', [])}
        new = [(v, l) for v, l in options if v not in have]
        if new:
            body = {'options': cur['options'] + opts(new, len(cur['options']))}
            write('PATCH', f'/crm/v3/properties/contacts/{name}', body,
                  f'add options to {name}: {", ".join(v for v, _ in new)}')


def ensure_form_fields():
    for kind, guid in FORMS.items():
        form = call('GET', f'/marketing/v3/forms/{guid}')
        if form is None:
            raise SystemExit(f'form {kind} ({guid}) not found')
        groups = form.get('fieldGroups', [])
        have = {f['name'] for g in groups for f in g.get('fields', [])}
        missing = [n for n in FIELDS[kind] if n not in have]
        synced = []   # existing choice fields get the property's current options (e.g. new industries)
        for g in groups:
            for f in g.get('fields', []):
                if f['name'] in PROPS and f.get('fieldType') in ('dropdown', 'multiple_checkboxes'):
                    prop = call('GET', f'/crm/v3/properties/contacts/{f["name"]}') or {}
                    want = {o['value'] for o in prop.get('options', [])} | {v for v, _ in PROPS[f['name']][3]}
                    if want - {o['value'] for o in f.get('options', [])}:
                        f['options'] = [{'label': o['label'], 'value': o['value'], 'displayOrder': o.get('displayOrder', i)}
                                        for i, o in enumerate(prop.get('options', []))]
                        synced.append(f['name'])
        print(f'form {kind}: {len(missing)} field(s) missing, {len(synced)} with new options')
        if not missing and not synced:
            continue
        if not missing:
            write('PATCH', f'/marketing/v3/forms/{guid}', {'fieldGroups': groups}, f'update options in form {kind}: {", ".join(synced)}')
            continue
        add = []
        for n in missing:
            prop = call('GET', f'/crm/v3/properties/contacts/{n}') or {}
            ftype = prop.get('fieldType') or PROPS.get(n, ('', 'text'))[1]
            field = {'objectTypeId': '0-1', 'name': n, 'label': prop.get('label') or (PROPS.get(n, (None, None, n))[2] or n),
                     'fieldType': FORM_FIELD_TYPE.get(ftype, 'single_line_text'), 'required': False, 'hidden': False}
            if field['fieldType'] in ('dropdown', 'multiple_checkboxes'):
                field['options'] = [{'label': o['label'], 'value': o['value'], 'displayOrder': o.get('displayOrder', i)}
                                    for i, o in enumerate(prop.get('options') or opts(PROPS[n][3]))]
            add.append({'groupType': 'default_group', 'richTextType': 'text', 'fields': [field]})
        write('PATCH', f'/marketing/v3/forms/{guid}', {'fieldGroups': groups + add},
              f'add to form {kind}: {", ".join(missing)}')


if __name__ == '__main__':
    if not TOKEN:
        raise SystemExit('Set HUBSPOT_TOKEN (private app token) first.')
    print('DRY RUN – nothing is changed. Add --apply to make the changes.\n' if not APPLY else '')
    ensure_properties()
    ensure_form_fields()
