import subprocess

seqs = ['P00519', 'P05480', 'P12931']

for seq in seqs:
    command_line = ['blastp','-query',
                    seq + '.fasta','-out',
                    'blout','-db','nr.00']
    subprocess.call(command_line)

