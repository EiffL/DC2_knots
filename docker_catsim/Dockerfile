FROM lsstdesc/stack-sims:w_2018_26-sims_2_9_0
MAINTAINER EiffL <francois.lanusse@gmail.com>

USER root

RUN mkdir /build

# Activate the stack environment and install required software
RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_sims \
    && pip install corner h5py \
    && pip install git+https://github.com/LSSTDESC/gcr-catalogs.git@f6b558b \
    && pip install git+https://github.com/drphilmarshall/OM10.git \
    && pip install git+https://github.com/drphilmarshall/LensPop.git

RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_sims \
    && cd /build && git clone https://github.com/LSSTDESC/Twinkles \
    && cd Twinkles && git checkout master \
    && eups declare -r . twinkles -t current \
    && setup twinkles

RUN source /opt/lsst/software/stack/loadLSST.bash && setup lsst_sims \
    && cd /build && git clone https://github.com/LSSTDESC/sims_GCRCatSimInterface \
    && cd sims_GCRCatSimInterface && git checkout master \
    && eups declare -r . sims_GCRCatSimInterface -t current \
    && setup sims_GCRCatSimInterface \
    && chmod a+x bin.src/generateInstCat.py \
    && bash /opt/lsst/software/stack/stack/miniconda3-4.3.21-10a4fa6/Linux64/sims_catUtils/2.9.0.sims/support_scripts/get_kepler_light_curves.sh \
    && bash /opt/lsst/software/stack/stack/miniconda3-4.3.21-10a4fa6/Linux64/sims_catUtils/2.9.0.sims/support_scripts/get_kepler_dmag.sh \
    && bash /opt/lsst/software/stack/stack/miniconda3-4.3.21-10a4fa6/Linux64/sims_catUtils/2.9.0.sims/support_scripts/get_mdwarf_flares.sh

USER lsst

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["bash", "/entrypoint.sh"]
