import numpy as np
import cPickle as pickle
import chumpy as ch
import cv2 as cv
import google.protobuf

np.set_printoptions(threshold=np.inf)

def backwards_compatibility_replacements(dd):

    # replacements
    if 'default_v' in dd:
        dd['v_template'] = dd['default_v']
        del dd['default_v']
        #print dd['v_template']
    if 'template_v' in dd:
        dd['v_template'] = dd['template_v']
        del dd['template_v']
    if 'joint_regressor' in dd:
        dd['J_regressor'] = dd['joint_regressor']
        del dd['joint_regressor']
    if 'blendshapes' in dd:
        dd['posedirs'] = dd['blendshapes']
        del dd['blendshapes']
    if 'J' not in dd:
        dd['J'] = dd['joints']
        del dd['joints']

    # defaults
    if 'bs_style' not in dd:
        dd['bs_style'] = 'lbs'

def ready_arguments(fname_or_dict):

    if not isinstance(fname_or_dict, dict):
        dd = pickle.load(open(fname_or_dict))
    else:
        dd = fname_or_dict
        
    backwards_compatibility_replacements(dd)
            
    return dd

data = ready_arguments('basicModel_f_lbs_10_207_0_v1.0.0.pkl')  



bs_style = 'lbs'
bs_type = 'lrotmin'

shapedirs = data['shapedirs']

for i in data.keys():
    print str(i) + '\t' + str(type(data[i]))

data['f'] = data['f'].astype(np.float64)

data['kintree_table'] = data['kintree_table'].astype(np.float64)

#print data['kintree_table'].shape

#print data['shapedirs'].shape

shape = np.array(data['shapedirs'])

print data['kintree_table']

# fs_write = cv.FileStorage('data.yml', cv.FILE_STORAGE_WRITE)
# fs_write.write('J_regressor_prior', data['J_regressor_prior'].toarray())
# print data['J_regressor_prior'].shape
# fs_write.write('f', data['f'])
# print data['f'].shape
# fs_write.write('J_regressor', data['J_regressor'].toarray())
# print data['J_regressor'].shape
# fs_write.write('kintree_table', data['kintree_table'])
# print data['kintree_table'].shape
# fs_write.write('J', data['J'])
# print data['J'].shape
# fs_write.write('weights_prior', data['weights_prior'])
# print data['weights_prior'].shape
# fs_write.write('weights', data['weights'])
# print data['weights'].shape
# fs_write.write('vert_sym_idxs', data['vert_sym_idxs'])
# print data['vert_sym_idxs'].shape
# fs_write.write('posedirs', data['posedirs'])
# print data['posedirs'].shape
# fs_write.write('v_template', data['v_template'])
# print data['v_template'].shape
# shape.reshape(-1, shape.shape[2])
# fs_write.write('shape', shape)
# print shape.shape
# fs_write.release()