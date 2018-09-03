#!/bin/sh

# This script will setup the lsst stack before executing the command
source /opt/lsst/software/stack/loadLSST.bash
setup lsst_sims
setup sims_GalSimInterface
setup imsim
export PATH=$PATH:/build/imSim/bin.src

# Hand off to the CMD
exec "$@"
