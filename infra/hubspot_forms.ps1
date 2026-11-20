<#
.SYNOPSIS
  Creates the HubSpot contact properties and form fields the German forms send (src/forms_de.py).
  Same logic as infra/hubspot_forms.py, for Windows without Python. Windows PowerShell 5.1 or PowerShell 7.
.EXAMPLE
  $env:HUBSPOT_TOKEN = '...'                 # private app, scopes: crm.schemas.contacts.write, forms
  .\infra\hubspot_forms.ps1                  # dry run: shows what would change
  .\infra\hubspot_forms.ps1 -Apply           # makes the changes
#>
param([switch]$Apply)
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
if (-not $env:HUBSPOT_TOKEN) { throw 'Set $env:HUBSPOT_TOKEN (private app token) first.' }

$Api = 'https://api.hubapi.com'
$Forms = [ordered]@{ client = '0fe9bdc2-8762-487e-9594-b1ebd3a91384'; member = '11628041-93d6-40d9-b4af-c73b732fce86'; guide = 'dcfdd777-5a17-4f14-ab9a-3f82c239e5b8' }

function O([string[]]$pairs) { # 'value|label' -> list
  $i = 0; foreach ($p in $pairs) { $v, $l = $p -split '\|', 2; [pscustomobject]@{ value = $v; label = $l; displayOrder = $i; hidden = $false }; $i++ }
}
# name = type, fieldType, label ($null = must exist already), options
$Props = [ordered]@{
  lgt_linkedin        = @('string', 'text', 'LinkedIn-Profil oder Website', @())
  lgt_work_status     = @('enumeration', 'select', 'Wie arbeitet die Person heute', @('freelancer|Freelancer', 'employed|Angestellt', 'transition|Im Umbruch', 'owner|Inhaber einer Firma', 'retired|Im Ruhestand'))
  lgt_commitment      = @('enumeration', 'select', 'Zeitliches Commitment', @('side|Nebenbei, 5–10 h', 'part|Teilzeit, 15–20 h', 'full|Vollzeit, 30–40 h'))
  lgt_team_role       = @('enumeration', 'select', 'Rolle im Team', @('process|Prozesskenner', 'build|Umsetzer', 'clients|Kunden gewinnen und begleiten', 'open|Noch offen'))
  lgt_side_work       = @('enumeration', 'select', $null, @('na|Trifft nicht zu'))
  lgt_industry        = @('enumeration', 'select', $null, @('amb_care|Ambulante Pflege', 'stat_care|Stationäre Pflege', 'craft|Handwerk, SHK', 'property|Hausverwaltung', 'cleaning|Gebäudereinigung', 'staffing|Zeitarbeit', 'none|Keine bestimmte'))
  lgt_industry_years  = @('enumeration', 'select', 'Jahre in der Branche', @('y0_2|Bis 2', 'y2_5|2–5', 'y5_10|5–10', 'y10_plus|Mehr als 10'))
  lgt_skills          = @('enumeration', 'checkbox', $null, @('process|Prozessanalyse', 'lowcode|Low-Code und Automatisierung', 'pm|Projektleitung', 'qm|Qualitätsmanagement'))
  lgt_ai_level        = @('enumeration', 'select', 'KI-Level (Selbsteinschätzung)', @('1|Kaum', '2|Im Alltag', '3|Eigene Abläufe', '4|Agenten und Automationen'))
  lgt_adizes_self     = @('enumeration', 'checkbox', 'Adizes (Selbsteinschätzung)', @('P|P – Macher', 'A|A – Ordner', 'E|E – Gestalter', 'I|I – Verbinder'))
  lgt_motive_start    = @('enumeration', 'checkbox', 'Motiv bei der Anmeldung', @('income|Einkommen', 'experience|Erfahrung', 'team|Ein Team', 'meaning|Sinnvolle Arbeit', 'equity|Anteil an einem Produkt'))
  lgt_referred_by     = @('string', 'text', 'Empfohlen von', @())
  lgt_decision_role   = @('enumeration', 'select', 'Rolle beim Auftraggeber', @('owner|Inhaber', 'md|Geschäftsführung', 'lead|Leitung eines Bereichs', 'other|Andere'))
  lgt_company_size    = @('enumeration', 'select', 'Mitarbeitende', @('s1_9|1–9', 's10_49|10–49', 's50_249|50–249', 's250_plus|250 und mehr'))
  lgt_current_software= @('string', 'text', 'Software heute', @())
  lgt_shared_interest = @('enumeration', 'select', 'Interesse an gemeinsamer Branchenlösung', @('yes|Ja', 'maybe|Vielleicht', 'no|Nein, nur für uns'))
  lgt_ref_relation    = @('enumeration', 'select', 'Beziehung des Vermittlers zum Auftraggeber', @('contact|Bekannte, Netzwerk', 'own_client|Eigener Kunde', 'employee|Dort angestellt', 'advisor|Berät bei der Auswahl', 'other|Andere'))
}
$Fields = @{
  member = @('lgt_linkedin', 'city', 'lgt_work_status', 'lgt_commitment', 'lgt_team_role', 'lgt_side_work', 'lgt_industry', 'lgt_industry_years', 'lgt_skills', 'lgt_ai_level', 'lgt_adizes_self', 'lgt_motive_start', 'lgt_referred_by', 'lgt_knows_owners', 'lgt_member_problem', 'lgt_lang_primary')
  client = @('lgt_decision_role', 'lgt_company_size', 'lgt_industry', 'lgt_current_software', 'lgt_shared_interest', 'lgt_client_pain', 'lgt_timeline', 'lgt_lang_primary')
  guide  = @('lgt_ref_relation')
}
$FormType = @{ text = 'single_line_text'; textarea = 'multi_line_text'; select = 'dropdown'; checkbox = 'multiple_checkboxes'; radio = 'dropdown'; booleancheckbox = 'single_checkbox' }

