import asyncio
from tracardi_maxmind_geolite2.model.maxmind_geolite2_client import GeoIpConfiguration, MaxMindGeoLite2Client
from tracardi_maxmind_geolite2.plugin import GeoIPAction

# config = GeoIpConfiguration(
#     license="xxx",
#     database="GeoLite2-City.mmdb"
# )
#
#
# c = MaxMindGeoLite2Client(config)
# x = c.read('195.210.25.6')
# print(x.country)

kwargs = {
    "source": {
        "id": "5600c92a-835d-4fbe-a11d-7076fd983434"
    }
}

async def main():
    geo = await GeoIPAction.build(**kwargs)
    result = await geo.run("195.210.25.6")
    print(result)

asyncio.run(main())
