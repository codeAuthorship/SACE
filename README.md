# SCAE: Can Seq2Seq Code Transformation Evade Code Authorship Attribution?

There is existing research for Code Authorship [1](https://dl.acm.org/doi/abs/10.1145/3243734.3243738) which identifies authors of source codes by employing TF-IDF.

Also, there is another existing research to evade the codeaAuthorship, which called Misleading Code Authorship by Monte Carlo Tree Search (MCTS) [2](https://www.usenix.org/conference/usenixsecurity19/presentation/quiring) (we refer this study as MAA).

In this project, we used outputs from [2](https://www.usenix.org/conference/usenixsecurity19/presentation/quiring) to train a Seq2Seq model (StructCoder) [3](https://arxiv.org/abs/2206.05239) to evade Code Authorship [1](https://dl.acm.org/doi/abs/10.1145/3243734.3243738) by employing transfer learning apporach.

## Setup the conda enviorment:
conda env scoder create -f scoder.yml

conda activate scoder

##The pre-trained checkpoint from Structcoder [3](https://arxiv.org/abs/2206.05239) that we used for our expriment is uploaded on [GoogleDrive](https://drive.google.com/file/d/1V98OciKJKftjR1ifm7elB1f3DO1UU7sp/view?usp=sharing). (You can also find it from the original work).


Download this file and save into src/saved_models/pretrain directory.

## Finetune on translation
python3 run_translation.py --do_train --do_eval --do_test --source_lang cpp --target_lang cpp --alpha1_clip -4 --alpha2_clip -4



------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------

### READ.ME below is from [StructCoder](https://github.com/reddy-lab-code-research/StructCoder).
------------------------------------------------------------------------------------------------------------------------------------
# StructCoder
Official implementation of [StructCoder: Structure-Aware Transformer for Code Generation](https://arxiv.org/abs/2206.05239)

## Setup the conda enviroment:
conda create -n structcoder --file structcoder.yml <br>
conda activate structcoder

## Download pretrained checkpoint:
mkdir -p saved_models/pretrain/checkpoint-12000 <br>
Download the pretrained model weights from [here](https://drive.google.com/drive/folders/1cyvtmZjaLc1OwlnU0_N_GwC_eAs5snf9?usp=sharing) and place it under saved_models/pretrain/checkpoint-12000/

## Finetune on translation:
python3 run_translation.py --do_train --do_eval --do_test --source_lang java --target_lang cs --max_target_length 320 --alpha1_clip -4 --alpha2_clip -4

python3 run_translation.py --do_train --do_eval --do_test --source_lang cs --target_lang java --max_target_length 256 --alpha1_clip -4 --alpha2_clip -4

## Finetune on text-to-code generation:
python3 run_generation.py --do_train --do_eval --do_test
