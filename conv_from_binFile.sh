#!/bin/bash

datadir="/home/ovtin/development/TB_STCF_ASHIPH/24112024"  
indirs=()

count=0
while read str
do
	count=$[ count + 1 ]
	indirs+=($str)
	echo "Line contents are : $str "
done < runs_list.dat
echo "count: $count "

#nev=()
#while read N
#do
#	count=$[ count + 1 ]
#	nev+=($N)
#	echo "Line contents are : $N "
##done < runs_nev.dat

for (( i = 0; i < $count; i++ ))
do
  	outfile="${indirs[i]}.root"
 
	nice -n 19 /home/ovtin/development/TB_STCF_ASHIPH/procn24dec24 7 $datadir/${indirs[i]}/wave_0.dat $datadir/${indirs[i]}/wave_2.dat $datadir/${indirs[i]}/wave_4.dat $datadir/${indirs[i]}/wave_6.dat $datadir/${indirs[i]}/wave_9.dat $datadir/${indirs[i]}/wave_11.dat $datadir/${indirs[i]}/wave_13.dat $datadir/$outfile -1000 2
  	##qsub -shell n -b y -V -N bin_to_root -cwd nice -n 19 /home/ovtin/development/TB_SND_ASHIPH/procn2jul18 $datadir/${indirs[i]}/wave_0.dat $datadir/${indirs[i]}/wave_4.dat $datadir/${indirs[i]}/wave_2.dat $datadir/$outfile -1000 20 0.0 0.0 2

done 

