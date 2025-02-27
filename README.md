# EndoDEER: Monocular <ins>D</ins>epth and <ins>E</ins>go-motion <ins>E</ins>stimation for <ins>E</ins>obotic <ins>Endo</ins>scopy via End-to-end Self-supervised Training with Multistage Efficient Finetuning
The pre-released code implementation for "EndoDEER: Monocular Depth and Ego-motion Estimation for Robotic Endoscopy via End-to-end Self-supervised Training with Multistage Efficient Finetuning". This work revisited the parameter-efficient finetuning for depth estiamtion in robotic endoscopy from the perspective of the training strategy.

**News:**
- [X] Evaluation Code and Weights have been Released.
- [ ] The further work on sim-to-real is on-going.

## Table of Contents
If you want to get back this section for navigation, click the [Back to ToC](#table-of-contents) at the beginning of each section.
- [Installation](#installation)
- [Prepare Datasets](#datasets)
- [Prepare Pretrained Weights](#pretrained-weights)
- Results of [Depth Estimation](#results-of-depth-estimation) and [Ego-motion + Camera Intrinsics Estimation](#results-of-ego-motion-estimation-and-camera-intrinsics-prediction)
- Evaluation of [Depth Estimation](#evaluation-of-depth-estimation) and [Ego-motion + Camera Intrinsics Estimation](#evaluation-of-ego-motion-estimation-and-camera-intrinsics-prediction)
- [Acknowledgements](#acknowledgements)

## Installation
[Back to ToC](#table-of-contents)

Our implementation system: 
- Ubuntu 22.04
- NVIDIA Geforce RTX 4090 GPU (At least 24GB GPU memory)
- Pytorch 2.0.0 + CUDA 11.8

Our environment packages: in [env.yaml](env.yaml)

You also need dowloading the [pretrained Depth Anything-B model](https://huggingface.co/spaces/LiheYoung/Depth-Anything/tree/main/checkpoints) into ./pretrained_model

## Datasets
[Back to ToC](#table-of-contents)

The experiments are implemented on two main-stream **public** endoscopic datasets for self-supervised depth estimation and zero-shot depth estimation.
- **SCARED dataset**: Train/Validation/Evaluation [Website](https://endovissub2019-scared.grand-challenge.org/)

- **Hamlyn dataset**: Zero-shot Evaluation [Website](http://hamlyn.doc.ic.ac.uk/vision/)

_**Sincerely thanks for their great contributions to the community!!!**_

## Pretrained Weights
[Back to ToC](#table-of-content)

The existing models pretrained on SCARED dataset can be downloaded from the following links:

**EndoDAC**: [in section **Results**](https://github.com/BeileiCui/EndoDAC?tab=readme-ov-file#results)

**MonoPCC**: [in section **Evaluation on SCARED**](https://github.com/adam99goat/MonoPCC?tab=readme-ov-file#-evaluation-on-scared)

**DVSMono**: [in section **Evaluation**](https://github.com/adam99goat/DVSMono/tree/main?tab=readme-ov-file#-evaluation)

**IID-SfMLearner**: [in section **Prediction for a single image**](https://github.com/bobo909/IID-SfmLearner?tab=readme-ov-file#%EF%B8%8F-prediction-for-a-single-image) ONLY weights for depth estimation

**AF-SfMLearner**: [in section **Model Zoo/End-to-End**](https://github.com/ShuweiShao/AF-SfMLearner?tab=readme-ov-file#-model-zoo)$^1$

**Depth Anything (Finetuned)**: 

**Depth Anything v2 (Finetuned)**: 

_**Sincerely thanks the above remarkable works for their contributions to the community!**_

**Ours**: 

**Ablations**:
