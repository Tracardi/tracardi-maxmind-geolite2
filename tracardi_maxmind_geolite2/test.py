import asyncio
from tracardi_maxmind_geolite2.plugin import GeoIPAction

kwargs = {
    "source": {
        "id": "b1d4ea68-f6d5-428e-a642-6fb827ae232c"
    },
    "ip": "payload@ip"
}


async def main():
    geo = await GeoIPAction.build(**kwargs)
    result = await geo.run(payload={"ip": "195.210.25.6"})
    print(result)


asyncio.run(main())
