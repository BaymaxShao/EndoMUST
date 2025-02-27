## Results of Depth Estimation
[Back to ToC](#table-of-contents)

:pushpin: Note that:
1. 'CI': `Pred.` denotes that **Camera Intrinsics** are **Predicted**.
2. 'TP': Number of **Trainable Parameters** in the depth map generation network.
3. *: Results form the **public provided weights**.
4. \^: Model **finetuned** on SCARED dataset.
5. **Inference speed** will be varied with hardware, e.g. 17.7ms on NVIDIA 3090 but 5.7ms on NVIDIA 4090 for EndoDAC.
### :clipboard: SCARED dataset
|Methods|From|CI|Abs Rel|Sq Rel|RMSE|RMSE Log|$\delta$|TP/M|Speed/ms|
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|AF-SfMLearner|**MedIA'22**|Given|0.059|0.435|4.925|0.082|0.974|14.8|2.0|
|Yang et al.|**TMI'24**|Given|0.062|0.558|5.585|0.090|0.962|2.0|8.0|
|Depth Anything\^|**CVPR'24**|Given|0.055|0.410|4.769|0.078|0.973|13.0|5.0|
|Depth Anything v2\^|**NeurIPS'24**|Given|0.076|0.683|6.379|0.104|0.949|13.0|5.0|
|IID-SfMLearner|**JBHI'24**|Given|0.057|0.430|4.822|0.079|0.972|14.8|2.0|
|DVSMono|**BIBM'24**|Given|0.055|0.410|4.797|0.078|0.975|27.0|12.7|
|MonoPCC|**arXiv'24**|Given|0.051|0.349|4.488|0.072|0.983|27.0|12.7|
|EndoDAC|**MICCAI'24**|Pred.|0.052|0.362|4.464|0.072|0.979|1.6|5.7|
|**EndoDEER**|**Ours**|**Pred.**|**0.046**|**0.313**|4.276|**0.067**|**0.984**|1.8|6.2|

### :clipboard: Hamlyn dataset (Zero-shot)
|Methods|From|CI|Abs Rel|Sq Rel|RMSE|RMSE Log|$\delta$|TP/M|Speed/ms|
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|Endo Depth & Motion|**RA-L'21**|Given|0.185|5.424|16.100|0.225|0.732|-|~15|
|AF-SfMLearner|**MedIA'22**|Given|0.168|4.440|13.870|0.204|0.770|14.8|1.0|
|Depth Anything\^|**CVPR'24**|Given|0.154|3.616|12.733|0.189|0.784|13.0|3.0|
|Depth Anything v2\^|**NeurIPS'24**|Given|0.182|4.994|15.067|0.219|0.740|13.0|3.0|
|IID-SfMLearner*|**JBHI'24**|Given|0.171|4.526|14.066|0.206|0.767|14.8|1.0|
|DVSMono*|**BIBM'24**|Given|0.152|3.566|12.643|0.187|0.791|27.0|10.5|
|MonoPCC*|**arXiv'24**|Given|0.158|3.889|13.205|0.194|0.782|27.0|10.5|
|EndoDAC|**MICCAI'24**|Pred.|0.156|3.854|12.936|0.193|0.791|1.6|4.0|
|**EndoDEER**|**Ours**|**Pred.**|**0.145**|**3.382**|**12.100**|**0.180**|**0.807**|1.8|4.5|

### :eyes: Qualitative Results of Depth Estimation
![](assets/vis_depth.png)

## Results of Ego-motion estimation and Camera Intrinsics Prediction
[Back to ToC](#table-of-contents)
### :clipboard: Quantitative Results of Ego-motion Estimation
The results are calculated by Absolute Translation Error(ATE). **The best results** are in bold, while <ins>the second best results</ins> are underlined.
|Methods|From|CI|Seq. 1|Seq. 2|Seq. 3|
|:---|:---|:---:|:---:|:---:|:---:|
|AF-SfMLearner|**MedIA'22**|Given|<ins>0.0941</ins>|0.0742|0.0596|
|IID-SfMLearner|**JBHI'24**|Given|0.1040|0.0781|0.0614|
|MonoPCC|**arXiv'24**|Given|0.0951|0.0764|0.0666|
|EndoDAC|**MICCAI'24**|Pred.|0.0936|0.0776|0.0588|
|**EndoDEER**|**Ours**|**Pred.**|**0.0933**|<ins>0.0750</ins>|**0.0586**|

### :eyes: Qualitative Results of Ego-motion Estimation
![](assets/vis_traj.png)

### :clipboard: Quantitative Results of Camera Intrinsics Estimation
The results are displayed as `value(relative error)`
|Methods|fx|fy|cx|cy|
|:---|:---:|:---:|:---:|:---:|
|GT|0.8200|1.0200|0.5000|0.5000|
|EndoDAC*|0.8610(5.00%)|1.0778(5.67%)|0.4917(1.66%)|0.5101(2.02%)|
|**EndoDEER**|0.8158(**0.51%**)|1.0232(**0.31%**)|0.4949(**1.02%**)|0.4951(**0.98%**)|
