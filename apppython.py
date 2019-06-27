from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient


SUBSCRIPTION_ID = '580d6029-ce58-46e6-82de-808c9cb03fef'
GROUP_NAME = 'myResourceGroup'
LOCATION = 'westus'

def create_resource_group(resource_group_client):
    resource_group_params = { 'location':LOCATION }
    resource_group_result = resource_group_client.resource_groups.create_or_update(
        GROUP_NAME, 
        resource_group_params
    )

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id = '61dae3ea-c39e-4214-b9f4-78e8d61533f1',
        secret = 'qher_xSZJ3.+[pczGSlVzJ6CmscG1kd1',
        tenant = 'f8b7098a-e235-4562-aabf-c5a6db419b02'
    )

    return credentials

if __name__ == "__main__":
    credentials = get_credentials()
    resource_group_client = ResourceManagementClient(
    credentials, 
    SUBSCRIPTION_ID
    )
    create_resource_group(resource_group_client)
    input('Resource group created. Press enter to continue...')
