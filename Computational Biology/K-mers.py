def kmer(seq, k):
    kmers = set()
    for i in range(len(seq)-k):
        kmers.add(seq[i:i+k])
    return kmers


if __name__ == "__main__":
    with open("test.FASTA", 'r', encoding='utf-8') as f:
        data = f.readlines()
        seq = data[1].replace("\n", "")
    print(seq)
    print(kmer(seq, 3))