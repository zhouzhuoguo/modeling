from HW_Settings_diffusion import *

# ######################################
# @ DIFFUSION
# ######################################

# """
TASK = "DIFFUSION"
CATE = "diffusion"
NN_NUM_STG      = 244
NN_FPS_ENA      = [False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False
                   

                   ]
NN_KNN_ENA      = [False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False
                   

                   ]
NN_POL_ENA      = [False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   True,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   True,
                   False,
                   False,
                   False,
                   False

                   ]

NN_NUM_CNV          = [2,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       6,
                       2,
                       1,
                       1,
                       1,
                       2,
                       2,
                       1,
                       2,
                       2,
                       1,
                       2,
                       2,
                       1,
                       2,
                       2,
                       2,
                       1,
                       6,
                       2,
                       1,
                       1,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       2,
                       2,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       2,
                       2,
                       1,
                       7,
                       6,
                       2,
                       2,
                       1,
                       1,
                       1,
                       1,
                       2,
                       7,
                       2,
                       2,
                       2,
                       2,
                       1,
                       2,
                       2,
                       2,
                       1,
                       2,
                       2,
                       2,
                       1,
                       2,
                       2,
                       2,
                       1

                       ]
NN_NUM_INPNT_STG    = [77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       262144,
                       262144,
                       262144,
                       262144,
                       65536,
                       65536,
                       65536,
                       16384,
                       16384,
                       16384,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       16384,
                       16384,
                       16384,
                       16384,
                       65536,
                       65536,
                       65536,
                       65536,
                       262144,
                       262144,
                       262144,
                       262144                      
                       ]
NN_NUM_OUTPNT_STG   = [77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       262144,
                       262144,
                       262144,
                       262144,
                       65536,
                       65536,
                       65536,
                       16384,
                       16384,
                       16384,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       16384,
                       16384,
                       16384,
                       16384,
                       65536,
                       65536,
                       65536,
                       65536,
                       262144,
                       262144,
                       262144,
                       262144  




                       ]

NN_NUM_OUTPNT_STG_POL=[77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       77,
                       262144,
                       262144,
                       262144,
                       65536,
                       65536,
                       65536,
                       16384,
                       16384,
                       16384,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       64,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       256,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       1024,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       4096,
                       16384,
                       16384,
                       16384,
                       16384,
                       65536,
                       65536,
                       65536,
                       65536,
                       262144,
                       262144,
                       262144,
                       262144,
                       262144  
                       ]

