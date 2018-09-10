# DC2_knots

Repository to host production and validation code for knots component in DESC DC2
images.


Command to build instance catalog:
```
$ shifter --entrypoint --image=docker:eiffl/catsim --env=HDF5_USE_FILE_LOCKING=FALSE --env=SIMS_GCRCATSIMINTERFACE_DIR=/build/sims_GCRCatSimInterface generateInstCat.py --fov 0.2 --db /global/projecta/projectdirs/lsst/groups/SSim/DC2/minion_1016_desc_dithered_v4.db --agn_db_name /global/projecta/projectdirs/lsst/groups/SSim/DC2/agn_db_mbh_7.0_m_i_30.0_gcr_protodc2_v3.db --disable_dithering --descqa_catalog proto-dc2_v3.0_addon_knots --protoDC2_ra 55.064 --protoDC2_dec -29.783 --ids 2187645 2187601 2230250 2230287 2365496 2365539 699447 660233 --out_dir=`pwd`
```

to run imsim in fast mode:
```
$ shifter --entrypoint --image=docker:eiffl/imsim imsim.py --disable_sensor_model --psf DoubleGaussian --processes=32 phosim_cat_2187645.txt
```

I'm selecting a few visits in multiple bands with small seeing and deeper 
fiveSigmaDepth in the create_visit_list.ipynb notebook

After selecting a few visits in different bands, I've manually matched the orientation of the telescope in all visits 
(so that galaxies will appear at the same position on the sensors), increased the exposure time to 120s and decreased
the seeing to 0.001 arcsec, so that it becomes possible to resolve individual knots.
