from CRABAPI.RawCommand import crabCommand
from CRABClient.UserUtilities import config #,                                                                                                                                                                                              
from CRABClient.ClientExceptions import ClientException
config = config()                                                                          
###General: In this section, the user specifies generic parameters about the request (e.g. request name).
config.General.workArea     = 'Cumulant_2023' ###fixed name for projects dir in my area
config.General.transferLogs = True 
config.General.transferOutputs = True
config.JobType.pluginName     = 'Analysis'
config.JobType.psetName       = '../cfg/PbPb_2023_vn_cfg.py'
config.Data.unitsPerJob       = 20
config.Data.totalUnits        = -1
config.JobType.maxMemoryMB = 4000
config.Data.splitting         = 'LumiBased'
config.JobType.inputFiles = ['CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_374289.db']
config.Data.inputDBS          = 'global'
config.Data.publication = False
config.Data.outLFNDirBase            = '/store/group/phys_heavyions/rosingh/PbPb_2023_UCC_vn'
config.Site.storageSite       = 'T2_CH_CERN'
        
config.General.requestName  = 'Cumulant_HiRaw6_UCC_vn_miniaod_0p5_3'        
config.Data.inputDataset = '/HIPhysicsRawPrime6/HIRun2023A-PromptReco-v2/MINIAOD'
config.Data.outputDatasetTag = 'Cumulant_HiRaw6_UCC_vn_miniaod_0p5_3' ###change for each sample(task) --only if publish
config.Data.lumiMask = 'Golden_Online_live.json'



