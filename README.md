# CW_1_rebuilding

### This skript allows to determine the GC-content of input reads.

### As input it takes a fastq or fasta file and the quality trashhold.

## How to use the skipt:

### use -q or --quality to set quality threshold, default is 20
### use -o or --open to select the fasta or fastq file to open

## To run the skipt open the terminal:

```
python kr1.py -o Exp2.fastq -q 0
```

## The output is hystogramm of the GC content is saved to file. 

![alt text](https://github.com/nataschkarodina/CW_1_rebuilding/blob/master/Per_sequence_GC_content.png)

##Comparing the results with the results from FASTQC:

![alt text](https://github.com/nataschkarodina/CW_1_rebuilding/blob/master/FASTQC_out.png)
