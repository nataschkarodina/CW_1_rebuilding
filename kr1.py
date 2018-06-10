from Bio import SeqIO
import matplotlib
matplotlib.use('TkAgg')
import argparse
import seaborn as sns

def getGC(f, q):
    result = []
    with open(f) as fast:
        for record in SeqIO.parse(fast, 'fastq'):
            GC = 0
            seq = str(record.seq)
            qua = record.letter_annotations['phred_quality']
            for i in range(len(qua)):
                if qua[i] >= q:
                    if seq[i] in ['G', 'C']:
                        GC += 1
            result.append(round((GC / len(seq)) * 100))
            #print(round((GC / len(seq)) * 100))
    ax = sns.distplot(result, hist=False)
    fig = ax.get_figure()
    fig.savefig('Per_sequence_GC_content.png')

#getGC('Exp2.fastq', 20)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--open', help='fasta or fastq file', type=str, required=True)
    parser.add_argument('-q', '--quality', help='set quality threshold, default is 20', type=int, default=20)
    args = parser.parse_args()
    f = args.open
    q = args.quality
    getGC(f, q)