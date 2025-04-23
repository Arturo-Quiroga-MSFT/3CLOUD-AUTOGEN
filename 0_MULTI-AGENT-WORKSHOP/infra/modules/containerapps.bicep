
@description('Tags to apply to resources')
param tags object

@description('Name of the Container Apps environment')
param envName string

@description('Name of the Container Apps managed pool')
param poolName string

param location string = 'swedencentral'

@description('My principal name')
param myPrincipalId string
// Create a Log Analytics workspace for the Container Apps environment
resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: '${envName}-logs'
  location: 'swedencentral'
  tags: tags
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
    features: {
      enableLogAccessUsingOnlyResourcePermissions: true
    }
  }
}

// Create a Container Apps environment
resource containerAppsEnv 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: envName
  location: location
  tags: tags
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalyticsWorkspace.properties.customerId
        sharedKey: logAnalyticsWorkspace.listKeys().primarySharedKey
      }
    }
  }
}

// Create a Container Apps managed pool
resource containerAppsManagedPool 'Microsoft.App/sessionPools@2024-02-02-preview' = {
  name: poolName
  location: location
  tags: tags
  properties: {
    environmentId: containerAppsEnv.id
    poolManagementType: 'Dynamic'
    containerType: 'PythonLTS'
    scaleConfiguration: {
      maxConcurrentSessions: 100
    }
    dynamicPoolConfiguration: {
      executionType: 'Timed'
      cooldownPeriodInSeconds: 300
    }
    sessionNetworkConfiguration: {
      status: 'EgressDisabled'
    }
  }
}


// Role definition ID for Azure ContainerApps Session Executor
var containerAppSessionExecutorRoleId = '0fb8eba5-a2bb-4abe-b1c1-49dfad359bb0' // Using Session User role ID

// Create direct role assignment (no nested module)
resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(containerAppsManagedPool.id, myPrincipalId, containerAppSessionExecutorRoleId)
  scope: containerAppsManagedPool
  properties: {
    roleDefinitionId: resourceId('Microsoft.Authorization/roleDefinitions', containerAppSessionExecutorRoleId)
    principalId: myPrincipalId
    principalType: 'User'  // Change to 'ServicePrincipal' if needed
  }
}

// Outputs
output environmentId string = containerAppsEnv.id
output managedPoolId string = containerAppsManagedPool.id
output managementEndpoint string = containerAppsManagedPool.properties.poolManagementEndpoint
