#!/bin/bash

docker build -t powerpanel .

docker build -t powerpanel-exporter exporter
