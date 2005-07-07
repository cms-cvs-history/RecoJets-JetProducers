#!/bin/sh

rm -f MidpointJets.root

cp CaloTowers.xml PoolFileCatalog.xml

cmsRun --parameter-set Midpoint.txt
