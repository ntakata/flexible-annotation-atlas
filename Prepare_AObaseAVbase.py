#!/usr/bin/env python
# coding: utf-8

# This code prepares AObase.json and AVbase.nrrd using online resources at AIBS (annotation_100.nrrd and 1.json; Put these in the data folder).

# # Set variables

# In[7]:


import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import sys
import os
from nbparameterise import(extract_parameters, replace_definitions, parameter_values)

path_datafolder = os.path.join(os.getcwd(), 'data')
dir_notebooks = 'notebooks'


# # Prepare anatomical ontology(AO)_base

# ## Add_VC_to_AO
# VC: voxel count, AO: annotation ontoloy

# In[8]:


with open(os.path.join(dir_notebooks,'Add_VC_to_AO.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV='annotation_100.nrrd',                          fn_input_AO='1.json',                          fn_output_AO='1_VC.json')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Prune_leaf_ROI_wo_VC_in_AO

# In[9]:


with open(os.path.join(dir_notebooks,'Prune_leaf_ROI_wo_VC_in_AO.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)

orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters, dir_data=path_datafolder)
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Divide_internal_ROI_with_VC_in_AO

# In[10]:


with open(os.path.join(dir_notebooks,'Divide_internal_ROI_with_VC_in_AO.ipynb'),                      encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters, dir_data=path_datafolder)
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Update_ID_in_AV_to_reflect_divided_AO

# In[11]:


with open(os.path.join(dir_notebooks,'Update_ID_in_AV_to_reflect_divided_AO.ipynb'),                      encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV = 'annotation_100.nrrd',                          fn_input_ID = 'dividedIDs.csv',                          fn_output_AV = 'AVbase.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Add_VC_to_AO

# In[12]:


with open(os.path.join(dir_notebooks,'Add_VC_to_AO.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV='AVbase.nrrd',                          fn_input_AO='1_VC_pruned_divided.json',                          fn_output_AO='AObase.json')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})

