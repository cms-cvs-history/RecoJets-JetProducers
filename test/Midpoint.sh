#!/bin/sh

rm -f MidpointJets.root

cp CaloTowers.xml PoolFileCatalog.xml

Mange --parameter-set Midpoint.txt
