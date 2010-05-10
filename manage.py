#!/usr/bin/env python
from migrate.versioning.shell import main

main(url='postgres://postgres:suite101@172.16.31.106:5432/collector',repository='migrations')
