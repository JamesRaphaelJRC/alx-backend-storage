#!/usr/bin/env bash
# Initializes a shell script and changes its user permission to execute automatcaally

if [ $# -eq 0 ]
then
  echo "No argument provided"
  exit 1
fi

file=$1
touch $file
chmod u+x $file
echo "#!/usr/bin/env bash" > $file
vim $file
