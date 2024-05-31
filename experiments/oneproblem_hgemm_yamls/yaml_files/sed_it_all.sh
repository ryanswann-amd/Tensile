#!/bin/bash
sed -i.bak 's/1LDSBuffer: \[0, 1\]/1LDSBuffer: \[0, 1, 2\]/g' *.yaml
sed -i.bak 's/NumWarmups: 20/NumWarmups: 10/g' *.yaml 
sed -i.bak 's/StreamKFullTiles: \[0, 1\]/StreamKFullTiles: \[0, 1, 2\]/g' *.yaml
sed -i.bak 's/- Exact:/#- Exact:/g' *.yaml 
sed -i.bak 's/#- Exact: \[128, 128, 1, 128\]/- Exact: \[8192, 4864, 1, 2944\]/g' *.yaml