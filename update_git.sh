#!/bin/bash
timestamp=$(date +%Y-%m-%d--%T)
git add *
git commit -m "$1"
git push origin master