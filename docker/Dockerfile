FROM lsstdesc/stack-sims:w_2018_26-sims_2_9_0
MAINTAINER EiffL <francois.lanusse@gmail.com>

USER root

RUN mkdir /build

# Activate the stack environment and install required software
RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_sims \
    && cd /build && git clone https://github.com/lsst/sims_GalSimInterface \
    && cd sims_GalSimInterface \
    && eups declare -r . sims_GalSimInterface -t current \
    && setup sims_GalSimInterface

RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_sims \
    && cd /build && git clone https://github.com/LSSTDESC/imSim \
    && cd imSim \
    && eups declare -r . imsim -t current \
    && setup imsim

USER lsst

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["bash", "/entrypoint.sh"]
