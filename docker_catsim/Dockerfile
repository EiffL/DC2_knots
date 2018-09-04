FROM lsstdesc/stack-sims:w_2018_13-sims_2_7_0
MAINTAINER EiffL <francois.lanusse@gmail.com>

USER root

RUN mkdir /build

# Activate the stack environment and install required software
RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_sims \
    && pip install corner h5py \
    && pip install git+https://github.com/LSSTDESC/gcr-catalogs.git@v0.7.2 \
    && pip install git+https://github.com/drphilmarshall/OM10.git@0.8 \
    && pip install git+https://github.com/drphilmarshall/LensPop.git@0.8

RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_sims \
    && cd /build && git clone https://github.com/LSSTDESC/Twinkles \
    && cd Twinkles && git checkout DC2-Run1.2-v2 \
    && eups declare -r . twinkles -t current \
    && setup twinkles

RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_sims \
    && cd /build && git clone https://github.com/LSSTDESC/sims_GCRCatSimInterface \
    && cd sims_GCRCatSimInterface && git checkout v0.2.0 \
    && eups declare -r . sims_GCRCatSimInterface -t current \
    && setup sims_GCRCatSimInterface \
    && chmod a+x bin.src/generateInstCat.py \
    && bash /opt/lsst/software/stack/stack/miniconda3-4.3.21-10a4fa6/Linux64/sims_catUtils/2.7.0.sims/support_scripts/get_kepler_light_curves.sh

USER lsst

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["bash", "/entrypoint.sh"]
