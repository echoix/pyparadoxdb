#!/usr/bin/env python

# pyparadox test.
# Copyright 2013 Grigory Petrov
# See LICENSE for details.

import pyparadoxdb

oDb = pyparadoxdb.open("test.db")
print(f"record size: {oDb.recordSize}")
print(f"header size: {oDb.headerSize}")
print(f"file type: {oDb.fileType}")
ABOUT = {1: "64m", 2: "128M", 3: "192M", 4: "256M"}
print(f"max table size: {ABOUT[oDb.maxTableSize]}")
print(f"number of records: {oDb.recordsCount}")
print(f"Sort order: {oDb.sortOrder:x}")
print(f"write protection: {oDb.writeProtected}")
print(f"Common version: {oDb.versionCommon:x}")
print(f"Next auto increment: {oDb.nextAutoInc}")
print(f"Data version: {oDb.versionData:04x}")
print(f"Codepage: {oDb.codepage:04x}")
print(f"Table name: {oDb.tableName}")
print(f"Sort order text: {oDb.sortOrderTxt}")
print("Fields: ")
for oField in oDb.fields:
    print(f"  {oField.name} ({oField.typeAsTxt()})")
print("Records: ")
for oRecord in oDb.records:
    print(f"  {oRecord}".encode())
