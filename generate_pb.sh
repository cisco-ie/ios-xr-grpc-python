#!/bin/bash
#pip install grpcio-tools
python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. ems_grpc.proto telemetry.proto