import asyncio
import aiohttp  # ye library h asybc requests k lie

# async fn hm bina asyncio k call ni kr skte
# ye non blocking operation

# async def brew(name):
#     print(f"brewing {name}...")
#     await asyncio.sleep(3)
#     print(f"{name} is ready...")


# async def main():
#     await asyncio.gather(
#         brew("Masala Chai"),
#         brew("ginger Chai"),
#         brew("Cinaamon Chai")
#     )

# asyncio.run(main())


# Another Example
async def fetch_url(session,url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status:", {response.status})


async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        [fetch_url(session,url) for url in urls]
        await asyncio.gather(*tasks)

asyncio.run(main())