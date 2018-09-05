# DC2_knots

Repository to host production and validation code for knots component in DESC DC2
images.


Command to build instance catalog:
```
$ shifter --entrypoint --image=docker:eiffl/catsim --env=HDF5_USE_FILE_LOCKING=FALSE generateInstCat.py --db /global/projecta/projectdirs/lsst/groups/SSim/DC2/minion_1016_desc_dithered_v4.db --agn_db_name /global/projecta/projectdirs/lsst/groups/SSim/DC2/agn_db_mbh_7.0_m_i_30.0_gcr_protodc2_v3.db --descqa_catalog proto-dc2_v2.1.2 --out_dir=`pwd` --protoDC2_ra 55.064 --protoDC2_dec -29.783 --enable_sprinkler --ids 181898
```

to run imsim in fast mode:
```
$ shifter --entrypoint --image=docker:eiffl/imsim imsim.py --disable_sensor_model --psf DoubleGaussian --processes=32 phosim_cat_181898.txt
```
