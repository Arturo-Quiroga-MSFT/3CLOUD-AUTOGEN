import asyncio
import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from autogen_core import (
    DefaultTopicId,
    MessageContext,
    RoutedAgent,
    default_subscription,
    message_handler,
)
from autogen_core.code_executor import CodeBlock, CodeExecutor, CodeResult
from autogen_core.models import (
    AssistantMessage,
    ChatCompletionClient,
    LLMMessage,
    SystemMessage,
    UserMessage,
)


@dataclass
class Message:
    content: str


class RemoteExecutor(CodeExecutor):
    """
    A code executor that runs code blocks in a remote Azure Container Apps instance.
    This allows for secure execution in an isolated environment with appropriate resources.

    EXERCISE: Implement this class to connect to and execute code in a remote container.

    Requirements for ACA ingress configuration:
    1. Your ACA container must have ingress enabled with an external endpoint
    2. The endpoint should be HTTPS for production use
    3. IP restrictions should be configured if needed for security
    4. Authentication should be enabled (API key is used in this code)
    """

    def __init__(
        self,
        timeout: Optional[int] = 60,
        pool_management_endpoint: Optional[str] = None,
        additional_session_config: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Initialize the RemoteExecutor with connection details for Azure Container Apps.

        Args:
            timeout: Maximum time in seconds to wait for code execution
            pool_management_endpoint: Endpoint for the Azure Container Apps session pool
            additional_session_config: Additional configuration parameters for the session
        """
        super().__init__()

        # TODO: Initialize the timeout parameter

        # TODO: Set the pool_management_endpoint, either from the parameter or from
        # environment variables. Use a placeholder value if not provided.

        # TODO: Initialize additional_session_config
        pass

    async def execute_code_blocks(
        self, code_blocks: List[CodeBlock], cancellation_token=None
    ) -> CodeResult:
        """
        EXERCISE: Implement this method to execute code blocks in a remote container

        Steps to implement:
        1. Create a SessionsPythonREPLTool with the appropriate configuration
        2. Execute each code block sequentially
        3. Collect logs and results
        4. Handle errors appropriately
        5. Return a CodeResult with the execution output and status

        Args:
            code_blocks: List of CodeBlock objects to execute
            cancellation_token: Optional token for cancellation

        Returns:
            CodeResult with execution output and status
        """
        # TODO: Initialize logs collection and exit_code

        try:
            # TODO: Create a SessionsPythonREPLTool with the proper configuration

            # TODO: Loop through and execute each code block
            # For each block:
            #   - Add a header to the logs
            #   - Execute the code block
            #   - Append results to logs
            #   - Handle any exceptions

            # TODO: Return the CodeResult with the combined logs and exit code
            pass

        except Exception:
            # TODO: Handle exceptions and return an appropriate CodeResult
            pass


def extract_markdown_code_blocks(markdown_text: str) -> List[CodeBlock]:
    """
    Extract code blocks from markdown text.

    Args:
        markdown_text: String containing markdown with code blocks

    Returns:
        List of CodeBlock objects
    """
    pattern = re.compile(r"```(?:\s*([\w\+\-]+))?\n([\s\S]*?)```")
    matches = pattern.findall(markdown_text)
    code_blocks: List[CodeBlock] = []
    for match in matches:
        language = match[0].strip() if match[0] else ""
        code_content = match[1]
        code_blocks.append(CodeBlock(code=code_content, language=language))
    return code_blocks


@default_subscription
class Assistant(RoutedAgent):
    def __init__(self, model_client: ChatCompletionClient) -> None:
        super().__init__("An assistant agent.")
        self._model_client = model_client
        self._chat_history: List[LLMMessage] = [
            SystemMessage(
                content="""Write Python script in markdown block, and it will be executed in a remote container.
                        Always save figures to file in the current directory. Do not use plt.show().
                        All code required to complete this task must be contained within a single response.""",
            )
        ]

    @message_handler
    async def handle_message(
        self, message: Message, ctx: MessageContext
    ) -> None:
        self._chat_history.append(
            UserMessage(content=message.content, source="user")
        )
        result = await self._model_client.create(self._chat_history)
        print(f"\n{'-' * 80}\nAssistant:\n{result.content}")
        self._chat_history.append(
            AssistantMessage(content=result.content, source="assistant")
        )  # type: ignore
        await self.publish_message(
            Message(content=result.content), DefaultTopicId()
        )  # type: ignore


@default_subscription
class Executor(RoutedAgent):
    def __init__(self, code_executor: CodeExecutor) -> None:
        super().__init__("A remote executor agent.")
        self._code_executor = code_executor

    @message_handler
    async def handle_message(
        self, message: Message, ctx: MessageContext
    ) -> None:
        code_blocks = extract_markdown_code_blocks(message.content)
        if code_blocks:
            result = await self._code_executor.execute_code_blocks(
                code_blocks, cancellation_token=ctx.cancellation_token
            )
            print(f"\n{'-' * 80}\nRemote Executor:\n{result.output}")
            await self.publish_message(
                Message(content=result.output), DefaultTopicId()
            )


async def run_remote_coding_agents():
    """
    EXERCISE: Complete this function to set up and run coding agents with remote execution.

    Steps:
    1. Load environment variables
    2. Create a runtime
    3. Initialize the model client
    4. Create a RemoteExecutor instance with appropriate configuration
    5. Register the Assistant and Executor agents
    6. Start the runtime and publish an initial message
    """
    # TODO: Load environment variables

    # TODO: Create a SingleThreadedAgentRuntime

    # TODO: Initialize the ChatCompletionClient

    # TODO: Create a RemoteExecutor with appropriate configuration
    # Hints:
    # - Set a reasonable timeout
    # - Configure the API key from environment variables
    # - Set appropriate session options (memory, CPU, etc.)

    # TODO: Register the assistant agent

    # TODO: Register the executor agent

    # TODO: Start the runtime and publish an initial message
    # Use a simple task like calculating a Fibonacci number as a test

    # TODO: Wait for the runtime to become idle before stopping


if __name__ == "__main__":
    asyncio.run(run_remote_coding_agents())
