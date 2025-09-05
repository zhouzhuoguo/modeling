from HW_Settings_PTV2 import *
import numpy as np

# ######################################
# @ PTV2
# ######################################

# """
TASK = "PTV2"
CATE = "KITTI_LOCAL_ATT"
NN_NUM_STG      = 61
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
                   False
                   ]
NN_POL_ENA      = [False,
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
                   True,
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
                   True,
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
                   True,
                   False,
                   False,
                   False,
                   False
                   
                   ]
# NN_FPS_ENA      = [False,   False, False, False, False,     False, False, False, False,     False]
# NN_KNN_ENA      = [False,   False, False, False, False,     False, False, False, False,     False]
# NN_POL_ENA      = [False,   False, False, False, False,     False, False, False, False,     False]

NN_NUM_CNV          = [1,
4,
4,
1,
1,
4,
4,
1,
4,
4,
1,
1,
4,
4,
1,
4,
4,
1,
1,
4,
4,
1,
4,
4,
1,
4,
4,
1,
4,
4,
1,
4,
4,
1,
4,
4,
1,
1,
4,
4,
1,
4,
4,
1,
1,
4,
4,
1,
1,
4,
4,
1,
1,
4,
4,
1,
1,
4,
4,
1,
1
                       ]

INPUT_SCALE = 1
NN_NUM_INPNT_STG    = np.array([131072// INPUT_SCALE,
                                131072// INPUT_SCALE,
                                1,
                                131072// INPUT_SCALE,
                                131072// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                512// INPUT_SCALE,
                                1,
                                512// INPUT_SCALE,
                                512// INPUT_SCALE,
                                1,
                                512// INPUT_SCALE,
                                512// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                131072// INPUT_SCALE,
                                1,
                                131072// INPUT_SCALE,
                                131072// INPUT_SCALE
                                        
                       ]) 
NN_NUM_OUTPNT_STG   = np.array([131072// INPUT_SCALE,
                                131072// INPUT_SCALE,
                                1,
                                131072// INPUT_SCALE,
                                131072// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                512// INPUT_SCALE,
                                1,
                                512// INPUT_SCALE,
                                512// INPUT_SCALE,
                                1,
                                512// INPUT_SCALE,
                                512// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                131072// INPUT_SCALE,
                                1,
                                131072// INPUT_SCALE,
                                131072// INPUT_SCALE 
                       ]) 

NN_NUM_OUTPNT_STG_POL= np.array([131072// INPUT_SCALE,
                                 131072// INPUT_SCALE,
                                1,
                                131072// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                512// INPUT_SCALE,
                                512// INPUT_SCALE,
                                1,
                                512// INPUT_SCALE,
                                512// INPUT_SCALE,
                                1,
                                512// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                2048// INPUT_SCALE,
                                1,
                                2048// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                8192// INPUT_SCALE,
                                1,
                                8192// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                32768// INPUT_SCALE,
                                1,
                                32768// INPUT_SCALE,
                                131072// INPUT_SCALE,
                                131072// INPUT_SCALE,
                                1,
                                131072// INPUT_SCALE,
                                131072// INPUT_SCALE
                       ])

