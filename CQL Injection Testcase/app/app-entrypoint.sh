#!/bin/bash

set -e

until cqlsh -e 'describe keyspaces' cassandra; do
  >&2 echo "Cassandra is not ready yet - sleeping"
  sleep 5
done

cqlsh -f init-cassandra.cql cassandra
python app.py
