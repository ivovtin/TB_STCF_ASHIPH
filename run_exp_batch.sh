#!/bin/bash

##root -l -b -q 'get_npe.C("ch1_point2_U53V_T15")'

U1=56
U2=56
U3=58
list=( 1 )

#for i in ${list[@]}
##for (( i = 1; i <= 16; i++ ))
#do 
#   echo "U1 = $U1, U2 = $U2, U3 = $U3" 
#   qsub -shell n -b y -V -N npe_res_sipms_u1-'${U1}'_u2-'${U2}'_u3-'${U3}' -cwd root -l -b -q 'get_npe.C("point'${i}'_sipms_u1-'${U1}'_u2-'${U2}'_u3-'${U3}'")'
#done
   
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe.C("p1_hum_u1-56_u2-56_u3-57_ndl_u32_fine_u2200")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe.C("p6_hum_u1-56_u2-56_u3-57_ndl_u32_fine_u2200")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe.C("p2_hum_u1-56_u2-56_u3-57_ndl_u31_fine_u2100-2")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe.C("p15_hum_u1-57_u2-57_u3-57_ndl_u34_fine_u2000")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe.C("p3_hum_u1-56_u2-56_u3-57_ndl_u30_fine_u2000")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe.C("p1_hum_u1-56_u2-56_u3-56_ndl_u32_fine_u2000")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe.C("p8_hum_u1-56_u2-56_u3-57")'

##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_PedFitCh1.C("p8_hum_u1-56_u2-56_u3-57")'

##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_woTRG2Cut.C("p11_hum_u1-57_u2-57_u3-57_ndl_u34_fine_u2000-TRG2bug")'  ##? cuts NDL, FM
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_woTRG2Cut.C("p15_hum_u1-57_u2-57_u3-57_ndl_u34_fine_u2000")'   ##? cuts NDL, FM
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_woTRG2Cut.C("p3_hum_u1-56_u2-56_u3-57_ndl_u30_fine_u2000")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_woTRG2Cut.C("p2_hum_u1-56_u2-56_u3-57_ndl_u31_fine_u2100")'

##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_woTRG2Cut_Point6.C("p6_hum_u1-56_u2-56_u3-57_ndl_u31_fine_u2100")'

##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_woTRG2Cut_PedFitCh13.C("p9_hum_u1-56_u2-56_u3-57_ndl_u34_fine_u2400")'


##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_Pedfit.C("p6_hum_u1-56_u2-56_u3-57_ndl_u32_fine_u2200")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_Pedfit.C("p5_hum_u1-56_u2-56_u3-57_ndl_u32_fine_u2200-4")'

qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_cutEvents.C("p7_hum_u1-56_u2-56_u3-57_ndl_u30_fine_u2000")'

##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_woTRG2Cut_NDLcut45_FMcut9.C("p11_hum_u1-57_u2-57_u3-57_ndl_u34_fine_u2000-TRG2bug")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_woTRG2Cut_NDLcut45_FMcut9.C("p15_hum_u1-57_u2-57_u3-57_ndl_u34_fine_u2000")'

##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_PedFitCh13Point5.C("p5_hum_u1-56_u2-56_u3-57_ndl_u32_fine_u2200-noFMsignal-TRG2highAmp")

##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_PedFitCh13.C("p1_hum_u1-56_u2-56_u3-57_ndl_u32_fine_u2200")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_PedFitCh13.C("p4_hum_u1-56_u2-56_u3-57_ndl_u34_fine_u2400")'
##qsub -shell n -b y -V -N npe_res_sipms_test -cwd root -l -b -q 'get_npe_withNDL-FMcuts_PedFitCh13("p2_hum_u1-56_u2-56_u3-57_ndl_u31_fine_u2100-2")'

