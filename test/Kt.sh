#!/bin/sh

rm -f KtJets.root

cp CaloTowers.xml PoolFileCatalog.xml

Mange --parameter-set Kt.txt
