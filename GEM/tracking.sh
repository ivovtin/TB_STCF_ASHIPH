#!/bin/bash


count=0
indirs=();
while read str
do
	count=$[ count + 1 ]
	indirs+=($str)
	echo "Line contents are : $str "
done < runs_list.dat
echo "count: $count "

##for indir in ${indirs[@]}
for (( i = 0; i < $count; i++ ))
do
  intfile="${indirs[i]}.root"
  echo $intfile
  nice -n 19 ~/development/TB_sw/gemCluster/process/trackprocess.sh $intfile
done 

