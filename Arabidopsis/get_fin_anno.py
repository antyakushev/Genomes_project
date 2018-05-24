### script to convert gff annotation into fin_anno txt file (like rice_anno_fin.txt)

import sys

data = open(sys.argv[1])

with open('./data/arab_anno_fin.txt', 'w') as anno:
    anno.write('"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\n'.format('MODEL', 'Chr', 'Frag', 'Start', 'Start.1', 'Strand', 'DESCRIPTION.x', 'Notes_etc', 'CHROM', 'FRAG_START', 'FRAG_STOP', 'STRAND', 'DESCRIPTION.y', 'TSS'))
    counter = 1
    for line in data.readlines():
        chrom, _, kind, start, stop, _, strand, _, name = line.strip().split('\t')
        if kind == "pseudogene" or kind == 'chromosome' or kind == "pseudogenic_transcript" or kind == "pseudogenic_exon":
            continue
        if kind == "exon" or kind == "five_prime_UTR" or kind == "CDS" or kind == "three_prime_UTR":
            model = name
            anno.write('"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\n'.format(counter, model, chrom, kind, start, stop, strand, name, "", chrom, start, stop, strand, name, start))
            counter += 1
        elif kind != "chromosome" or kind != "gene":
            model = name.split(';')[1].split('=')[1]
            anno.write('"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\t"{}"\n'.format(counter, model, chrom, kind, start, stop, strand, name, "", chrom, start, stop, strand, name, start))
            counter += 1
