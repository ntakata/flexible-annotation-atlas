# Information for FAA reconstruction
This FAAocd was prepared for cortico-striatal-thalamo (CST) circuitry analysis used in [Abe et al. (2020) NeuroImage "Diffusion functional MRI reveals global brain network functional abnormalities driven by targeted local activity in a neuropsychiatric disease mouse model"](https://doi.org/10.1016/j.neuroimage.2020.117318).

For FAAocd reconstruction without dividing nodes, some steps should be skipped. See Supplementary Table 4 in our paper ([bioRxiv](https://doi.org/10.1101/2020.02.17.953547)). 

## Steps
0-1

0-2

1-1 skip this step `Divide_ROI_with_gene_expression_data.ipynb`

1-2 skip this step

1-3 skip this step

1-4 skip this step

2-1 skip this step `Divide_ROI_with_fiber_innervation.ipynb`

2-2 skip this step

2-3 skip this step

2-4 skip this step

Rename following files before performing a step 3-1.
- `AObase_c.json` to `AObase_c_g_f.json`
- `AVbase_c.nrrd` to `AVbase_c_g_f.nrrd`

3-1 `Divide_left_right_AV.ipynb`

3-2

3-3

3-4

4-1

4-2 `Reassign_ID.ipynb`

4-3

5 `Transform_AllenImage_from_NRRD_toNIfTI.ipynb`
