import math

# ################################################################################
# BITWIDTH
# ################################################################################

REF_BITWIDTH = 8
BITWIDTH = 8
BITWIDTH_RATE = REF_BITWIDTH / BITWIDTH

# ################################################################################
# HW
# ################################################################################

NUM_INF  = 1

# FPS
FPS_CORE = 16

# KNN
KNN_CORE = 8

# PE
PE_BANK_ROW = 2 * BITWIDTH_RATE
PE_BANK_COL = 2 * BITWIDTH_RATE
PE_BANK = PE_BANK_COL * PE_BANK_ROW
PE_ROW  = 16
PE_COL  = 16

# POL
POL_CORE = 8
POL_COMP_CORE = 32

# GB- 512KB = 128*128*32
GLB_NUMSRAM = 128 * BITWIDTH_RATE
GLB_DEPSRAM = 128
GLB_NUMDATA = 32 # Actually, Number of Data, whatever the bitwidth is
GLB_WORD    = GLB_DEPSRAM*GLB_NUMSRAM

NUMCORDPERWORD = math.floor(256/24)
NUMDISTPERWORD = 256/16
NUMPIDXWORD  = 256/16
NUMFILROWWORD = GLB_NUMDATA / (PE_COL*PE_BANK_COL) # 2X1 PE ARRAY : 2


# ################################################################################
# CONSUMPTION OF POWER
# ################################################################################


# Reference Design is PointCloudAcc
VOLTAGE_28NM        = 0.94
TECH_28NM           = 28
AREA_28NM           = 1.5
SYA_AREA_28NM       = 0.3 # 512 PE
GLB_AREA_28NM       = 0.2 # 64KB
FREQ_28NM           = 200
Energy_1bit_EMA     = 5.68*(10**-9)
CURRENT_STATIC_28NM = VOLTAGE_28NM/0.713*35
POWER_STC_28NM      = VOLTAGE_28NM*CURRENT_STATIC_28NM
POWER_FPS_28NM      = VOLTAGE_28NM*VOLTAGE_28NM/0.713*(38       - 35)
POWER_KNN_28NM      = VOLTAGE_28NM*VOLTAGE_28NM/0.713*(40.88    - 35)
POWER_SYA_28NM      = VOLTAGE_28NM*VOLTAGE_28NM/0.713*(76       - 35)
POWER_POL_28NM      = VOLTAGE_28NM*VOLTAGE_28NM/0.713*(43.53    - 35)
POWER_GLB_28NM      = VOLTAGE_28NM*VOLTAGE_28NM/0.713*0


TECH        = 16 # 28 nm
SYA_AREA    = 4 # synthesis area, 1024 IN8 (mixed precision)
AREA        = (AREA_28NM - SYA_AREA_28NM + GLB_AREA_28NM*(GLB_NUMSRAM/16 -1) )/((TECH_28NM/TECH)**2) + SYA_AREA
FREQ        = 1000
VOLTAGE     = ( ( (0.8 if FREQ > 1000 else 0.75) if FREQ >= 800 else 0.7) if FREQ >= 300 else 0.65) if FREQ > 100 else 0.6  # V, TSMC 16nm, std voltage

POWER_BASIC = POWER_STC_28NM*1             *AREA/AREA_28NM*(VOLTAGE/VOLTAGE_28NM)**2# from 0.9V to 0.713V; 100 MHz; For 200 MHz, Power Transfer according SYA -> *(0.94V*181.47mA)/(0.713V*76mA) Refer to ISSCC_Nebula_Statis.xlsx
POWER_FPS   = POWER_FPS_28NM*FREQ/FREQ_28NM*AREA/AREA_28NM*(VOLTAGE/VOLTAGE_28NM)**2                                                 * ((1/BITWIDTH_RATE)**2)          
POWER_KNN   = POWER_KNN_28NM*FREQ/FREQ_28NM*AREA/AREA_28NM*(VOLTAGE/VOLTAGE_28NM)**2                                                 * ((1/BITWIDTH_RATE)**2)                   
POWER_SYA   = POWER_SYA_28NM*FREQ/FREQ_28NM*AREA/AREA_28NM*(VOLTAGE/VOLTAGE_28NM)**2 * (SYA_AREA*(TECH_28NM/TECH)**2)/SYA_AREA_28NM  * ((1/BITWIDTH_RATE)**2)   
POWER_POL   = POWER_POL_28NM*FREQ/FREQ_28NM*AREA/AREA_28NM*(VOLTAGE/VOLTAGE_28NM)**2                                                 * ((1/BITWIDTH_RATE)**2)               
POWER_GLB   = POWER_GLB_28NM*FREQ/FREQ_28NM*AREA/AREA_28NM*(VOLTAGE/VOLTAGE_28NM)**2 * GLB_NUMSRAM/16                                * ((1/BITWIDTH_RATE)**2)                  



# ################################################################################
# RUN-SWITCH OF INNOVATIVE SKILLS
# ################################################################################

ENA_ABS = True  # Adaptive Block-wise Sampling
ENA_SBS = True # Sampling-based Skipping
ENA_BDA = True # Block-wise Delay Aggregation
ENA_CNS = True  # When CNC, Skipping (ITP_RATE -1) Conv
ENA_MLF = True # MLP Fusion


# ################################################################################
# RUN-SWITCH OF RUN-TIME PROCESS CONTROL
# ################################################################################

ENA_AHEAD   = True # Enable constraint ahead, e.g., KNN ahead SYA < 2
ENA_PREDICT = False


AHEAD_FPSSYA_STG = 1
AHEAD_KNNSYA_STG = 1
AHEAD_SYAPOL_BLK = 4
AHEAD_POLRES_BLK = 4
AHEAD_RESSYA_BLK = 4 # Not Block
AHEAD_CNCSYA_BLK = 1


# #######################################################################
# SIMULATE REAL-WORLD SCENARIOS
# #######################################################################
ENA_RELY    = True # Enable rely between modules, POL <- KNN <- FPS <- Previous FPS
ENA_CAP     = True # Enable constraint of GLB_CapFull

# PRE-START
FRE_RATIO   = 4 * BITWIDTH_RATE # OFF-CHIP / ON-CHIP: 1: 32B=256b
ITFPRE      = 10 # 5 On-chip + 10 Off-chip
SYAPRE      = 5  # PE_ROW*PE_BANK

# ULTIRATIO
FPSUTI     = 0.2 # 1/5; utilization 
KNNUTI     = 0.1 # 1/10
SYAUTI     = 1
POLUTI     = 1
RESUTI     = 1
CNCUTI     = 1

TH_ITFACT   = 1


# #############################################################
# STAT
# #############################################################
NUMCLK      = 800000000 if not ENA_ABS else 800000000
ITFACT_STAT_PERIOD = 100
NUMSTAT     = 149




# #############################################################
# OPTIMIZE THE SPEED OF MODEL
# #############################################################
STAT_ACTRATIO = True # Enable to stat
SWITCH_TIME = False
VERBOSE = False # swich of print


STPPRT      = 1000 # Step Of Print 
GLBEMPTYCLK = 100 # increasing the time step in GLB
STAT_APPEND_SRIDE = 5000 # control printing's time step
GLBCap_Step =5000
Cnt_Step = 100



# #############################################################
# LOCAL_ATTENTION
# #############################################################

LOCAL_ATTENTION = True
LA_USE_MULT = True

