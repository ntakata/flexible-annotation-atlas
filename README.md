# Flexible annotation atlas (FAA) of the mouse brain

This repository contains Python codes for our paper ([bioRxiv](https://doi.org/10.1101/2020.02.17.953547)) __"Flexible annotation atlas of the mouse brain: combining and dividing brain structures of the Allen Brain Atlas while maintaining anatomical hierarchy"__.

## Highlihgts
- A flexible annotation atlas (FAA) for the mouse brain is proposed.
- FAA is expected to improve whole brain ROI-definition consistency among laboratories.
- The ROI can be combined or divided objectively while maintaining anatomical hierarchy by leveraging public resources of the Allen Institute for Brain Science.
- A mere two-step procedure with user-specified, text-based inforamtion and Python codes constructs FAAs with total ROI counts from 1 to more than 1,000.

## Examples of FAA
FAA consists of a JSON-formatted text file (anatomical ontology, AO) and a three-dimensional volume file of the mouse brain (annotation volume, AV). Examples of FAA are shown below: FAAsegment (total node count: 4), FAAcoarse (101), and FAAdetailed (1381). In FAAdetailed, nodes for the hippocampus and striatum were divided to two (dorsal and ventral regions) based on gene expression and fiber projection, respectively.

An icicle plot shows anatomical hierarchy of FAAdetailed with a brain structure acronym and its volume in nL. In an FAAs folder, some FAAs and an HTML file for zoomable visualization of anatomical hierarchy are available.
![FAA-example-AVs](FAAs/FAA-AVs.png)
![FAA-example-AOdetailed](FAAs/FAA-AOdetailed.gif)

## Steps to construct your annotation atlas
### 0. Preprocessing
Run `Prepare_AObaseAVbase.ipynb` to obtain preprocessed files in the data folder: a text file (AObase.json) and a volume file (AVbase.nrrd). This preprocessing eliminates _destructive_ brain structures in the original anatomical ontology file and an annotation volume of the mouse brain provided by the Allen Institute for Brain Science (AIBS).

### 1. Combining brain structures
Copy AObase.json and rename it to AObase_c.json in the data folder. Edit __AObase_c.json__ with a text editor to combine brain structures in AVbase.nrrd. Specifically, delete all contents within brackets [] of a key "children" for an inner node to combine its all descendent nodes. For example, "children": [ {"id":8, ... }, ..., {"id": 73, ..., "voxel_count": 6136}] would be "children": [] in a file AObase_c.json.

### 2. Dividing a brain structure based on gene expression and/or fiber projection.
Specify text-based information in `Divide_nodes.ipynb`: 1) IDs of brain structures ( __Target_ROI_IDs__), 2) Experimental ID ( __ExpID__) of a gene of interest, and 3) __Acronyms__ of a brain structures which are a source and a target of neuronal fiber innervation. Then, run `Divide_nodes.ipynb` to obtain your FAA, which consists of an ontology text file ( __AO_LR_remapID.json__) and an annotation volume ( __AV_LR_remapID_RAS.nii__) in the data folder.

A more detailed manual describing the step-by-step procedure is available [here](/Supplementary_Tables/table_allen_v5.2.pdf) or at Supplementary Tables 2-4 in our paper.

You can use Python scripts (Prepare_AObaseAVbase.py, Divide_nodes.py) instead of these Jupyter notebooks. For example, execute `ipython Prepare_AObaseAVbase.py` in an Anaconda Prompt.

## How to share your original FAA
There are two ways.
- Share your FAA itself (AO_LR_remapID.json and AV_LR_remapID_RAS.nii).
- Share a text-based information to reconstruct FAA. See [exampes](/FAAs/FAAdetailed/reconstruction-info/README.md) in an FAAs folder.

## Software environment
The pipeline for FAA construction was created with Python (3.7.1) using AllenSDK (version 0.16.1) written in Jupyter Notebook (5.6.0) on Anaconda (2018.12) on Windows 10 (Professional 64 bit, Microsoft). The yaml file for the anaconda environment is available in a yaml folder. [Nbparameterise](https://github.com/takluyver/nbparameterise) is also necessary.
