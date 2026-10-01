# Runs the HTTP REST guide of the NanoPing docs against two nodes.
#
# Start the client node with
#
#   np up --rest-api 127.0.0.1:10565
#
# and the hub server node with `np -c config.yaml up`, where config.yaml is
#
#   node:
#     name: My Server
#   http:
#     address: 127.0.0.1:8769
#   hubServer:
#     authenticationByRequest:
#       timeout: 5m
#   restApi:
#     address: 127.0.0.1:10566
#   pipelines: {}
#
# Then run `python main.py`.
import argparse
import asyncio
import sys

from guide import Addresses, run

parser = argparse.ArgumentParser()
parser.add_argument("--client", default="http://127.0.0.1:10565")
parser.add_argument("--server", default="http://127.0.0.1:10566")
parser.add_argument("--server-http", default="http://127.0.0.1:8769")
arguments = parser.parse_args()

try:
    asyncio.run(run(Addresses(arguments.client, arguments.server, arguments.server_http), print))
except Exception as error:
    print(error, file=sys.stderr)
    sys.exit(1)
