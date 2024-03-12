
import json
import pandas as pd
import configparser
import adal


def getDeployConfigs(self):

        config_block = self.configparser['DepConfigs']
        api_vesrion = config_block.get("api_version")
        subscription_id = config_block.get("suscription_id")
        rg_name = config_block.get("rg_name")
        adf_name = config_block.get("adf_name")
        TENANT_ID = config_block.get("TENANT_ID")
        CLIENT = config_block.get("CLIENT")
        KEY = config_block.get("KEY")

        """ Token genration script."""
        authority_url = 'https://login.microsoftonline.com/'+TENANT_ID
        context = adal.AuthenticationContext(authority_url)
        token = context.acquire_token_with_client_credentials(
            resource='https://management.azure.com',
            client_id=CLIENT,
            client_secret=KEY
        )
        return api_vesrion, subscription_id, rg_name, adf_name, token["accessToken"] 