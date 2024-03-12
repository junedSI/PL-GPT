import configparser

class Reader:
    def __init__(self, config_file='config.cfg'):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.openai_config = self._get_openai_config()
        self.adf_config = self._get_azure_data_factory_config()

    def _get_openai_config(self):
        return {
            'azure_endpoint': self.config.get('OpenAI', 'azure_endpoint'),
            'openai_api_version': self.config.get('OpenAI', 'openai_api_version'),
            'deployment_name': self.config.get('OpenAI', 'deployment_name'),
            'openai_api_key': self.config.get('OpenAI', 'openai_api_key'),
            'openai_api_type': self.config.get('OpenAI', 'openai_api_type'),
            'temperature': self.config.get('OpenAI', 'temperature')
        }

    def _get_azure_data_factory_config(self):
        return {
            'api_version': self.config.get('AzureDataFactory', 'api_version'),
            'suscription_id': self.config.get('AzureDataFactory', 'suscription_id'),
            'resource_group': self.config.get('AzureDataFactory', 'rg_name'),
            'factory_name': self.config.get('AzureDataFactory', 'adf_name'),
            'tenant_id': self.config.get('AzureDataFactory', 'TENANT_ID'),
            'client_id': self.config.get('AzureDataFactory', 'CLIENT'),
            'client_secret': self.config.get('AzureDataFactory', 'KEY')
        }

# Example usage
config_reader = Reader()
openai_config = config_reader.openai_config
adf_config = config_reader.adf_config

print("OpenAI Config:")
print(openai_config)
print("\nAzure Data Factory Config:")
print(adf_config)
