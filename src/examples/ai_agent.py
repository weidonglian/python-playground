import os
import sys
from tabnanny import verbose
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel

# Load environment variables from .env file
load_dotenv()

# Load the API key from environment
google_api_key = os.getenv('GOOGLE_API_KEY')

# Define dependencies
class CodeContext(BaseModel):
    language: str
    style: str
    include_comments: bool
    include_tests: bool
    include_docstrings: bool

async def run_agent_with_prompt(prompt: str):
    """Run the agent with a given prompt"""
    # Create agent with Google's Gemini model
    agent = Agent(
        model=GoogleModel(model_name="gemini-2.5-flash"),
        system_prompt="""
        You are an expert software developer. Write code according to the user's request.
        Follow the context provided to ensure code quality and standards.
        """,
        deps_type=CodeContext,
    )

    context = CodeContext(
        language="Python",
        style="PEP8, clean and readable full complete code pyproject managed via uv",
        include_comments=True,
        include_tests=True,
        include_docstrings=True,
    )

    try:
        result = await agent.run(prompt, deps=context)

        # Pretty print the result
        print("=" * 80)
        print("🤖 AI Agent Response")
        print("=" * 80)
        print()
        print(result.output)
        print()
        print("=" * 80)

    except Exception as e:
        print(f"❌ Error: {e}")

async def interactive_mode():
    """Run the agent in interactive mode"""
    print("🤖 AI Agent - Interactive Mode")
    print("Enter your prompts (or 'quit' to exit)")
    print("-" * 60)

    while True:
        try:
            user_prompt = input("\n💭 Your prompt: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 Goodbye!")
            break

        if user_prompt.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break

        if not user_prompt:
            print("❌ Please enter a prompt!")
            continue

        print("\n🔄 Processing...")
        await run_agent_with_prompt(user_prompt)

async def main():
    # Check if prompt is provided as command line argument
    if len(sys.argv) > 1:
        # Use command line argument as prompt
        prompt = " ".join(sys.argv[1:])
        print(f"🔄 Processing prompt: {prompt}")
        await run_agent_with_prompt(prompt)
    else:
        # Run in interactive mode
        await interactive_mode()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())