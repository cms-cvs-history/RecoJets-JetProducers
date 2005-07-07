#!/bin/sh

rm -f KtJets.root

cp CaloTowers.xml PoolFileCatalog.xml

cmsRun --parameter-set Kt.txt
