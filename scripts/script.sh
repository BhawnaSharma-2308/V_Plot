zcat mapped.bed.gz | awk '{ y = (1000 / ($4 - $3)) * (($9 + $10) / 2 - $3) - 500; print int(y) "\t" $12}' > output.txt
cat output.txt | awk -F, '{ freq[$1 "\t" $2]++ } END { for (key in freq) print key,freq[key] }' > final_frequency.tsv
