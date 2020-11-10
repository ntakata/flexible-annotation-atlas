#!/usr/bin/env python
# coding: utf-8

# This code divides leaf nodes based on gene expression and fiber projection. Five additional modifications are performed. 

# # Set variables

# In[1]:


dir_notebooks = 'notebooks'

# user-specified information
gene_ExpID = 74881161 # Wfs1 is highly expressed in CA1 of the dorsal hippocampus
gene_TargetROIID = 382 # 382 is hippocampal CA1

fiber_TargetROIID = 672 # Caudoputamen
fiber_Fiber_from = 'AI'
fiber_Fiber_to = 'CP'


# In[2]:


import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import sys
import os
from nbparameterise import(extract_parameters, replace_definitions, parameter_values)

path_datafolder = os.path.join(os.getcwd(), 'data')
path_figfolder = os.path.join(os.getcwd(), 'figs')
path_genefolder = os.path.join(os.getcwd(), 'gene_data', str(gene_ExpID)) + '\\'
path_fiberfolder = os.path.join(os.getcwd(), 'fiber_data\\From_'+str(fiber_Fiber_from)+                               '_To_'+str(fiber_Fiber_to)) + '\\'


# # (continued) Combine nodes 

# ## Get_ID_parentID_pairs

# In[3]:


with open(os.path.join(dir_notebooks,'Get_ID_parentID_pairs.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AO='AObase.json',                          fn_output_csv='ID_parentID_AObase.csv')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Replace_ID_with_its_parent_ID_to_reflect_combined_AO

# In[4]:


with open(os.path.join(dir_notebooks,'Replace_ID_with_its_parent_ID_to_reflect_combined_AO.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV='AVbase.nrrd',                          fn_input_AO='AObase_c.json',                          fn_input_csv='ID_parentID_AObase.csv',                          fn_output_AV='AVbase_c.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# # Divide ROI with gene expression data

# ## Divide_ROI_with_gene_expression_data

# In[5]:


with open(os.path.join(dir_notebooks,'Divide_ROI_with_gene_expression_data.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          ExpID=gene_ExpID,                          Target_ROI_ID=gene_TargetROIID,                          dir_data=path_datafolder,                          dir_fig=path_figfolder,                          dir_gene=path_genefolder,                          fn_input_AV='AVbase_c.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Update_AV_according_to_gene_expression

# In[6]:


with open(os.path.join(dir_notebooks,'Update_AV_according_to_gene_expression.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          ExpID=gene_ExpID,                          Target_ROI_ID=gene_TargetROIID,                          dir_data=path_datafolder,                          dir_fig=path_figfolder,                          dir_gene=path_genefolder,                          fn_input_AV_gene='AV_target_ROI_ID_'+str(gene_TargetROIID)+                          '_gene_'+str(gene_ExpID)+'.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Update_AO_according_to_gene_expression

# In[7]:


with open(os.path.join(dir_notebooks,'Update_AO_according_to_gene_expression.ipynb'),         encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          ExpID=gene_ExpID,                          Target_ROI_ID=gene_TargetROIID,                          dir_data=path_datafolder)
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Add_VC_to_AO

# In[8]:


with open(os.path.join(dir_notebooks,'Add_VC_to_AO.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV='AVbase_c_g.nrrd',                          fn_input_AO='AObase_c_g_woVC.json',                          fn_output_AO='AObase_c_g.json')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# # Divide ROI with fiber innervation data

# ## Divide_ROI_with_fiber_innervation

# In[9]:


with open(os.path.join(dir_notebooks,'Divide_ROI_with_fiber_innervation.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          Target_ROI_ID=fiber_TargetROIID,                          Fiber_from=fiber_Fiber_from,                          Fiber_to=fiber_Fiber_to,                          dir_data=path_datafolder,                          dir_fig=path_figfolder,                          dir_fiber=path_fiberfolder,                          fn_input_AV='AVbase_c_g.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Update_AV_according_to_fiber_innervation

# In[10]:


with open(os.path.join(dir_notebooks,'Update_AV_according_to_fiber_innervation.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          Target_ROI_ID=fiber_TargetROIID,                          Fiber_from=fiber_Fiber_from,                          Fiber_to=fiber_Fiber_to,                          dir_data=path_datafolder,                          dir_fig=path_figfolder,                          dir_fiber=path_fiberfolder,                          fn_input_AV_ori='AVbase_c_g.nrrd',                          fn_input_AV_fiber='AV_target_ROI_ID_'+str(fiber_TargetROIID)+                          '_fiber_from_'+fiber_Fiber_from+'_to_'+fiber_Fiber_to+'.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Update_AO_according_to_fiber_innervation

# In[11]:


with open(os.path.join(dir_notebooks,'Update_AO_according_to_fiber_innervation.ipynb'),         encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          Target_ROI_ID=fiber_TargetROIID,                          Fiber_from=fiber_Fiber_from,                          Fiber_to=fiber_Fiber_to,                          dir_data=path_datafolder)

new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Add_VC_to_AO

# In[12]:


with open(os.path.join(dir_notebooks,'Add_VC_to_AO.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV='AVbase_c_g_f.nrrd',                          fn_input_AO='AObase_c_g_f_woVC.json',                          fn_output_AO='AObase_c_g_f.json')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# # Make ROI-IDs different in right and left side of the brain

# ## Divide_left_right_AV

# In[5]:


with open(os.path.join(dir_notebooks,'Divide_left_right_AV.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV_ori='AVbase_c_g_f.nrrd',                          fn_output_AV_update='AVbase_c_g_f_LR.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Prepare_AO_LR

# In[6]:


with open(os.path.join(dir_notebooks,'Prepare_AO_LR.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AO='AObase_c_g_f.json')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Merge json files (AO_L and AO_R)

# In[8]:


with open(os.path.join(dir_notebooks, 'Merge_AO_LR.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)

orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                         dir_data=path_datafolder,                         fn_input_AOL='AO_L.json',                         fn_input_AOR='AO_R.json',                         fn_input_template='AO_LR_wo_VC_TEMPLATE.json',                         fn_output_AO='AO_LR_wo_VC.json')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Add_VC_to_AO

# In[12]:


with open(os.path.join(dir_notebooks,'Add_VC_to_AO.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV='AVbase_c_g_f_LR.nrrd',                          fn_input_AO='AO_LR_wo_VC.json',                          fn_output_AO='AO_LR.json')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# # Reassign ID

# ## Get_ID_parentID_pairs

# In[13]:


with open(os.path.join(dir_notebooks,'Get_ID_parentID_pairs.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AO='AO_LR.json',                          fn_output_csv='ID_parentID_LR.csv')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Reassign IDs in AO json file

# In[ ]:


with open(os.path.join(dir_notebooks,'Reassign_ID.ipynb'), encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AO='AO_LR.json',                          fn_output_AO='AO_LR_remapID.json',                          fn_output_csv='remapIDpairs.csv')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# ## Update_ID_in_AV_to_reflect_reassignedID

# In[ ]:


with open(os.path.join(dir_notebooks,'Update_ID_in_AV_to_reflect_reassignedID.ipynb'),          encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input_AV='AVbase_c_g_f_LR.nrrd',                          fn_input_ID='remapIDpairs.csv',                          fn_output_AV='AV_LR_remapID.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})


# # Transform AllenImage from NRRD to NIfTI

# In[ ]:


with open(os.path.join(dir_notebooks,'Transform_AllenImage_from_NRRD_to_NIfTI.ipynb')) as f:
    nb = nbformat.read(f, as_version=4)
    
orig_parameters = extract_parameters(nb)
params = parameter_values(orig_parameters,                          dir_data=path_datafolder,                          fn_input='AV_LR_remapID.nrrd')
new_nb = replace_definitions(nb, params)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(new_nb, {'metadata':{'path':'./notebooks'}})