function Call($method, $path, $body) {
  $p = @{ Method = $method; Uri = "$Api$path"; Headers = @{ Authorization = "Bearer $env:HUBSPOT_TOKEN" }; ContentType = 'application/json; charset=utf-8' }
  if ($null -ne $body) { $p.Body = [Text.Encoding]::UTF8.GetBytes(($body | ConvertTo-Json -Depth 30 -Compress)) }
  try { Invoke-RestMethod @p }
  catch {
    $code = $_.Exception.Response.StatusCode.value__
    if ($code -eq 404) { return $null }
    throw "$method $path : $code $($_.ErrorDetails.Message)"
  }
}
function Write-Change($method, $path, $body, $what) {
  if ($Apply) { Write-Host "  APPLY $what" -ForegroundColor Yellow; Call $method $path $body | Out-Null }
  else { Write-Host "  would $what" }
}

if (-not $Apply) { Write-Host "DRY RUN - nothing is changed. Add -Apply to make the changes.`n" -ForegroundColor Cyan }

# 1. properties
$role = Call GET '/crm/v3/properties/contacts/lgt_role'
$group = if ($role) { $role.groupName } else { 'contactinformation' }
foreach ($name in $Props.Keys) {
  $type, $ftype, $label, $pairs = $Props[$name]
  $cur = Call GET "/crm/v3/properties/contacts/$name"
  if (-not $cur) {
    if (-not $label) { throw "$name should exist already but is missing" }
    $body = @{ name = $name; label = $label; type = $type; fieldType = $ftype; groupName = $group }
    if ($pairs.Count) { $body.options = @(O $pairs) }
    Write-Change POST '/crm/v3/properties/contacts' $body "create property $name"
    continue
  }
  $have = @($cur.options | ForEach-Object { $_.value })
  $new = @($pairs | Where-Object { ($_ -split '\|', 2)[0] -notin $have })
  if ($new.Count) {
    $start = @($cur.options).Count
    $add = @(O $new | ForEach-Object { $_.displayOrder += $start; $_ })
    Write-Change PATCH "/crm/v3/properties/contacts/$name" @{ options = @($cur.options) + $add } "add options to ${name}: $(($new | ForEach-Object { ($_ -split '\|')[0] }) -join ', ')"
  }
}

# 2. form fields
function FieldOptions($name) {
  $prop = Call GET "/crm/v3/properties/contacts/$name"
  $src = if ($prop -and $prop.options) { $prop.options } elseif ($Props.Contains($name)) { @(O $Props[$name][3]) } else { @() }
  $i = 0; @($src | ForEach-Object { [pscustomobject]@{ label = $_.label; value = $_.value; displayOrder = $i }; $i++ })
}
foreach ($kind in $Forms.Keys) {
  $guid = $Forms[$kind]
  $form = Call GET "/marketing/v3/forms/$guid"
  if (-not $form) { throw "form $kind ($guid) not found" }
  $groups = @($form.fieldGroups)
  $have = @($groups | ForEach-Object { $_.fields } | ForEach-Object { $_.name })
  $missing = @($Fields[$kind] | Where-Object { $_ -notin $have })
  $synced = @()
  foreach ($g in $groups) { foreach ($f in $g.fields) {
    if ($Props.Contains($f.name) -and $f.fieldType -in 'dropdown', 'multiple_checkboxes') {
      $want = @(FieldOptions $f.name | ForEach-Object { $_.value }) + @($Props[$f.name][3] | ForEach-Object { ($_ -split '\|')[0] })
      $got = @($f.options | ForEach-Object { $_.value })
      if (@($want | Where-Object { $_ -notin $got }).Count) { $f.options = @(FieldOptions $f.name); $synced += $f.name }
    } } }
  Write-Host "form ${kind}: $($missing.Count) field(s) missing, $($synced.Count) with new options"
  if (-not $missing.Count -and -not $synced.Count) { continue }
  $add = foreach ($n in $missing) {
    $prop = Call GET "/crm/v3/properties/contacts/$n"
    $ft = if ($prop) { $prop.fieldType } elseif ($Props.Contains($n)) { $Props[$n][1] } else { 'text' }
    $lbl = if ($prop) { $prop.label } elseif ($Props.Contains($n) -and $Props[$n][2]) { $Props[$n][2] } else { $n }
    $field = [ordered]@{ objectTypeId = '0-1'; name = $n; label = $lbl; fieldType = $(if ($FormType[$ft]) { $FormType[$ft] } else { 'single_line_text' }); required = $false; hidden = $false }
    if ($field.fieldType -in 'dropdown', 'multiple_checkboxes') { $field.options = @(FieldOptions $n) }
    @{ groupType = 'default_group'; richTextType = 'text'; fields = @($field) }
  }
  $what = @(); if ($missing.Count) { $what += "add $($missing -join ', ')" }; if ($synced.Count) { $what += "new options in $($synced -join ', ')" }
  Write-Change PATCH "/marketing/v3/forms/$guid" @{ fieldGroups = @($groups) + @($add) } "form ${kind}: $($what -join '; ')"
}
Write-Host "`nDone."
