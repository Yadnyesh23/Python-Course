import asyncio

async def prepare_coffee():
    print("Starting coffee...")
    await asyncio.sleep(3)
    print("Coffee ready!")
    
async def prepare_sandwich():
    print("Starting sandwich...")
    await asyncio.sleep(3)
    print("Sandwich ready!")
    
async def main():
    await asyncio.gather(
        prepare_coffee(),
        prepare_sandwich()
    )
    # await prepare_coffee()
    # await prepare_sandwich()

asyncio.run(main())

