#!/usr/bin/env python3
from prometheus_client import start_http_server, Gauge

# Type
host_type = Gauge('host_type', 'Type of host', ['host_type'])
host_type.labels('virtual_machine').set(1.0)

if __name__ == '__main__':
    # Start
    start_http_server(8080)
    print("Metrics server started on http://0.0.0.0:8080")

    # Keep alive
    while True:
        pass  # или time.sleep(60)
