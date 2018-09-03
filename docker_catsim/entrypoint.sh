#!/bin/sh

# This script will setup the lsst stack before executing the command
source /opt/lsst/software/stack/loadLSST.bash
setup lsst_sims
setup twinkles
setup sims_GCRCatSimInterface
export PATH=$PATH:/build/sims_GCRCatSimInterface/bin.src

# Hand off to the CMD
exec "$@"
