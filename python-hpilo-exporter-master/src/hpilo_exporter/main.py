"""
Entrypoint for the application
"""

import argparse

from hpilo_exporter.exporter import ILOExporterServer


def main():

    # Serve request on: http://192.168.2.143:9416/metrics
    # request sample: GET http://192.168.2.143:9416/metrics?ilo_host=
    parser = argparse.ArgumentParser(description='Exports ilo heath_at_a_glance state to Prometheus')

    parser.add_argument('--address', type=str, dest='address', default='192.168.2.143', help='address to serve on')
    parser.add_argument('--port', type=int, dest='port', default='9416', help='port to bind')
    parser.add_argument('--endpoint', type=str, dest='endpoint', default='/metrics',
                        help='endpoint where metrics will be published')

    args = parser.parse_args()

    exporter = ILOExporterServer(**vars(args))
    exporter.run()


if __name__ == '__main__':
    main()
