import os
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

async def main():
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

    result = await agent.run(
        "Write a Python function that takes a list of numbers and returns the sum of the even numbers.",
        deps=context,
    )

    print(result)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())