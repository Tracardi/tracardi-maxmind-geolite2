import asyncio
from tracardi_maxmind_geolite2.plugin import GeoIPAction

kwargs = {
    "source": {
        "id": "3a77663c-ae26-4e91-9f24-fdb3b0f295fd"
    },
    "ip": "payload@ip"
}


async def main():
    geo = await GeoIPAction.build(**kwargs)
    result = await geo.run(payload={"ip": "195.210.25.6"})
    print(result)


asyncio.run(main())
