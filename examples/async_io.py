import asyncio

async def say_hello():
    print("Hello, async world!")

async def main():
    await say_hello()
    print("finish!")


if __name__ == "__main__":
    asyncio.run(main())