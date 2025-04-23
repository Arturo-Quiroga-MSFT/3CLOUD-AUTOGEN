@description('Tags to apply to resources')
param tags object

@description('Name of the Azure OpenAI service')
param openAiName string

@description('Location for the OpenAI service')
@allowed([
  'eastus'
  'southcentralus'
  'westeurope'
  'swedencentral'
  'westus'
])
param location string = 'swedencentral'

resource openAi 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: openAiName
  location: location
  tags: tags
  kind: 'OpenAI'
  sku: {
    name: 'S0'
  }
  properties: {
    customSubDomainName: openAiName
    publicNetworkAccess: 'Enabled'
  }
}

// Define the model deployment with hardcoded GPT-4o configuration
resource gpt4oDeployment 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
  parent: openAi
  name: 'gpt-4o'
  sku: {
    name: 'Standard'
    capacity: 150
  }
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-4o'
      version: '2024-11-20'
    }
    raiPolicyName: 'Microsoft.Default'
  }
}
// Outputs
output openAIId string = openAi.id
output openAIEndpoint string = openAi.properties.endpoint
