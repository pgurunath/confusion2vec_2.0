# Confusion2Vec 2.0
This repository contains the source code and data used for training Confusion2Vec 2.0 word vector representation models. We also make the pre-trained embeddings.

The source code is an augmented version of the [fastText](https://fasttext.cc/) library from Facebook. Documentation of the origin source code can be accessed at their [website](https://fasttext.cc) or their [GitHub](https://github.com/facebookresearch/fastText) page.

## Installation
### Requirements
 
* (g++-4.7.2 or newer) or (clang-3.3 or newer)
* make
* cmake 2.8.9 or newer (optional)

### Building using make

```
$ wget https://github.com/pgurunath/confusion2vec_2.0/archive/main.zip
$ unzip main.zip
$ cd confusion2vec_2.0
$ make
```

This will produce object files for all the classes as well as the main binary `fasttext`.

### Building fastText using cmake

```
$ git clone https://github.com/pgurunath/confusion2vec_2.0.git
$ cd confusion2vec_2.0
$ mkdir build && cd build && cmake ..
$ make && make install
```

This will create the binary and also all relevant libraries (shared, static, PIC).

## Example use cases
All the use cases and functionality of fastText are supported and they can be referred [here](https://github.com/facebookresearch/fastText). We only provide descriptions of the augmented functionality of the software towards estimating the confusion2vec 2.0 models.

### Inter-Confusion Model
Without Pre-training / Initialization
```
$ ./fasttext c2v-inter -t 0.001 -neg 64 -ws 5 -epoch 5 -input sausage.txt -output inter-confusion -thread 32 -dim 300 -lr 0.01
```

With Pre-training / Initialization on fastText skip-gram model trained on [Wikipedia](https://fasttext.cc/docs/en/pretrained-vectors.html).
```
$ ./fasttext c2v-inter -t 0.001 -neg 64 -ws 5 -epoch 5 -input sausage.txt -output inter-confusion-pre-wiki -thread 32 -dim 300 -lr 0.01 -inputModel wiki.en.bin -incr
```

### Intra-Confusion Model
Without Pre-training / Initialization
```
$ ./fasttext c2v-intra -t 0.001 -neg 64 -ws 5 -epoch 5 -input sausage.txt -output intra-confusion -thread 32 -dim 300 -lr 0.01
```

With Pre-training / Initialization on fastText skip-gram model trained on [Wikipedia](https://fasttext.cc/docs/en/pretrained-vectors.html).
```
$ ./fasttext c2v-intra -t 0.001 -neg 64 -ws 5 -epoch 5 -input sausage.txt -output intra-confusion-pre-wiki -thread 32 -dim 300 -lr 0.01 -inputModel wiki.en.bin -incr
```

### Top-Confusion Model
Without Pre-training / Initialization
```
$ ./fasttext c2v-top -t 0.001 -neg 64 -ws 5 -epoch 5 -input sausage.txt -output top-confusion -thread 32 -dim 300 -lr 0.01
```

With Pre-training / Initialization on fastText skip-gram model trained on [Wikipedia](https://fasttext.cc/docs/en/pretrained-vectors.html).
```
$ ./fasttext c2v-top -t 0.001 -neg 64 -ws 5 -epoch 5 -input sausage.txt -output top-confusion-pre-wiki -thread 32 -dim 300 -lr 0.01 -inputModel wiki.en.bin -incr
```

### Hybrid Inter-Intra Confusion Model 
Without Pre-training / Initialization
```
$ ./fasttext c2v-hybrid -t 0.001 -neg 64 -ws 5 -epoch 5 -input sausage.txt -output hybrid-confusion -thread 32 -dim 300 -lr 0.01
```

With Pre-training / Initialization on fastText skip-gram model trained on [Wikipedia](https://fasttext.cc/docs/en/pretrained-vectors.html).
```
$ ./fasttext c2v-hybrid -t 0.001 -neg 64 -ws 5 -epoch 5 -input sausage.txt -output hybrid-confusion-pre-wiki -thread 32 -dim 300 -lr 0.01 -inputModel wiki.en.bin -incr
```

## Supplementary Scripts
### Data Preparation
Converting Kaldi Sausage format to compatible text format for training confusion2vec models
```
python scripts/convert_sausage.py exp/chain/decode/sausage.lat.txt data/lang/words.txt sausage.txt
```

## References
If you use this code please cite:
Prashanth Gurunath Shivakumar, Panayiotis Georgiou, Shrikanth Narayanan, *Confusion2Vec 2.0: Enriching Ambiguous Spoken Language Representations with Subwords*

### Contact
* E-mail: [pgurunat@usc.edu](mailto:pgurunat@usc.edu)
