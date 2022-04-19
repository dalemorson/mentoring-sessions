#!/bin/bash
for num in {1..10}
do
    aws s3api create-bucket --bucket mentoring-bucket-prefix-${num} --region us-east-1
done