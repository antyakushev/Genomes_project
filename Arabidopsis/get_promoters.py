### script to get promoter intervals(-+500 nucleotides of tss) in .bed format

import sys

data = open(sys.argv[1])

with open('./data/promoters_arab.bed', 'w') as tss:
    with open('./data/Promoters_final_arab.txt', 'w') as promoters:
        promoters.write("{}\t{}\t{}\t{}\n".format("CHROM", "MODEL", "TSS", "STRAND"))
        for line in data.readlines():
            chrom, start, stop, strand, description, model = line.strip().split('\t')
            if strand == "+":
                prom_start = int(start)-500
                prom_end = int(start)+500
                tss.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(chrom, prom_start, prom_end, description, model, strand))
                promoters.write("{}\t{}\t{}\t{}\n".format(chrom, model, start, strand))
            elif strand == "-":
                prom_start = int(stop)-500
                prom_end = int(stop)+500
                tss.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(chrom, prom_start, prom_end, description, model, strand))
                promoters.write("{}\t{}\t{}\t{}\n".format(chrom, model, stop, strand))
