#!/usr/bin/bash
for x in {1..40}
do

	read a b c d e f g h i j k l m n o p q r s t u < <(awk "NR==$x {print}" pt800.txt)

	for z in $b $c $d $e $f $g $h $i $j $k $l $m $n $o $p $q $r $s $t $u

	do
		/home/avinashverma/backup/HELIOS-K/heliosk -P $a -T $z -name $a-$z

	done
done
