# EndoMUST: Monocular Dpth Estimation for Robotic <ins>Endo</ins>scopy via <ins>Mu</ins>ltistage <ins>S</ins>elf-supervised <ins>T</ins>raining
Here is the pre-released code implementation for "**EndoMUST: Monocular Depth Estimation for Robotic Endoscopy via Multistage Self-supervised Training**". 

We revisit the self-supervised training strategy for endoscopy depth estimation, to jointly tackle all kinds of challenges.

:newspaper: **News:**
- [X] 🚩 Evaluation Code and Weights have been Released.
- [ ] :dart: The further work on sim-to-real is on-going.


## Table of Contents
📑 If you want to get back this section for navigation, click the [Back to ToC](#table-of-contents) at the beginning of each section.
- [Installation](#installation)
- [Prepare Datasets](#datasets)
- [Prepare Pretrained Weights](#pretrained-weights)
- [Results](assets/Results.md)
- Evaluation of [Depth Estimation](#evaluation-of-depth-estimation) and [Ego-motion + Camera Intrinsics Estimation](#evaluation-of-ego-motion-estimation-and-camera-intrinsics-prediction)
- [Acknowledgements](#acknowledgements)

## Installation
[Back to ToC](#table-of-contents)

:computer: Our implementation system: 
- Ubuntu 22.04
- NVIDIA Geforce RTX 4090 GPU (At least 24GB GPU memory)
- Pytorch 2.0.0 + CUDA 11.8

Our environment packages: in [env.yaml](env.yaml)

:heavy_exclamation_mark: (Some packages are used for implementation of existing works, e.g. `mmengine` for MonoViT used in MonoPCC and DVSMono.)

:file_folder: You also need dowloading the [pretrained Depth Anything-B model](https://huggingface.co/spaces/LiheYoung/Depth-Anything/tree/main/checkpoints) into ./pretrained_model

## Datasets
[Back to ToC](#table-of-contents)

The experiments are implemented on two main-stream **public** endoscopic datasets :file_folder: for self-supervised depth estimation and zero-shot depth estimation.
- **SCARED dataset**: Train/Validation/Evaluation [Website](https://endovissub2019-scared.grand-challenge.org/)

- **Hamlyn dataset**: Zero-shot Evaluation [Website](http://hamlyn.doc.ic.ac.uk/vision/)

_**Sincerely thanks for their great contributions to the community!!!**_

## Pretrained Weights
[Back to ToC](#table-of-contents)

The existing models pretrained on SCARED dataset :floppy_disk: can be downloaded from the following links:

**EndoDAC**: [in section **Results**](https://github.com/BeileiCui/EndoDAC?tab=readme-ov-file#results)

**MonoPCC**: [in section **Evaluation on SCARED**](https://github.com/adam99goat/MonoPCC?tab=readme-ov-file#-evaluation-on-scared)

**DVSMono**: [in **AF_training_split/README.md**](https://github.com/adam99goat/DVSMono/blob/main/AF_training_split/README.md#comparison-with-sotas-using-the-training-split-of-af-sfmlearner)

**IID-SfMLearner**: [in section **Prediction for a single image**](https://github.com/bobo909/IID-SfmLearner?tab=readme-ov-file#%EF%B8%8F-prediction-for-a-single-image) ONLY weights for depth estimation, for ego-motion estimation: [GoogleDrive](), [BaiduCloud]()

**AF-SfMLearner**: [in section **Model Zoo/End-to-End**](https://github.com/ShuweiShao/AF-SfMLearner?tab=readme-ov-file#-model-zoo)

**Depth Anything (Finetuned)**: [GoogleDrive](), [BaiduCloud]()

**Depth Anything v2 (Finetuned)**: [GoogleDrive](), [BaiduCloud]()

_**Sincerely thanks the above remarkable works for their contributions to the community!**_ :kissing_heart:

**Ours**: [GoogleDrive](), [BaiduCloud]()

**Ablations**: [GoogleDrive](), [BaiduCloud]()

## Acknowledgements
[Back to ToC](#table-of-contents)

_Sincerely thanks the following related works for their remarkable contribution to the community and their inspiration to this work!_ :kissing_heart:
- [MonoPCC](https://github.com/adam99goat/MonoPCC): Novel idea of cycle transformation constraints for training
- [DVSMono](https://github.com/adam99goat/DVSMono): Excellent idea of pose alignment-friendly dynamic view selection for training
- [EndoDAC](https://github.com/BeileiCui/EndoDAC): Innovative idea of parameter-efficient finetuning for endoscopic scenes
- [IID-SfMLearner](https://github.com/bobo909/IID-SfmLearner): Novel idea to deal with the illumination issues
- [Depth Anything](https://github.com/DepthAnything): Milestone for general depth estimation --- Move forward to [Depth Anything v2](https://github.com/DepthAnything/Depth-Anything-V2)
- [AF-SfMLearner](https://github.com/ShuweiShao/AF-SfMLearner): Milestone for depth estimation in endoscopy