NN_ARCH         = [[{"CNC": False, "RES": False, "ITP": False, "MTN": False, "SRC": True,  "IN0": 0,      "IN1": 0,     "OUT":[[0, 1]]     }, # CLIPTextEmbeding token_embeding
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[1, 0], [1, 1], [1, 3]]     }], # CLIPTextEmbeding position_embeding


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[1, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[1, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[1, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [1, 5], "IN1": [0, 1],     "OUT":[[2, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[2, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [2, 1], "IN1": [1, 5],     "OUT":[[3, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[4, 0], [4, 1], [4, 3]]    }], # fake conv CLIPEncoder1_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[4, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[4, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[4, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [4, 5], "IN1": [3, 0],     "OUT":[[5, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[5, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [5, 1], "IN1": [4, 5],     "OUT":[[6, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[7, 0], [7, 1], [7, 3]]    }], # fake conv CLIPEncoder2_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[7, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[7, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[7, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [7, 5], "IN1": [6, 0],     "OUT":[[8, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[8, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [8, 1], "IN1": [7, 5],     "OUT":[[9, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[10, 0], [10, 1], [10, 3]]    }], # fake conv CLIPEncoder3_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[10, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[10, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[10, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [10, 5], "IN1": [9, 0],     "OUT":[[11, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[11, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [11, 1], "IN1": [10, 5],     "OUT":[[12, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[13, 0], [13, 1], [13, 3]]    }], # fake conv CLIPEncoder4_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[13, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[13, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[13, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [13, 5], "IN1": [12, 0],     "OUT":[[14, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[14, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [14, 1], "IN1": [13, 5],     "OUT":[[15, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[16, 0], [16, 1], [16, 3]]    }], # fake conv CLIPEncoder5_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[16, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0   }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[16, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[16, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [16, 5], "IN1": [15, 0],     "OUT":[[17, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[17, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [17, 1], "IN1": [16, 5],     "OUT":[[18, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[19, 0], [19, 1], [19, 3]]    }], # fake conv CLIPEncoder6_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[19, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0   }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[19, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[19, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [19, 5], "IN1": [18, 0],     "OUT":[[20, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[20, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [20, 1], "IN1": [19, 5],     "OUT":[[21, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[22, 0], [22, 1], [22, 3]]    }], # fake conv CLIPEncoder7_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[22, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0   }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[22, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[22, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [22, 5], "IN1": [21, 0],     "OUT":[[23, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[23, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [23, 1], "IN1": [22, 5],     "OUT":[[24, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[25, 0], [25, 1], [25, 3]]    }], # fake conv CLIPEncoder8_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[25, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0   }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[25, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[25, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [25, 5], "IN1": [24, 0],     "OUT":[[26, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[26, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [26, 1], "IN1": [25, 5],     "OUT":[[27, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[28, 0], [28, 1], [28, 3]]    }], # fake conv CLIPEncoder9_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[28, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0   }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[28, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[28, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [28, 5], "IN1": [27, 0],     "OUT":[[29, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[29, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [29, 1], "IN1": [28, 5],     "OUT":[[30, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[31, 0], [31, 1], [31, 3]]    }], # fake conv CLIPEncoder10_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[31, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0   }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[31, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[31, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [31, 5], "IN1": [30, 0],     "OUT":[[32, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[32, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [32, 1], "IN1": [31, 5],     "OUT":[[33, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[34, 0], [34, 1], [34, 3]]    }], # fake conv CLIPEncoder11_end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0    }, # linear_wq
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[34, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":0   }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[34, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[34, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [34, 5], "IN1": [33, 0],     "OUT":[[35, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[35, 1]] }, # fake conv to isolate consecutive "RES"
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [35, 1], "IN1": [34, 5],     "OUT":[[36, 0]]    }], # MLP


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[37, 0]]   }], # fake conv CLIPEncoder12_end


                
                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[62, 1], [62, 2], [70, 1], [70, 2], [79, 1], [79, 2], [87, 1], [87, 2], [96, 1], [96, 2], [104, 1], [104, 2], [119, 1], [119, 2], [144, 1], [144, 2], [153, 1], [153, 2], [162, 1], [162, 2], [172, 1], [172, 2], [181, 1], [181, 2], [190, 1], [190, 2], [200, 1], [200, 2], [209, 1], [209, 2], [218, 1], [218, 2], ]    }], # CLIP end


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False, "SRC": True,   "IN0": 0,      "IN1": 0,     "OUT":[[39, 0]]     }], # VAE encoder begin
                   

                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[39, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [39, 1],      "IN1": [38, 0],     "OUT":[[40, 0]]     }], # RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[40, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [40, 1],      "IN1": [39, 1],     "OUT":[[41, 0]]    }],# RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[42, 0]]     }], # downsample


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[42, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [42, 1],      "IN1": [41, 0],     "OUT":[[43, 0]]    }], # RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[43, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [43, 1],      "IN1": [42, 1],     "OUT":[[44, 0]]     }], # RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[45, 0]]     }], # downsample


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[45, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [45, 1],      "IN1": [44, 0],     "OUT":[[46, 0]]    }], # RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[46, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [46, 1],      "IN1": [45, 1],     "OUT":[[47, 0]]     }], # RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[48, 0]]    }], # downsample


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[48, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [48, 1],      "IN1": [47, 0],     "OUT":[[49, 0]]    }], # RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[49, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [49, 1],      "IN1": [48, 1],     "OUT":[[50, 0]]     }], # RESNETBIK

                   
                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[50, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [50, 1],      "IN1": [49, 1],     "OUT":[[51, 0]]     }], # UnetMidBlock RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[52, 0], [52, 1], [52, 3]]     }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[52, 2]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[52, 4]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[52, 5]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [52, 5], "IN1": [51, 0],     "OUT":[[53, 0]]    }], # linear_wo UnetMidBlock Selfattention


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[53, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [53, 1],      "IN1": [53, 0],     "OUT":[[54, 0]]     }], # UnetMidBlock RESNETBIK


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[55, 0]]     }], # conv3x3


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[56, 0]]     }], # conv1x1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[57, 0]]     }], # 重参数化 (encoder结束，准备接UNET)


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[58, 0]]     }], # UNET部分
    

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[58, 1]]     },# 第一个ResBLK  
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [58, 1], "IN1": [58, 0],     "OUT":[[59, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[59, 1]]     }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [59, 1], "IN1": [57, 0],     "OUT":[[60, 0]]    }], # 考虑time embedding的RES后的Conv3x3


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[61, 0]]    }], # RESNetBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[61, 1], [61, 2], [61, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[61, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[61, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[61, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [61, 6], "IN1": [61, 0],     "OUT":[[62, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[62, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[62, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[62, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [62, 5], "IN1": [61, 6],     "OUT":[[63, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[63, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [63, 1], "IN1": [62, 5],     "OUT":[[64, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[64, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [64, 1], "IN1": [60, 0],     "OUT":[[65, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[66, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[66, 1]]     },# 第二个ResBLK  
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [66, 1], "IN1": [66, 0],     "OUT":[[67, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[67, 1]]    },
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [67, 1], "IN1": [65, 0],     "OUT":[[68, 0]]    }], # 考虑time embedding的RES后的Conv3x3


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[69, 0]]    }], # RESNetBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[69, 1], [69, 2], [69, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[69, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[69, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[69, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [69, 6], "IN1": [69, 0],     "OUT":[[70, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[70, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[70, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[70, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [70, 5], "IN1": [69, 6],     "OUT":[[71, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[71, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [71, 1], "IN1": [70, 5],     "OUT":[[72, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[72, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [72, 1], "IN1": [68, 0],     "OUT":[[73, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[74, 0]]    }], # Transformer后的伪卷积

                    
                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,     "IN1": 0,     "OUT":[[75, 0]]     }], # Downsample3x3卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[75, 1]]   },# 第二个Crossattndown的第一个ResBLK的第一个卷积操作
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [75, 1], "IN1": [75, 0],     "OUT":[[76, 0]]     }],# time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[76, 1]]     }, # 考虑time embedding的RES后的Conv3x3
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [76, 1], "IN1": [76, 0],     "OUT":[[77, 0]]    }], # 通道不匹配做的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[78, 0]]     }], # 第一个RES后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[78, 1], [78, 2], [78, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[78, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[78, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[78, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [78, 6], "IN1": [78, 0],     "OUT":[[79, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[79, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[79, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[79, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [79, 5], "IN1": [78, 6],     "OUT":[[80, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[80, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [80, 1], "IN1": [79, 5],     "OUT":[[81, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[81, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [81, 1], "IN1": [77, 0],     "OUT":[[82, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[83, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[83, 1]]     },# 第二个ResBLK  
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [83, 1], "IN1": [83, 0],     "OUT":[[84, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[84, 1]]    },
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [84, 1], "IN1": [82, 0],     "OUT":[[85, 0]]    }], # 考虑time embedding的RES后的Conv3x3


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[86, 0]]    }], # RESNetBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[86, 1], [86, 2], [86, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[86, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[86, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[86, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [86, 6], "IN1": [86, 0],     "OUT":[[87, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[87, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[87, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[87, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [87, 5], "IN1": [86, 6],     "OUT":[[88, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[88, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [88, 1], "IN1": [87, 5],     "OUT":[[89, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[89, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [89, 1], "IN1": [85, 0],     "OUT":[[90, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[91, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[92, 0]]   }], # Downsample3x3卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[92, 1]]   },# 第二个Crossattndown的第一个ResBLK的第一个卷积操作
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [92, 1], "IN1": [92, 0],     "OUT":[[93, 0]]     }],# time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[93, 1]]     }, # 考虑time embedding的RES后的Conv3x3
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [93, 1], "IN1": [93, 0],     "OUT":[[94, 0]]    }], # 通道不匹配做的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[95, 0]]     }], # 第一个RES后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[95, 1], [95, 2], [95, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[95, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[95, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[95, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [95, 6], "IN1": [95, 0],     "OUT":[[96, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[96, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[96, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[96, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [96, 5], "IN1": [95, 6],     "OUT":[[97, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[97, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [97, 1], "IN1": [96, 5],     "OUT":[[98, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[98, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [98, 1], "IN1": [94, 0],     "OUT":[[99, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[100, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[100, 1]]     },# 第二个ResBLK  
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [100, 1], "IN1": [100, 0],     "OUT":[[101, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[101, 1]]    },
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [101, 1], "IN1": [99, 0],     "OUT":[[102, 0]]    }], # 考虑time embedding的RES后的Conv3x3


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[103, 0]]    }], # RESNetBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[103, 1], [103, 2], [103, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[103, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[103, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[103, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [103, 6], "IN1": [103, 0],     "OUT":[[104, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[104, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[104, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[104, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [104, 5], "IN1": [103, 6],     "OUT":[[105, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[105, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [105, 1], "IN1": [104, 5],     "OUT":[[106, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[106, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [106, 1], "IN1": [102, 0],     "OUT":[[107, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[108, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[109, 0]]    }], # Downsample3x3卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[109, 1]]     },# DownBLK第一个ResBLK
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [109, 1], "IN1": [109, 0],     "OUT":[[110, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[110, 1]]     }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [110, 1], "IN1": [108, 0],     "OUT":[[111, 0]]     }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[112, 0]]     }], # 第一个RESBLK后的伪卷积

                    
                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[112, 1]]     }, # DownBLK的第二个ResBLK的第一个卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [112, 1], "IN1": [112, 0],     "OUT":[[113, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[113, 1]]     },
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [113, 1], "IN1": [111, 0],     "OUT":[[114, 0]]     }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[115, 0]]     }], # DownBLK模块后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[115, 1]]     },# UNETMIDBLK第一个ResBLK
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [115, 1], "IN1": [115, 0],     "OUT":[[116, 0]]      }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[116, 1]]     },
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [116, 1], "IN1": [114, 0],     "OUT":[[117, 0]]      }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[118, 0]]     }], # UNETMIDBLK第一个RESBLK后的伪卷积

                    
                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[118, 1], [118, 2], [118, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[118, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[118, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[118, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [118, 6], "IN1": [118, 0],     "OUT":[[119, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[119, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[119, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[119, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [119, 5], "IN1": [118, 6],     "OUT":[[120, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[120, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [120, 1], "IN1": [119, 5],     "OUT":[[121, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[121, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [121, 1], "IN1": [117, 0],     "OUT":[[122, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[123, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[123, 1]]     },# UNETMIDBLK第二个ResBLK
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [123, 1], "IN1": [123, 0],     "OUT":[[124, 0]]    }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[124, 1]]    },# fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [124, 1], "IN1": [122, 0],     "OUT":[[125, 0]]     }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[126, 0]]    }], # UNETMIDBLK第二个RESBLK后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [125, 0], "IN1": [114, 0],     "OUT":[[127, 0]]     }], # UPBLK第一个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[127, 1]]    }, # UPBLK第一个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [127, 1], "IN1": [127, 0],     "OUT":[[128, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[128, 1]]    }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [128, 1], "IN1": [126, 0],     "OUT":[[129, 0]]    }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[130, 0]]     }], # UPBLK第一个RESBLK后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [129, 0], "IN1": [111, 0],     "OUT":[[131, 0]]     }], # UPBLK第二个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[131, 1]]    }, # UPBLK第二个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [131, 1], "IN1": [131, 0],     "OUT":[[132, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[132, 1]]     }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [132, 0], "IN1": [130, 0],     "OUT":[[133, 0]]     }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[134, 0]]     }], # UPBLK第二个RESBLK后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [133, 0], "IN1": [108, 0],     "OUT":[[135, 0]]      }], # UPBLK第三个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[135, 1]]    }, # UPBLK第三个RESBLK的第一层卷积s
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [135, 1], "IN1": [135, 0],     "OUT":[[136, 0]]   }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[136, 1]]    }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [136, 1], "IN1": [134, 0],     "OUT":[[137, 0]]      }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[138, 0]]     }], # UPBLK第三个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[139, 0]]     }], # UPsample与3x3卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [138, 0], "IN1": [107, 0],     "OUT":[[140, 0]]     }], # 第一个CrossattnUPBLK第一个RESBLK的concate伪卷积
                     
                     
                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[140, 1]]    }, # CrossattnUPBLK第一个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [140, 1], "IN1": [140, 0],     "OUT":[[141, 0]]    }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[141, 1]]    }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [141, 1], "IN1": [139, 0],     "OUT":[[142, 0]]     }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[143, 0]]    }], # CrossattnUPBLK第一个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[143, 1], [143, 2], [143, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[143, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[143, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[143, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [143, 6], "IN1": [143, 0],     "OUT":[[144, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[144, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[144, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[144, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [144, 5], "IN1": [143, 6],     "OUT":[[145, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[145, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [145, 1], "IN1": [144, 5],     "OUT":[[146, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[146, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [146, 1], "IN1": [142, 0],     "OUT":[[147, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[148, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [147, 0], "IN1": [99, 0],     "OUT":[[149, 0]]     }], # CrossattnUPBLK第二个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[149, 1]]    }, # CrossattnUPBLK第二个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [149, 1], "IN1": [149, 0],     "OUT":[[150, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[150, 1]]    }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [150, 1], "IN1": [148, 0],     "OUT":[[151, 0]]      }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[152, 0]]    }], # CrossattnUPBLK第二个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[152, 1], [152, 2], [152, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[152, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[152, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[152, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [152, 6], "IN1": [152, 0],     "OUT":[[153, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[153, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[153, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[153, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [153, 5], "IN1": [152, 6],     "OUT":[[154, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[154, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [154, 1], "IN1": [153, 5],     "OUT":[[155, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[155, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [155, 1], "IN1": [151, 0],     "OUT":[[156, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[157, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [156, 0], "IN1": [82, 0],     "OUT":[[158, 0]]      }], # CrossattnUPBLK第三个RESBLK的concate伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[158, 1]]     }, # CrossattnUPBLK第三个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [158, 1], "IN1": [158, 0],     "OUT":[[159, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[159, 1]]     }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [159, 1], "IN1": [157, 0],     "OUT":[[160, 0]]      }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[161, 0]]     }], # CrossattnUPBLK第三个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[161, 1], [161, 2], [161, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[161, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[161, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[161, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [161, 6], "IN1": [161, 0],     "OUT":[[162, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[162, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[162, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[162, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [162, 5], "IN1": [161, 6],     "OUT":[[163, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[163, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [163, 1], "IN1": [162, 5],     "OUT":[[164, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[164, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [164, 1], "IN1": [160, 0],     "OUT":[[165, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[166, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[167, 0]]     }], # UPsample的插值与3x3卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [166, 0], "IN1": [90, 0],     "OUT":[[168, 0]]     }], # 第二个CrossattnUPBLK第一个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[168, 1]]    }, # CrossattnUPBLK第一个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [168, 1], "IN1": [168, 0],     "OUT":[[169, 0]]    }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[169, 1]]     }, # time embedding后的卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [169, 1], "IN1": [169, 0],     "OUT":[[170, 0]]    }], # 通道不匹配做的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[171, 0]]     }], # CrossattnUPBLK第一个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[171, 1], [171, 2], [171, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[171, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[171, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[171, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [171, 6], "IN1": [171, 0],     "OUT":[[172, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[172, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[172, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[172, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [172, 5], "IN1": [171, 6],     "OUT":[[173, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[173, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [173, 1], "IN1": [172, 5],     "OUT":[[174, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[174, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [174, 1], "IN1": [170, 0],     "OUT":[[175, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[176, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [175, 0], "IN1": [82, 0],     "OUT":[[177, 0]]     }], # CrossattnUPBLK第二个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[177, 1]]    }, # CrossattnUPBLK第二个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [177, 1], "IN1": [177, 0],     "OUT":[[178, 0]]    }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[178, 1]]    }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [178, 1], "IN1": [176, 0],     "OUT":[[179, 0]]     }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[180, 0]]   }], # CrossattnUPBLK第二个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[180, 1], [180, 2], [180, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[180, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[180, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[180, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [180, 6], "IN1": [180, 0],     "OUT":[[181, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[181, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[181, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[181, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [181, 5], "IN1": [180, 6],     "OUT":[[182, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[182, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [182, 1], "IN1": [181, 5],     "OUT":[[183, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[183, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [183, 1], "IN1": [179, 0],     "OUT":[[184, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[185, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [184, 0], "IN1": [74, 0],     "OUT":[[186, 0]]     }], # CrossattnUPBLK第三个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[186, 1]]    }, # CrossattnUPBLK第三个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [186, 1], "IN1": [186, 0],     "OUT":[[187, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[187, 1]]    }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [187, 1], "IN1": [185, 0],     "OUT":[[188, 0]]      }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[189, 0]]      }], # CrossattnUPBLK第三个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[189, 1], [189, 2], [189, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[189, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[189, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[189, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [189, 6], "IN1": [189, 0],     "OUT":[[190, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[190, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[190, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[190, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [190, 5], "IN1": [189, 6],     "OUT":[[191, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[191, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [191, 1], "IN1": [190, 5],     "OUT":[[192, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[192, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [192, 1], "IN1": [188, 0],     "OUT":[[193, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[194, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[195, 0]]      }], # UPsample的插值与3x3卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [195, 0], "IN1": [73, 0],     "OUT":[[196, 0]]      }], # 第三个CrossattnUPBLK第一个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[196, 1]]    }, # CrossattnUPBLK第一个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [196, 1], "IN1": [196, 0],     "OUT":[[197, 0]]   }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[197, 1]]     }, # time embedding后的卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [197, 1], "IN1": [197, 0],     "OUT":[[198, 0]]   }], # 通道不匹配做的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[199, 0]]    }], # CrossattnUPBLK第一个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[199, 1], [199, 2], [199, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[199, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[199, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[199, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [199, 6], "IN1": [199, 0],     "OUT":[[200, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[200, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[200, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[200, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [200, 5], "IN1": [199, 6],     "OUT":[[201, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[201, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [201, 1], "IN1": [200, 5],     "OUT":[[202, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[202, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [202, 1], "IN1": [198, 0],     "OUT":[[203, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[204, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [203, 0], "IN1": [65, 0],     "OUT":[[205, 0]]     }], # CrossattnUPBLK第二个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[205, 1]]    }, # CrossattnUPBLK第二个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [205, 1], "IN1": [205, 0],     "OUT":[[206, 0]]     }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[206, 1]]    }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [206, 1], "IN1": [204, 0],     "OUT":[[207, 0]]     }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[208, 0]]     }], # CrossattnUPBLK第二个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[208, 1], [208, 2], [208, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[208, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[208, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[208, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [208, 6], "IN1": [208, 0],     "OUT":[[209, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[209, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[209, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[209, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [209, 5], "IN1": [208, 6],     "OUT":[[210, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[210, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [210, 1], "IN1": [209, 5],     "OUT":[[211, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[211, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [211, 1], "IN1": [207, 0],     "OUT":[[212, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[213, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": True, "RES": False, "ITP": False, "MTN": False,  "IN0": [213, 0], "IN1": [57, 0],     "OUT":[[214, 0]]     }], # CrossattnUPBLK第三个RESBLK的concate伪卷积
                     

                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[214, 1]]    }, # CrossattnUPBLK第三个RESBLK的第一层卷积
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [214, 1], "IN1": [214, 0],     "OUT":[[215, 0]]    }], # time embedding


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[215, 1]]    }, # fake conv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [215, 1], "IN1": [213, 0],     "OUT":[[216, 0]]     }], # time embedding后的卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[217, 0]]     }], # CrossattnUPBLK第三个RESBLK后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,     "OUT":[[217, 1], [217, 2], [217, 4]]     }, # Transformer第一层1x1卷积
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[217, 3]]    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[217, 5]]    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[217, 6]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [217, 6], "IN1": [217, 0],     "OUT":[[218, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[218, 3]]     }, # linear_wq
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wv
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[218, 4]]   }, # MATMUL_qk
                    {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[218, 5]]    }, # MATMUL_vr
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [218, 5], "IN1": [217, 6],     "OUT":[[219, 0]]    }], # linear_wo


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[219, 1]]    }, # feedward中linearGELU
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [219, 1], "IN1": [218, 5],     "OUT":[[220, 0]]    }], # feedward中linear


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,     "OUT":[[220, 1]]    }, # fakeconv
                    {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [220, 1], "IN1": [216, 0],     "OUT":[[221, 0]]    }], # basictransfromer后的reshapeConv1x1


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[222, 0]]    }], # Transformer后的伪卷积


                    [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[223, 0]]     }], # GNSiLUConv2D的卷积


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[224, 0]]     }], # conv1x1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[225, 0]]     }], # conv3x3


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[225, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [225, 1],      "IN1": [224, 0],     "OUT":[[226, 0]]     }],

                  [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[226, 1], [226, 2], [226, 4]]     },
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # linear_wq（selfattention的wk与wv也忽略）
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[226, 3]]    }, # linear_wk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0    }, # MATMUL_qk
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[226, 5]]    }, # linear_wv
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[226, 6]]    }, # MATMUL_vr
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [226, 6], "IN1": [226, 0],     "OUT":[[227, 0]]    }], # linear_wo


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[227, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [227, 1],"IN1": [227, 0],     "OUT":[[228, 0]]     }], 


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[228, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [228, 1],      "IN1": [227, 1],     "OUT":[[229, 0]]     }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[229, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [229,1],      "IN1": [228, 1],     "OUT":[[230, 0]]   }],


                  [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[230, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [230, 1],      "IN1": [229, 1],     "OUT":[[231, 0]]   }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[232, 0]]     }], # upsample


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[232, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [232, 1],      "IN1": [231, 0],     "OUT":[[233, 0]]     }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[233, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [233, 1],      "IN1": [232, 1],     "OUT":[[234, 0]]   }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[234, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [234, 1],      "IN1": [233, 1],     "OUT":[[235, 0]]   }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[236, 0]]     }], # upsample


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[236, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [236, 1],      "IN1": [235, 0],     "OUT":[[237, 0]]     }],


                  [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[237, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [237, 1],      "IN1": [236, 1],     "OUT":[[238, 0]]   }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[238, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [238, 1],      "IN1": [237, 1],     "OUT":[[239, 0]]   }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[240, 0]]     }], # upsample


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[240, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [240, 1],      "IN1": [239, 0],     "OUT":[[241, 0]]     }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[241, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [241, 1],      "IN1": [240, 1],     "OUT":[[242, 0]]   }],


                  [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":[[242, 1]]     },
                   {"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [242, 1],      "IN1": [241, 1],     "OUT":[[243, 0]]   }],


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,     "OUT":0     }], 
                

                    ] # [P Res/Cnc?, Perform Res?, Interplot? x 4, Maintain? for next ResCnv, [Which OFM0], [Which OFM1]]

