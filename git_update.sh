#!/bin/bash
git add .
if [ -z "$1" ]
then
        git commit -m "doing some task"
else
        git commit -m "$1"
fi
git push
