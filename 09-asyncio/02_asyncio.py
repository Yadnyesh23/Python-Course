import asyncio

async def brew_chai(name):
    print(f"Brewing {name} chai....")
    await asyncio.sleep(3)
    print(f"{name} chai is ready!")

async def main():
    await asyncio.gather(
        brew_chai("Masala"),
        brew_chai("Ginger"),
        brew_chai("Lemon"),
    )

asyncio.run(main())