K               = 4
ITP_RATE        = 4 # Interplote Rate
SMP_RATE        = 4 # Sampling Rate
NN_MAX_LAYER    = 7

NN_FPS_AVGPNT_PERBLOCK = 64/3.4 if ENA_ABS else 256 # vs PNNPU
FPS_MAXDIFF_PERBLOCK   = 3      if ENA_ABS else 2
NN_KNN_AVGPNT_PERBLOCK = 512 # Center Points

NN_TOTAL_GOP = 1.6


# # 80% Channel Sparsity
# NN_NUM_FIL_ORI  = [[32],    [48, 28, 52], [100, 56, 112], [180,  80, 228], [256, 150, 256],   [111, 146],   [128, 128,  40]]
# NN_NUM_CHN_IN   = [[3 ],    [32, 35, 28], [ 52, 58,  56], [100, 100, 100], [128, 128, 128],   [ 54, 130],   [ 95, 128, 128]]
# NN_REAL_GOP  = 0.77
# SA = 30 # Sparsity
# SW = 80

# 89% Channel Sparsity
NN_NUM_FIL_ORI  = [[768, 768],   
                   [768, 768, 77, 768, 96, 768],
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 77, 768, 96, 768], 
                   [768, 768], 
                   [768],
                   [3],
                   [128],    
                   [128, 128],
                   [128, 128], 
                   [128],
                   [256, 256], 
                   [256, 256], 
                   [256],
                   [512, 512], 
                   [512, 512], 
                   [512], 
                   [512, 512], 
                   [512, 512],
                   [512, 512], 
                   [512], 
                   [512, 512, 4096, 512, 64, 512], 
                   [512, 512], 
                   [8],
                   [8],
                   [4],
                   [320],    
                   [320, 320], 
                   [320, 320],
                   [320], 
                   [320, 320, 320, 4096, 320, 40, 320], 
                   [320, 320, 320, 77, 40, 320], 
                   [1280, 320], 
                   [320, 320],
                   [320], 
                   [320, 320], 
                   [320, 320],
                   [320], 
                   [320, 320, 320, 4096, 320, 40, 320], 
                   [320, 320, 320, 77, 40, 320], 
                   [1280, 320], 
                   [320, 320], 
                   [320],
                   [320],
                   [640, 640], 
                   [640, 640], 
                   [640], 
                   [640, 640, 640, 640, 1024, 80, 640], 
                   [640, 640, 640, 77, 80, 640], 
                   [1280, 640], 
                   [640, 640],
                   [640],
                   [640, 640], 
                   [640, 640], 
                   [640],
                   [640, 640, 640, 640, 1024, 80, 640], 
                   [640, 640, 640, 77, 80, 640], 
                   [1280, 640], 
                   [640, 640], 
                   [640],
                   [640],
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280], 
                   [1280, 1280, 1280, 1280, 256, 160, 1280], 
                   [1280, 1280, 1280, 77, 160, 1280], 
                   [1280, 1280], 
                   [1280, 1280],
                   [1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280, 1280, 1280, 256, 160, 1280], 
                   [1280, 1280, 1280, 77, 160, 1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280],
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280], 
                   [1280, 1280],
                   [1280],
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280, 1280, 1280, 64, 160, 1280], 
                   [1280, 1280, 1280, 77, 160, 1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280], 
                   [1280, 1280],
                   [1280],
                   [2560], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [2560], 
                   [1280, 1280], 
                   [1280, 1280],
                   [1280],
                   [1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280],
                   [2560], 
                   [1280, 1280], 
                   [1280, 1280],
                   [1280], 
                   [1280, 1280, 1280, 1280, 256, 160, 1280], 
                   [1280, 1280, 1280, 77, 160, 1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [2560], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280, 1280, 1280, 256, 160, 1280], 
                   [1280, 1280, 1280, 77, 160, 1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [2560], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280, 1280, 1280, 256, 160, 1280], 
                   [1280, 1280, 1280, 77, 160, 1280], 
                   [1280, 1280], 
                   [1280, 1280],
                   [1280],
                   [1280],
                   [1920], 
                   [640, 640],
                   [640, 640], 
                   [640], 
                   [640, 640, 640, 640, 1024, 80, 640], 
                   [640, 640, 640, 77, 80, 640], 
                   [1280, 640], 
                   [640, 640], 
                   [640],
                   [1280], 
                   [640, 640], 
                   [640, 640], 
                   [640],
                   [640, 640, 640, 640, 1024, 80, 640], 
                   [640, 640, 640, 77, 80, 640], 
                   [1280, 640], 
                   [640, 640],  
                   [640],
                   [1280], 
                   [640, 640], 
                   [640, 640], 
                   [640],
                   [640, 640, 640, 640, 1024, 80, 640], 
                   [640, 640, 640, 77, 80, 640], 
                   [1280, 640], 
                   [640, 640],  
                   [640], 
                   [640],
                   [960], 
                   [320, 320], 
                   [320, 320], 
                   [320], 
                   [320, 320, 320, 320, 4096, 40, 320], 
                   [320, 320, 320, 77, 40, 320], 
                   [1280, 320], 
                   [320, 320],
                   [320], 
                   [640], 
                   [320, 320], 
                   [320, 320], 
                   [320],
                   [320, 320, 320, 320, 4096, 40, 320], 
                   [320, 320, 320, 77, 40, 320], 
                   [1280, 320], 
                   [320, 320], 
                   [320],
                   [640], 
                   [320, 320], 
                   [320, 320], 
                   [320],
                   [320, 320, 320, 320, 4096, 40, 320], 
                   [320, 320, 320, 77, 40, 320], 
                   [1280, 320], 
                   [320, 320], 
                   [320],
                   [4],
                   [4],
                   [512],
                   [512, 512], 
                   [512, 512, 512, 4096, 64, 512, 512], 
                   [512, 512],
                   [512, 512], 
                   [512, 512], 
                   [512, 512], 
                   [512],
                   [512, 512], 
                   [512, 512], 
                   [512, 512], 
                   [512],
                   [256, 256], 
                   [256, 256], 
                   [256, 256], 
                   [256],
                   [128, 128], 
                   [128, 128], 
                   [128, 128], 
                   [3]

                   
                   ]  
