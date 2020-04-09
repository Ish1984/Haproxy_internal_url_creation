#!/bin/sh
#Select the Region
###################
# Available Options#
# qa 
# edc
# ndc
# uk
# ukdr
# Region will be passed as the parameter by user in Jenkins job
echo "Switching to Job Workspace "
echo " "
echo "#########################"
cd ${workspace}
echo "Converting dns.yaml to dns.json"
echo " "
python3.8 -c 'import sys, yaml, json; json.dump(yaml.load(sys.stdin), sys.stdout, indent=4)' < dns.yaml > dns.json
echo " "
echo "$Region selected by user"
echo "Extracting jsonpath for $Region "
python3.8 jsonpath.py dns.json |grep $Region |grep -v region > $Region.txt
echo " "
echo " "
echo "Executing Shell script for $Region URL creation"
echo " "
echo "Calling backend_url_script.py script"
python backend_url_script.py > $Region_url.txt

