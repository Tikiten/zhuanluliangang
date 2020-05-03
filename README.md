# zhuanluliangang
There are two version of this project :offline and online. The offline version trains model based on dataset which contains a lot of 10-second video. The online version preprocesses a 10-minute video, then use the model which pre-trained in the offline version to detect. The output is a txt which contains detections results every few seconds.

This repository contains the source code for the paper.
```@inproceedings{hara3dcnns,
  author={Kensho Hara and Hirokatsu Kataoka and Yutaka Satoh},
  title={Can Spatiotemporal 3D CNNs Retrace the History of 2D CNNs and ImageNet?},
  booktitle={Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  pages={6546--6555},
  year={2018},
}```
