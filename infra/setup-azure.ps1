<#
  team.amalor.ai: one-time setup on Azure. Run in PowerShell 7 with Azure CLI and GitHub CLI (gh) installed.
  Steps 1-3 now; step 4 after the CNAME has propagated (usually a few minutes).

    ./infra/setup-azure.ps1            # steps 1-3
    ./infra/setup-azure.ps1 -BindDomain  # step 4
#>
param([switch]$BindDomain)
$ErrorActionPreference = 'Stop'
$tenant = 'aed4db3d-f0be-4b3e-ab35-80a9fa86b0bb'
$rg     = 'rg-amalor-web'
$app    = 'swa-amalor-team'
$repo   = 'amalor-ai/team'

$cur = az account show --query tenantId -o tsv 2>$null
if ($cur -ne $tenant) { az login --tenant $tenant | Out-Null }
az account set --subscription 'Azure-Abonnement 1'

if (-not $BindDomain) {
  # 1. Static Web App (Free)
  $out = az deployment group create -g $rg -f "$PSScriptRoot/main.bicep" --query properties.outputs.defaultHostname.value -o tsv
  Write-Host "Static Web App: https://$out"

  # 2. Deployment token -> GitHub secret (never printed)
  az staticwebapp secrets list -n $app -g $rg --query properties.apiKey -o tsv | gh secret set AZURE_STATIC_WEB_APPS_API_TOKEN -R $repo
  gh workflow run deploy.yml -R $repo
  Write-Host 'Deploy started. Check: gh run list -R amalor-ai/team'

  # 3. DNS: CNAME team -> Static Web App (DNS as code lives in amalor-website/infra/dns.bicep, enableTeam = true)
  Write-Host 'Now in the amalor-website repo:'
  Write-Host '  az deployment group create -g rg-amalor-web -f infra/dns.bicep -p infra/dns.bicepparam'
  Write-Host 'Then, after a few minutes:  ./infra/setup-azure.ps1 -BindDomain'
}
else {
  # 4. Bind team.amalor.ai (Azure checks the CNAME and issues the certificate itself)
  az deployment group create -g $rg -f "$PSScriptRoot/main.bicep" -p enableCustomDomain=true --query properties.provisioningState -o tsv
  Write-Host 'Done. Certificate can take up to 15 minutes: https://team.amalor.ai'
}
