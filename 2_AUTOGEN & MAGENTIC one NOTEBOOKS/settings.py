import os

from dotenv import load_dotenv

load_dotenv()



llm_config = {
    "provider": "AzureOpenAIChatCompletionClient",
    "config": {
        "model": "gpt-4o",
        "api_key": os.environ.get("AZURE_OPENAI_API_KEY", "3ShjYyRHd6t0VthIuoOUe1GEnwlj1tkNSHkOs6IrO1CxKQ3gHmsIJQQJ99BAACfhMk5XJ3w3AAABACOG3ddZ"),
        "azure_endpoint": os.environ.get("AZURE_OPENAI_URL", "https://aq-aoai-swedencentral.openai.azure.com/"),
        "api_version": "2024-10-21",
    },
}

# llm_websurfer = {
#     "temperature": 0,
#     "cache_seed": None,
#     "config_list": [
#         {
#             "model": "gpt-4o",
#             "api_type": "azure",
#             "api_key": os.environ.get("AZURE_OPENAI_API_KEY", ""),
#             "base_url": os.environ.get("AZURE_OPENAI_URL", ""),
#             "api_version": "2024-08-01-preview",
#         }
#     ],
# }

# browser_config = {
#     "viewport_size": 4096,
#     "bing_api_key": os.environ.get(bing_api_key_name),
# }

generated_directory = "./generated"

# if os.environ.get(bing_api_key_name) is None:
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#     print("WARNING: Bing API key not found. Some examples won't work.")
#     print(f"Set the environment variable {bing_api_key_name}")
#     print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if os.environ.get("AZURE_OPENAI_API_KEY") is None:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("WARNING: Azure OpenAI API key not found. None of the examples will work.")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

if os.environ.get("AZURE_OPENAI_URL") is None:
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("WARNING: Azure OpenAI API URL not found. None of the examples will work.")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
