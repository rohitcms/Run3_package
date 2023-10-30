import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_pp_on_PbPb_2023_cff import Run3_pp_on_PbPb_2023 
process = cms.Process("Cumulants")
#process.load('RecoVertex.PrimaryVertexProducer.OfflinePrimaryVerticesRecovery_cfi')
process.load('Configuration.Geometry.GeometryDB_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')

# __________________ General _________________

# Configure the logger
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True ),
)

# Configure the number of maximum event the analyser run on in interactive mode
# -1 == ALL
process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(5000) 
#    input = cms.untracked.int32(500) 
)

#rootFiles = open("/eos/cms/store/group/phys_heavyions/sayan/TrackingTools_run3_datataking/pbpb_miniaod_datasets/run374810_ls0001_ls1752_streamPhysicsHIPhysicsRawPrime0_miniaod.txt", "r").readlines()
process.source = cms.Source("PoolSource",                                                                                
 #   duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),                                                       
    fileNames = cms.untracked.vstring(                                                                                   
#        'file:/eos/cms/store/group/phys_heavyions/wangj/RECO2023/miniaod_PhysicsHIPhysicsRawPrime0_374810/reco_run374810_ls0210_streamPhysicsHIPhysicsRawPrime0_StorageManager.root'
#       '/store/hidata/HIRun2023A/HIPhysicsRawPrime3/MINIAOD/PromptReco-v1/000/373/870/00000/6f2a145d-d79c-40d5-909d-174d860bde96.root'
#        '/store/hidata/HIRun2023A/HIMinimumBias0/MINIAOD/PromptReco-v1/000/373/870/00000/27122bd1-d3bf-4528-804d-013fd2fd7474.root'
'/store/hidata/HIRun2023A/HIPhysicsRawPrime0/MINIAOD/PromptReco-v2/000/374/668/00000/1bb772f3-bfa5-46ef-81d2-8cf78de992b0.root'
#        rootFiles
    ),                                                                                                                   
)                                                                                                                        

#process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
# Set the global tag
from Configuration.AlCa.GlobalTag import GlobalTag                                                                       
process.GlobalTag = GlobalTag(process.GlobalTag, '132X_dataRun3_Express_v4', '')                                         
#process.HiForestInfo.GlobalTagLabel = process.GlobalTag.globaltag                                                       
                                                                                                                         
process.GlobalTag.snapshotTime = cms.string("9999-12-31 23:59:59.000")                                                   
process.GlobalTag.toGet.extend([                                                                                         
    cms.PSet(record = cms.string("HeavyIonRcd"),                                                                         
        tag = cms.string("CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_374289"),            
        connect = cms.string("sqlite_file:CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run3v1302x04_offline_374289.db"),                                                                                                                 
        label = cms.untracked.string("HFtowers")                                                                         
        ),           
    ])                                                                                                                   
                                                                                                                         
process.load("RecoHI.HiCentralityAlgos.CentralityBin_cfi")                                                               
process.centralityBin.Centrality = cms.InputTag("hiCentrality")                                                          
process.centralityBin.centralityVariable = cms.string("HFtowers")                                                        
# __________________ Event selection _________________
# Add PbPb collision event selection 
#process.load('HeavyIonsAnalysis.EventAnalysis.skimanalysis_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.collisionEventSelection_cff')
process.load('HeavyIonsAnalysis.TrackAnalysis.TrackAnalyzer_cfi')
process.load('HeavyIonsAnalysis.EventAnalysis.hffilter_cfi')

#process.ana_step = cms.Path(process.offlinePrimaryVerticesRecovery + process.HiForest)
# Define the event selection sequence
process.eventFilter_HM = cms.Sequence(
    process.phfCoincFilter2Th4 *
#    process.phfCoincFilter3Th3 *
    process.primaryVertexFilter *
    process.clusterCompatibilityFilter
)
import FWCore.PythonUtilities.LumiList as LumiList
process.source.lumisToProcess = LumiList.LumiList(filename = '/eos/cms/store/group/phys_heavyions/sayan/HIN_run3_pseudo_JSON/HIPhysicsRawPrime/Golden_Online_live.json').getVLuminosityBlockRange()
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel  
process.hltfilter = hltHighLevel.clone(                         
    HLTPaths = [                                                
       # "HLT_HIMinimumBiasHF1ANDZDC1nOR_v*",
"HLT_HIMinimumBiasHF1AND*"
        #"HLT_HIMinimumBiasHF1AND_v*"
#        "HLT_HIL1_UCC_0_1_v3"

    ]                                                           
)                                                               
# Define the output
process.TFileService = cms.Service("TFileService",fileName = cms.string('pbpb_2023_vn_UCC_test.root'))
process.load("Analyzers.Cumulants.cumulants_cfi")
process.std = process.defaultCumu.clone()


#process.load('MergingProducer.generalAndHiPixelTracks.MergingPixAndGenProducer_cfi')

#from HLTrigger.Configuration.CustomConfigs import MassReplaceInputTag
#process = MassReplaceInputTag(process,"offlinePrimaryVertices","offlinePrimaryVerticesRecovery")
#process.offlinePrimaryVerticesRecovery.oldVertexLabel = "offlinePrimaryVertices"
process.p = cms.Path(#process.generalAndHiPixelTracks * 
                     process.eventFilter_HM *
                     process.hltfilter *
   process.centralityBin*
    process.std
#                     process.generalAndHiPixelTracks *
                  #   process.centralityBin*
                   
)
                   
