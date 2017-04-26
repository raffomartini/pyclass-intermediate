#!/bin/bash
timestamp=$(date +%Y-%m-%d--%T)
git add *
git commit -m "$timestamp"
git push origin master
cd 2017-04-24/
git pull