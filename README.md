# SCAE: Can Seq2Seq Code Transformation Evade Code Authorship Attribution?

There is existing research for Code Authorship [1](https://dl.acm.org/doi/abs/10.1145/3243734.3243738) which identifies authors of source codes by employing TF-IDF.

Also, there is another existing research to evade the codeaAuthorship, which called Misleading Code Authorship by Monte Carlo Tree Search (MCTS) [2](https://www.usenix.org/conference/usenixsecurity19/presentation/quiring) (we refer this study as MAA).

In this project, we used outputs from [2](https://www.usenix.org/conference/usenixsecurity19/presentation/quiring) to train a Seq2Seq model (StructCoder) [3](https://arxiv.org/abs/2206.05239) to evade Code Authorship [1](https://dl.acm.org/doi/abs/10.1145/3243734.3243738) by employing transfer learning apporach.

## Setup the conda enviorment:
1. Create a virtual enviorment with requirements using conda and scoder.yml file.
- conda env scoder create -f scoder.yml
2. Activate the virtual enviorment.
- conda activate scoder

## Data prepraration:
1. Untargeted Trasnformation.
- Move training, validation, and testing files from [Untargeted_transformation](https://github.com/codeAuthorship/SCAE/tree/main/data/Untatgeted_Transformation) to [data](https://github.com/codeAuthorship/SCAE/tree/main/src/data) in src folder.
- In [data](https://github.com/codeAuthorship/SCAE/tree/main/src/data), there should be train.cpp.text_1&2.cpp, valid.cpp.text_1&2.cpp, and test.cpp.text_1&2.cpp.

2. Targeted Trasnformation.
- Move training, validation, and testing files from [Targeted_transformation](https://github.com/codeAuthorship/SCAE/tree/main/data/Targeted_Transformation) to [data](https://github.com/codeAuthorship/SCAE/tree/main/src/data) in src folder.
- In [data](https://github.com/codeAuthorship/SCAE/tree/main/src/data), there should be train.cpp.text_1&2.cpp, valid.cpp.text_1&2.cpp, and test.cpp.text_1&2.cpp.

### The names of data for Untargeted and Targeted transformation are the same. Therefore, we need to modify it to avoid conflict.

##The pre-trained checkpoint from Structcoder [3](https://arxiv.org/abs/2206.05239) that we used for our expriment is uploaded on [GoogleDrive](https://drive.google.com/file/d/1V98OciKJKftjR1ifm7elB1f3DO1UU7sp/view?usp=sharing). (You can also find it from the original work).


Download this file and save into src/saved_models/pretrain directory.

## Finetune on translation
python3 run_translation.py --do_train --do_eval --do_test --source_lang cpp --target_lang cpp --alpha1_clip -4 --alpha2_clip -4


## MAA's Targeted Attack Analysis is presented in [here](https://github.com/codeAuthorship/MAA-Targeted-Attack)
