#!bin/bash

rm $output
rm hitrate-vs-data-dt1.csv hitrate-vs-data-dt2.csv hitrate-vs-data-dt3.csv hitrate-vs-data-dt4.csv

filenames=("hitrate-vs-data-dt1.csv" "hitrate-vs-data-dt2.csv" "hitrate-vs-data-dt3.csv" "hitrate-vs-data-dt4.csv")
clf="hybrid"
datatypes=(1 2 3 4)
pruned=1

dataamount=(0.01 0.02 0.03 0.04 0.08 0.16 0.32 0.64 1) # difficult to loop through decimal values...

for d in ${dataamount[*]}
do
	python makeVocabulary.py $d
	for datatype in ${datatypes[*]}
	do
		output=${filenames[$(($datatype - 1))]}
		python hitratevsdata.py $clf $datatype $pruned $d >> $output
	done
done

