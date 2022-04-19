#!/bin/bash
for bucket in $@
do
    aws s3api create-bucket --bucket ${bucket} --region us-east-1
done