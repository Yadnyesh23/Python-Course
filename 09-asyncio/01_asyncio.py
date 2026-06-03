import asyncio

async def brew_chai():
    print("Brewing chai....")
    await asyncio.sleep(3)
    print("Chai is ready")
    
# brew_chai()

asyncio.run(brew_chai())