NN_NUM_CHN_IN   = [[1, 768],   
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768, 768, 96, 768, 77, 768], 
                   [768, 768], 
                   [768],
                   [768],
                   [3],    
                   [128, 128], 
                   [128, 128], 
                   [128],
                   [128, 256], 
                   [256, 256], 
                   [256],
                   [256, 512], 
                   [512, 512], 
                   [512], 
                   [512, 512], 
                   [512, 512],
                   [512, 512], 
                   [512], 
                   [512, 512, 64, 512, 4096, 512], 
                   [512, 512], 
                   [512],
                   [8],
                   [8],
                   [4],    
                   [320, 1280], 
                   [320, 320], 
                   [320],
                   [320, 320, 320, 40, 320, 4096, 320], 
                   [320, 768, 768, 40, 70, 320], 
                   [320, 1280], 
                   [320, 320],
                   [320], 
                   [320, 1280], 
                   [320, 320],
                   [320],  
                   [320, 320, 320, 40, 320, 4096, 320], 
                   [320, 768, 768, 40, 77, 320], 
                   [320, 1280], 
                   [320, 320], 
                   [320],
                   [320],
                   [320, 1280], 
                   [640, 640],
                   [320], 
                   [640, 640, 640, 640, 80, 1024, 640], 
                   [640, 768, 768, 80, 77, 640], 
                   [640, 1280], 
                   [640, 640],
                   [640], 
                   [640, 1280], 
                   [640, 640], 
                   [640],
                   [640, 640, 640, 640, 80, 1024, 640], 
                   [640, 768, 768, 80, 77, 640], 
                   [640, 1280], 
                   [640, 640], 
                   [640],
                   [640],
                   [640, 1280], 
                   [1280, 640], 
                   [1280], 
                   [1280, 1280, 1280, 1280, 160, 256, 1280], 
                   [1280, 768, 768, 160, 77, 1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280, 1280, 1280, 160, 256, 1280], 
                   [1280, 768, 768, 160, 77, 1280], 
                   [1280, 1280], 
                   [1280, 1280],  
                   [1280],
                   [1280],
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280], 
                   [1280, 1280],
                   [1280],
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280, 1280, 1280, 160, 64, 1280], 
                   [1280, 768, 768, 160, 77, 1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280], 
                   [1280, 1280],
                   [1280],
                   [1280], 
                   [2560, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280], 
                   [2560, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280],
                   [1280], 
                   [2560, 1280], 
                   [1280, 1280],
                   [1280], 
                   [1280, 1280, 1280, 1280, 160, 256, 1280], 
                   [1280, 768, 768, 160, 77, 1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280], 
                   [2560, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280, 1280, 1280, 160, 256, 1280], 
                   [1280, 768, 768, 160, 77, 1280], 
                   [1280, 1280], 
                   [1280, 1280],
                   [1280],  
                   [1280], 
                   [2560, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280, 1280, 1280, 1280, 160, 256, 1280], 
                   [1280, 768, 768, 160, 77, 1280], 
                   [1280, 1280], 
                   [1280, 1280], 
                   [1280],
                   [1280],
                   [1280], 
                   [1920, 1280], 
                   [640, 1280], 
                   [1280], 
                   [640, 640, 640, 640, 80, 1024, 640], 
                   [640, 768, 768, 80, 77, 640], 
                   [640, 1280], 
                   [640, 640], 
                   [640],
                   [640], 
                   [1280, 1280], 
                   [640, 640], 
                   [640],
                   [640, 640, 640, 640, 80, 1024, 640], 
                   [640, 768, 768, 80, 77, 640], 
                   [640, 1280], 
                   [640, 640],   
                   [640],
                   [640], 
                   [1280, 1280], 
                   [640, 640], 
                   [640],
                   [640, 640, 640, 640, 80, 1024, 640], 
                   [640, 768, 768, 80, 77, 640], 
                   [640, 1280], 
                   [640, 640],    
                   [640],
                   [640],
                   [640], 
                   [960, 1280], 
                   [320, 640], 
                   [320], 
                   [320, 320, 320, 320, 40, 4096, 320], 
                   [320, 768, 768, 40, 77, 320], 
                   [320, 1280], 
                   [320, 320], 
                   [320],
                   [320], 
                   [640, 1280], 
                   [320, 320], 
                   [320],
                   [320, 320, 320, 320, 40, 4096, 320], 
                   [320, 768, 768, 40, 77, 320], 
                   [320, 1280], 
                   [320, 320],  
                   [320],
                   [320], 
                   [640, 1280], 
                   [320, 320],
                   [320], 
                   [320, 320, 320, 320, 40, 4096, 320], 
                   [320, 768, 768, 40, 77, 320], 
                   [320, 1280], 
                   [320, 320], 
                   [320],
                   [320],
                   [4],
                   [4],
                   [512, 512],
                   [512, 512, 512, 64, 4096, 512, 512], 
                   [512, 512],
                   [512, 512], 
                   [512, 512], 
                   [512, 512], 
                   [512],
                   [512, 512], 
                   [512, 512], 
                   [512, 512], 
                   [512],
                   [256, 256], 
                   [256, 256], 
                   [256, 256], 
                   [256],
                   [128, 128], 
                   [128, 128], 
                   [128, 128], 
                   [128]
                
                   
                   ]

