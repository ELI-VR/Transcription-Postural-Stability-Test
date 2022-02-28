#!/bin/bash

#create directory if not yet existing
mkdir -p data/post_stability/


echo "  Processing live data"

python -m post_stability.post_stability_data_processing "$1" data/post_stability

echo " velocities.csv has been generated"