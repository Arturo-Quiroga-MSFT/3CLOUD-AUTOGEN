# Using AgentGroupChat to facilitate communication between agents
# Exercise: Complete the code to set up a group chat between two agents

import asyncio
import datetime
import os

import dotenv
from azure.core.exceptions import ClientAuthenticationError
from azure.identity import DefaultAzureCredential
from semantic_kernel.agents.agent import Agent
from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import (
    AzureChatCompletion,
)
from semantic_kernel.exceptions.function_exceptions import (
    FunctionExecutionException,
)
from semantic_kernel.kernel import Kernel

from settings import llm_config

dotenv.load_dotenv()

azure_openai_endpoint = os.getenv("AZURE_OPENAI_URL")
pool_management_endpoint = os.getenv("ACA_POOL_MANAGEMENT_ENDPOINT")


def auth_callback_factory(scope):
    auth_token = None

    async def auth_callback() -> str:
        """Auth callback for the SessionsPythonTool."""
        nonlocal auth_token
        current_utc_timestamp = int(
            datetime.datetime.now(datetime.timezone.utc).timestamp()
        )

        if not auth_token or auth_token.expires_on < current_utc_timestamp:
            credential = DefaultAzureCredential()

            try:
                auth_token = credential.get_token(scope)
            except ClientAuthenticationError as cae:
                err_messages = getattr(cae, "messages", [])
                raise FunctionExecutionException(
                    f"Failed to retrieve the client auth token with messages: {' '.join(err_messages)}"
                ) from cae

        return auth_token.token

    return auth_callback


def setup_chat_service(kernel: Kernel, service_id: str) -> None:
    """Set up a chat completion service for the kernel."""
    deployment_name = llm_config.get("config", {}).get("model", "gpt-4o")
    endpoint = llm_config.get("config", {}).get(
        "azure_endpoint", azure_openai_endpoint
    )
    api_key = llm_config.get("config", {}).get("api_key", None)
    api_version = llm_config.get("config", {}).get("api_version", "2024-06-01")

    chat_service = AzureChatCompletion(
        service_id=service_id,
        endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
        deployment_name=deployment_name,
    )
    kernel.add_service(chat_service)


async def create_code_agent() -> Agent:
    """Create an agent specialized in executing Python code.

    TODO: Implement this function to create a code execution agent with the following capabilities:
    1. Create a kernel and set up the chat service
    2. Configure the Python code interpreter tool
    3. Add the code interpreter plugin to the kernel
    4. Create and return a ChatCompletionAgent with appropriate name and description
    """
    kernel = Kernel()
    service_id = "code-execution-service"
    setup_chat_service(kernel, service_id)

    # TODO: Create the Python code interpreter using SessionsPythonTool
    # python_code_interpreter = SessionsPythonTool(...)

    # TODO: Add the Python code interpreter plugin to the kernel
    # plugin = kernel.add_plugin(...)

    # TODO: Define an appropriate description for the code agent
    description = """I am a Python Code Execution Agent. 
    I can run Python code to solve problems using the PythonCodeInterpreter plugin.
    """

    # TODO: Create and return a ChatCompletionAgent
    # code_agent = ChatCompletionAgent(...)

    return None  # Replace with your implemented agent


async def create_chat_agent() -> Agent:
    """Create a chat agent that interacts with users and coordinates with the code agent.

    TODO: Implement this function to create a math problem solver agent that:
    1. Creates a kernel and sets up the chat service
    2. Defines an appropriate description explaining how to interact with the code agent
    3. Creates and returns a ChatCompletionAgent
    """
    # TODO: Implement this function
    return None


async def main():
    """Main function to coordinate the agent group chat.

    TODO: Complete the implementation to:
    1. Create the code and chat agents
    2. Set up an agent group chat
    3. Create a chat history with initial system message
    4. Add the user question to the chat
    5. Start the group chat and display messages from each agent
    """
    # Create the agents
    code_agent = await create_code_agent()
    chat_agent = await create_chat_agent()

    # TODO: Create an agent group chat with the agents
    # group_chat = AgentGroupChat(...)

    # TODO: Set up the initial chat history with a system message
    # chat_history = ...

    # User's question
    user_question = "Calculate the fibonacci number of 10"
    print(f"User: {user_question}")
    print("\n--- Starting group chat ---\n")

    # TODO: Add the user's message to the group chat
    # await group_chat.add_chat_message(...)

    # TODO: Implement the message handling loop to display agent messages
    # async for message in group_chat.invoke():
    #     # Display who's speaking and what they're saying
    #     ...

    print("\n--- Group chat completed ---\n")


if __name__ == "__main__":
    asyncio.run(main())
