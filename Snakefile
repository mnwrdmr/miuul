rule all:
    input:
        'resource/G_intestinalis.fasta'

rule create_output:
    output:
        'output/output_file.txt'
    shell:
        'python create_output.py {input} > {output}'