#!bin/bash
#output="hitrate-vs-chi2.csv"

#rm $output
filenames=("hitrate-vs-chi2-dt1.csv" "hitrate-vs-chi2-dt2.csv" "hitrate-vs-chi2-dt3.csv" "hitrate-vs-chi2-dt4.csv")
clf="hybrid"
datatypes=(1 2 3 4)
pruned=1
chi2end=100

prechi=(0.25 0.5 0.75) # difficult to loop through decimal values...

for datatype in ${datatypes[*]}
do

	output=${filenames[$(($datatype - 1))]}
	
	rm $output
	
	for chi in ${prechi[*]}
	do
		python hitratevschi2.py $clf $datatype $pruned $chi >> $output
		#echo $chi >> $output
	done

	for (( chi=1; chi<=$chi2end; chi*=2 ))
	do
		python hitratevschi2.py $clf $datatype $pruned $chi >> $output
		#echo $chi >> $output
	done
	python hitratevschi2.py $clf $datatype $pruned $chi2end >> $output

done

