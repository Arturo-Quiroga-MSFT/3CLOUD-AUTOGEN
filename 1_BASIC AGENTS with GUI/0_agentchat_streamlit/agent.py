import yaml
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_core.models import ChatCompletionClient


class Agent:
    def __init__(self) -> None:
        # Load the model client from config.
        with open("/Users/arturoquiroga/3CLOUD-AUTOGEN/1_AUTOGEN-SDK-SAMPLES/0_agentchat_streamlit/model_config.yml", "r") as f:
            model_config = yaml.safe_load(f)
        model_client = ChatCompletionClient.load_component(model_config)
        self.agent = AssistantAgent(
            name="assistant",
            model_client=model_client,
            system_message="You are a helpful AI assistant.",
        )

    async def chat(self, prompt: str) -> str:
        response = await self.agent.on_messages(
            [TextMessage(content=prompt, source="user")],
            CancellationToken(),
        )
        assert isinstance(response.chat_message, TextMessage)
        return response.chat_message.content
