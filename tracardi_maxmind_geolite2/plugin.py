from typing import Optional
from tracardi.service.storage.helpers.source_reader import read_source
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.result import Result
from tracardi_dot_notation.dot_accessor import DotAccessor

from tracardi_maxmind_geolite2.model.maxmind_geolite2_client import GeoIpConfiguration, \
    PluginConfiguration, MaxMindGeoLite2


class GeoIPAction(ActionRunner):

    @staticmethod
    async def build(**kwargs) -> 'GeoIPAction':
        plugin = GeoIPAction(**kwargs)
        resource = await read_source(resource_id=plugin.config.source.id)
        geoip2_config = GeoIpConfiguration(
            **resource.config
        )

        plugin.client = MaxMindGeoLite2(geoip2_config)

        return plugin

    def __init__(self, **kwargs):
        self.client = None  # type: Optional[MaxMindGeoLite2]
        self.config = PluginConfiguration(**kwargs)

        if self.config.ip is None:
            raise ValueError("IP not set. Please check configuration.")

    async def run(self, payload):

        dot = DotAccessor(self.profile, self.session, payload, self.event, self.flow)

        ip = dot[self.config.ip]

        location = await self.client.fetch(ip)

        result = {
            "city": location.city.name,
            "country": {
                "name": location.country.name,
                "code": location.country.iso_code
            },
            "county": location.subdivisions.most_specific.name,
            "postal": location.postal.code,
            "latitude": location.location.latitude,
            "longitude": location.location.longitude
        }

        return Result(port="location", value=result)


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_maxmind_geolite2.plugin',
            className='GeoIPAction',
            inputs=["payload"],
            outputs=['location'],
            version='0.1.5',
            license="MIT",
            author="Risto Kowaczewski",
            init={
                "source": {
                    "id": None,
                },
                "ip": "event@metadata.ip"
            }
        ),
        metadata=MetaData(
            name='GeoIp service',
            desc='Converts IP to location information.',
            type='flowNode',
            width=200,
            height=100,
            icon='location',
            group=["Location"]
        )
    )
