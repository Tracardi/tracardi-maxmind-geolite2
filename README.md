# GeoLite2 plugin

This plugin reads connects geoIP servers and returns localisation based on the provided ip address.

# Configuration

Example:

```json
{
  "source": {
    "id": "5600c92a-835d-4fbe-a11d-7076fd983434"
  },
  "ip": "payload@ip"
}
```

To run this plugin you must provide source id that has configured GeoLite2 server credentials.

Example of source configuration for GeoLite2 API:

```json
{
  "webservice": {
    "accountId": <you-account-id>,
    "license": <license-key>
  }
}
```

You must provide `license-key` and `account-id` to connect to MaxMind GeoLite2 API.

Example of source configuration for GeoLite2 local database file:

```json
{
  "database": <path-to-database>
}
```

If you provide local database for city locations you can use it locally without connecting to remote API.
