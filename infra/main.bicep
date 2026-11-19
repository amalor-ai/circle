// Team der letzten Generation: Azure Static Web App for team.amalor.ai
// Deploy:  az deployment group create -g rg-amalor-web -f infra/main.bicep [-p enableCustomDomain=true]
// Same resource group as the amalor.ai website (rg-amalor-web), separate app.
targetScope = 'resourceGroup'

@description('Name of the Static Web App')
param name string = 'swa-amalor-team'

@description('Region of the resource (content is served globally)')
@allowed([
  'westeurope'
  'centralus'
  'eastus2'
  'westus2'
  'eastasia'
])
param location string = 'westeurope'

@description('Free is enough for a static site')
@allowed([
  'Free'
  'Standard'
])
param sku string = 'Free'

@description('Bind team.amalor.ai. Enable only after the CNAME "team" in Azure DNS points to this app.')
param enableCustomDomain bool = false

param hostname string = 'team.amalor.ai'

param tags object = {
  project: 'amalor'
  workload: 'team-website'
}

resource swa 'Microsoft.Web/staticSites@2023-12-01' = {
  name: name
  location: location
  tags: tags
  sku: {
    name: sku
    tier: sku
  }
  properties: {
    // Deployed from GitHub Actions with the deployment token; no repo binding here.
    allowConfigFileUpdates: true
    stagingEnvironmentPolicy: 'Disabled'
  }
}

resource customDomain 'Microsoft.Web/staticSites/customDomains@2023-12-01' = if (enableCustomDomain) {
  parent: swa
  name: hostname
  properties: {
    validationMethod: 'cname-delegation'
  }
}

output defaultHostname string = swa.properties.defaultHostname