NN_ARCH         = [[{"CNC": False, "RES": False, "ITP": False, "MTN": False, "SRC": True, "IN0": 0,      "IN1": 0,   "OUT": [[1, 0]]     }], # GVAPatchEmbed
                   

                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[1, 1], [1, 2], [1, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[2, 0]]    }], # linear_q downsample 130K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[2, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[2, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[2, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[3, 0]]    }], # Attention Output upsample 1 - 130k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [3, 0],   "IN1": [0, 0],   "OUT": [[4, 0]]    }], # NormReLUFCNorm Res  


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[5, 0]]    }], # MLP&POL 130k - 32k


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[5, 1], [5, 2], [5, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[6, 0]]   }], #  linear_q downsample 32K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[6, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[6, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[6, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[7, 0]]    }], # Attention Output upsample 1 - 32k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [7, 0],   "IN1": [4, 0],   "OUT": [[8, 0]]    }], # NormReLUFCNorm Res


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[8, 1], [8, 2], [8, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[9, 0]]    }], # linear_q downsample 32K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[9, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[9, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[9, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[10, 0]]    }], # Attention Output upsample 1 - 32k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [10, 0],   "IN1": [7, 0],   "OUT": [[11, 0]]    }], # NormReLUFCNorm Res encoder1-2 


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[12, 0]]    }], # MLP&POL 32k - 8k


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[12, 1], [12, 2], [12, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[13, 0]]    }], # linear_q downsample 8K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[13, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[13, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[13, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[14, 0]]   }], # Attention Output upsample 1 - 8k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [14, 0],   "IN1": [11, 0],   "OUT": [[15, 0]]    }], # NormReLUFCNorm Res


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[15, 1], [15, 2], [15, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[16, 0]]    }], # linear_q downsample 8K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[16, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[16, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[16, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[17, 0]]    }], # Attention Output upsample 1 - 8k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [17, 0],   "IN1": [14, 0],   "OUT": [[18, 0]]    }], # NormReLUFCNorm Res encoder2-2 


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[19, 0]]    }], # MLP&POL  8k - 2k


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[19, 1], [19, 2], [19, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[20, 0]]    }], # linear_q downsample 2K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[20, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[20, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[20, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[21, 0]]    }], # Attention Output upsample 1 - 2k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [21, 0],   "IN1": [18, 0],   "OUT": [[22, 0]]    }], # NormReLUFCNorm Res encoder3-1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[22, 1], [22, 2], [22, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[23, 0]]    }], # linear_q downsample 2K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[23, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[23, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[23, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[24, 0]]    }], # Attention Output upsample 1 - 2k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [24, 0],   "IN1": [21, 0],   "OUT": [[25, 0]]    }], # NormReLUFCNorm Res encoder3-2


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[25, 1], [25, 2], [25, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[26, 0]]    }], # linear_q downsample 2K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[26, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[26, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[26, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[27, 0]]    }], # Attention Output upsample 1 - 2k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [27, 0],   "IN1": [24, 0],   "OUT": [[28, 0]]    }], # NormReLUFCNorm Res encoder3-3


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[28, 1], [28, 2], [28, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[29, 0]]    }], # fake conv downsample 2K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[29, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[29, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[29, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[30, 0]]    }], # fake conv upsample 1 - 2k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [30, 0],   "IN1": [27, 0],   "OUT": [[31, 0]]    }], # NormReLUFCNorm Res encoder3-4
                   

                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[31, 1], [31, 2], [31, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[32, 0]]    }], # fake conv downsample 2K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[32, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[32, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[32, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[33, 0]]    }], # fake conv  upsample 1 - 2k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [33, 0],   "IN1": [30, 0],   "OUT": [[34, 0]]    }], # NormReLUFCNorm Res encoder3-5


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[34, 1], [34, 2], [34, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[35, 0]]    }], # fake conv downsample 2K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[35, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[35, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[35, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[36, 0]]    }], # fake conv upsample 1 - 2k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [36, 0],   "IN1": [33, 0],   "OUT": [[37, 0]]    }], # NormReLUFCNorm Res


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[38, 0]]    }], # MLP&POL  encoder3-6 2k - 0.5k


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[38, 1], [38, 2], [38, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[39, 0]]    }], # linear_q  downsample 0.5K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[39, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[39, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[39, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[40, 0]]    }], #  upsample 1 - 0.5k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [40, 0],   "IN1": [37, 0],   "OUT": [[41, 0]]    }], # NormReLUFCNorm Res encoder4-1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[41, 1], [41, 2], [41, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0   }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[42, 0]]    }], # downsample 0.5K - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[42, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[42, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[42, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[43, 0]]    }], #  upsample 1 - 0.5k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [43, 0],   "IN1": [40, 0],   "OUT": [[44, 0]]    }], # NormReLUFCNorm Res encoder4-2


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [44, 0],       "IN1": [36, 0],   "OUT": [[45, 0]]    }], # upsample 0.5k - 2k
                   

                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[45, 1], [45, 2], [45, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[46, 0]]    }], # dowmsample 2k - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[46, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[46, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[46, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[47, 0]]    }], #  upsample 1 - 2k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [47, 0],   "IN1": [44, 0],   "OUT": [[48, 0]]    }], # NormReLUFCNorm Res decoder1


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [48, 0],       "IN1": [17, 0],   "OUT": [[49, 0]]    }], # upsample 2k - 8k


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[49, 1], [49, 2], [49, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[50, 0]]    }], #  dowmsample 8k - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[50, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[50, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[50, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[51, 0]]    }], #  upsample 1 - 8k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [51, 0],   "IN1": [48, 0],   "OUT": [[52, 0]]    }], # NormReLUFCNorm Res decoder2


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [52, 0],      "IN1": [10, 0],   "OUT": [[53, 0]]    }], # upsample 8k - 32k


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[53, 1], [53, 2], [53, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0   }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[54, 0]]    }], #  downsample 32k - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[54, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[54, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[54, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[55, 0]]    }], #  upsample 1 - 32k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [55, 0],   "IN1": [52, 0],   "OUT": [[56, 0]]    }], # NormReLUFCNorm Res decoder3


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [56, 0],      "IN1": [3, 0],   "OUT": [[57, 0]]    }], # upsample 32k - 130k


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,      "IN1": 0,   "OUT": [[57, 1], [57, 2], [57, 3]]     }, # FCNormReLU  
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_v
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": 0    }, # linear_k
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[58, 0]]    }], #  downsample 130k - 1


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[58, 1]]    }, # relative position encoding pem linear
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[58, 2]]    }, # weight encoding liear1
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[58, 3]]    }, # weight encoding liear2
                   {"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0,       "IN1": 0,   "OUT": [[59, 0]]    }], #  upsample 1 - 130k


                   [{"CNC": False, "RES": True, "ITP": False, "MTN": False,  "IN0": [59, 0],   "IN1": [56, 0],   "OUT": [[60, 0]]    }], # NormReLUFCNorm Res decoder4


                   [{"CNC": False, "RES": False, "ITP": False, "MTN": False,  "IN0": 0, "IN1": 0,   "OUT": 0    }] # Seghead





                    
                ] # [P Res/Cnc?, Perform Res?, Interplot? x 4, Maintain? for next ResCnv, [Which OFM0], [Which OFM1]]

