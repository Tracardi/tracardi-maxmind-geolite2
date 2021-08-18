import asyncio
from tracardi_maxmind_geolite2.plugin import GeoIPAction

kwargs = {
    "source": {
        "id": "5600c92a-835d-4fbe-a11d-7076fd983434"
    },
    "ip": "payload@ip"
}


async def main():
    geo = await GeoIPAction.build(**kwargs)
    result = await geo.run(payload={"ip": "195.210.25.6"})
    print(result)


asyncio.run(main())