NN_REAL_GOP  = 1.5
SA = 40 # Sparsity
SW = 89

# # 96.6% Channel Sparsity
# NN_NUM_FIL_ORI  = [[32],    [16, 16, 16], [46, 32, 47], [48,  48, 48], [47, 111, 47 ],   [111, 95],   [128, 128, 40 ]]
# NN_NUM_CHN_IN   = [[3 ],    [32, 35, 14], [15, 18, 24], [31 , 34, 23], [18, 21,  111],   [54, 110],   [95,  128, 128]]
# NN_REAL_GOP  = 0.007
# SA = 61.78 # Sparsity
# SW = 96.6
NN_NUM_FIL      =   NN_NUM_FIL_ORI


# ##############################################################
# #LOCAL_ATT
# ##############################################################
if LOCAL_ATTENTION:
   LOCAL_ATT_STG = [1,4,7,10,13,16,19,22,25,28,31,34,52,61,62,69,70,78,79,86,87,95,96,103,104,118,119,143,144,152,153,161,162,171,172,180,181,189,190,199,200,208,209,217,218,226]

   from collections import defaultdict
   REPEAT_STG = defaultdict(lambda: 1, {1:1,4:1,7:1,10:1,13:1,16:1,19:1,22:1,25:1,28:1,31:1,34:1,52:1,61:1,62:1,69:1,70:1,78:1,79:1,86:1,87:1,95:1,96:1,103:1,104:1,118:1,119:1,143:1,144:1,152:1,153:1,161:1,162:1,171:1,172:1,180:1,181:1,189:1,190:1,199:1,200:1,208:1,209:1,217:1,218:1,226:1}) 
   Heads = 8