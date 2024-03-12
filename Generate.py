import os
import json
from AzureOpenai import OpenAIConnector  # Assuming you have a module for interacting with Azure OpenAI

class Generator:
    def __init__(self, openai_config, adf_folder='ADF'):
        self.openai_config = openai_config
        self.adf_folder = adf_folder

    def generate_dataset_json(self, dataset_name):
        # Use OpenAI to generate JSON for dataset
        dataset_json = OpenAIConnector.generate_dataset_json(dataset_name, self.openai_config)
        self._save_json(dataset_json, 'Dataset', dataset_name)

    def generate_linked_services_json(self, linked_service_name):
        # Use OpenAI to generate JSON for linked service
        linked_service_json = OpenAIConnector.generate_linked_service_json(linked_service_name, self.openai_config)
        self._save_json(linked_service_json, 'LinkedServices', linked_service_name)

    def generate_pipeline_json(self, pipeline_name):
        # Use OpenAI to generate JSON for pipeline
        pipeline_json = OpenAIConnector.generate_pipeline_json(pipeline_name, self.openai_config)
        self._save_json(pipeline_json, 'Pipelines', pipeline_name)

    def generate_integration_runtime_json(self, integration_runtime_name):
        # Use OpenAI to generate JSON for integration runtime
        integration_runtime_json = OpenAIConnector.generate_integration_runtime_json(integration_runtime_name, self.openai_config)
        self._save_json(integration_runtime_json, 'IntegrationRuntime', integration_runtime_name)

    def _save_json(self, data, component_type, component_name):
        folder_path = os.path.join(self.adf_folder, component_type)
        os.makedirs(folder_path, exist_ok=True)
        file_name = f"{component_name}.json"
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"JSON for {component_type} '{component_name}' saved to {file_path}")

# Example usage
if __name__ == "__main__":
    config_reader = ConfigReader()
    openai_config = config_reader.get_openai_config()
    
    generator = Generator(openai_config)
    generator.generate_dataset_json('my_dataset')
    generator.generate_linked_services_json('my_linked_service')
    generator.generate_pipeline_json('my_pipeline')
    generator.generate_integration_runtime_json('my_integration_runtime')