K               = 4 # be used in POL
ITP_RATE        = 4 # Interplote Rate
SMP_RATE        = 4 # Sampling Rate
NN_MAX_LAYER    = 5

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
NN_NUM_FIL_ORI  = [[48],
                   [48, 48, 48, 48], 
                   [8, 8, 8, 48], 
                   [48],
                   [96],
                   [96, 96, 96, 96],
                   [16, 16, 16, 96],
                   [96],
                   [96, 96, 96, 96],
                   [16, 16, 16, 96],
                   [96], 
                   [192], 
                   [192, 192, 192, 192],
                   [16, 16, 16, 192],
                   [192],
                   [192, 192, 192, 192],
                   [16, 16, 16, 192],
                   [192],
                   [384],
                   [384, 384, 384, 384], 
                   [16, 16, 16, 384],
                   [384],
                   [384, 384, 384, 384], 
                   [16, 16, 16, 384],
                   [384],
                   [384, 384, 384, 384], 
                   [16, 16, 16, 384],
                   [384],
                   [384, 384, 384, 384], 
                   [16, 16, 16, 384],
                   [384],
                   [384, 384, 384, 384], 
                   [16, 16, 16, 384],
                   [384],
                   [384, 384, 384, 384], 
                   [16, 16, 16, 384],
                   [384],
                   [512],
                   [512, 512, 512, 512], 
                   [16, 16, 16, 512],
                   [512],
                   [512, 512, 512, 512], 
                   [16, 16, 16, 512],
                   [512],
                   [384],
                   [384, 384, 384, 384], 
                   [16, 16, 16, 384],
                   [384],
                   [192],
                   [192, 192, 192, 192],
                   [16, 16, 16, 192],
                   [192],
                   [96],
                   [96, 96, 96, 96],
                   [16, 16, 16, 96],
                   [96], 
                   [48],
                   [48, 48, 48, 48], 
                   [8, 8, 8, 48], 
                   [48],
                   [19]
                   ]  
NN_NUM_CHN_IN   = [[4],
                   [48, 48, 48, 48], 
                   [48, 8, 8, 8], 
                   [48],
                   [48],
                   [96, 96, 96, 96], 
                   [96, 16, 16, 16],
                   [96],
                   [96, 96, 96, 96], 
                   [96, 16, 16, 16],
                   [96],
                   [96],  
                   [192, 192, 192, 192], 
                   [192, 16, 16, 16],
                   [192],
                   [192, 192, 192, 192], 
                   [192, 16, 16, 16],
                   [192],
                   [192],
                   [384, 384, 384, 384], 
                   [384, 16, 16, 16],
                   [384],
                   [384, 384, 384, 384], 
                   [384, 16, 16, 16],
                   [384],
                   [384, 384, 384, 384], 
                   [384, 16, 16, 16],
                   [384],
                   [384, 384, 384, 384], 
                   [384, 16, 16, 16],
                   [384],
                   [384, 384, 384, 384], 
                   [384, 16, 16, 16],
                   [384],
                   [384, 384, 384, 384], 
                   [384, 16, 16, 16],
                   [384],
                   [384],
                   [512, 512, 512, 512], 
                   [512, 16, 16, 16],
                   [512],
                   [512, 512, 512, 512], 
                   [512, 16, 16, 16],
                   [512],
                   [512],
                   [384, 384, 384, 384], 
                   [384, 16, 16, 16],
                   [384],
                   [384],
                   [192, 192, 192, 192], 
                   [192, 16, 16, 16],
                   [192],
                   [192],
                   [96, 96, 96, 96], 
                   [96, 16, 16, 16],
                   [96],
                   [96],
                   [48, 48, 48, 48], 
                   [48, 8, 8, 8], 
                   [48],
                   [48]
                   ]


NN_REAL_GOP  = 0.77
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
   LOCAL_ATT_STG = [2,6,9,13,16,20,23,26,29,32,35,39,42,46,50,54,58]

   from collections import defaultdict
   REPEAT_STG = defaultdict(lambda: 1, {2:131072/INPUT_SCALE, 6:32768/INPUT_SCALE, 9:32768/INPUT_SCALE, 13:8192/INPUT_SCALE, 16:8192/INPUT_SCALE, 20:2048/INPUT_SCALE, 23:2048/INPUT_SCALE, 26:2048/INPUT_SCALE, 29:2048/INPUT_SCALE, 32:2048/INPUT_SCALE, 35:2048/INPUT_SCALE, 39:512/INPUT_SCALE, 42:512/INPUT_SCALE, 46:2048/INPUT_SCALE, 50:8192/INPUT_SCALE, 54:32768/INPUT_SCALE, 58:131072/INPUT_SCALE}) 
   Heads = 8

