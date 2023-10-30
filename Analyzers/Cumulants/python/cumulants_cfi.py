import FWCore.ParameterSet.Config as cms

defaultCumu = cms.EDAnalyzer('Cumulants', #Analyzer named: Correspond to the class name in 'plugin' folder
                             #Track collection
                             tracks = cms.InputTag("packedPFCandidates"),
                             tracksgen = cms.InputTag("packedGenParticles"),
                             trackschi2 = cms.InputTag("packedPFCandidateTrackChi2"),
                             vertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
                             centralitybin = cms.InputTag("centralityBin", "HFtowers"),
                             qualityString = cms.string("highPurity"),
                             eventPlane = cms.InputTag("hiEvtPlaneFlat"),
                             minvz         = cms.untracked.double(-15.0), 
                             maxvz         = cms.untracked.double(15.0),
                             maxrho        = cms.untracked.double(0.2),
                             isBVselByMult = cms.untracked.bool(True),
                             #Multiplicity selection
                             centmin       = cms.untracked.int32(0),  
                             centmax       = cms.untracked.int32(100),
                             noffmin       = cms.untracked.int32(10),
                             noffmax       = cms.untracked.int32(4000),
                             ptnoffmin     = cms.untracked.double(0.4),
                             ptnoffmax     = cms.untracked.double(10000.0),
                             dzdzerrornoff = cms.untracked.double(3.0),
                             d0d0errornoff = cms.untracked.double(3.0),
                             pterrorptnoff = cms.untracked.double(0.1),
                             #Track selection
                             etamin    = cms.untracked.double(-2.4),
                             etamax    = cms.untracked.double(2.4),
                             ptmin     = cms.untracked.double(0.5),
                             ptmax     = cms.untracked.double(3.0),
                             dzdzerror = cms.untracked.double(3.0),
                             d0d0error = cms.untracked.double(3.0),
                             pterrorpt = cms.untracked.double(0.1),
                             #Acc X Eff
                             cweight    = cms.untracked.bool(False),
                             fname = cms.untracked.InputTag('EffCorrectionsPixelPbPb2018_v1.root'),
                             #fname = cms.untracked.InputTag('Hijing_8TeV_MB_eff_v3_tight.root'),
                             #fname = cms.untracked.InputTag('Hijing_8TeV_MB_eff_v3_loose.root'),
                             #fname = cms.untracked.InputTag('Hijing_8TeV_MB_eff_v4_narrow.root'),
                             #fname = cms.untracked.InputTag('Hijing_8TeV_MB_eff_v4_wide.root'),
                             effmultbin = cms.untracked.vint32(0,10,20,60,100,200),
                             fpt = cms.untracked.InputTag("2018PbPb_Efficiency_GeneralTracks_highPt.root"),
                             fpix = cms.untracked.InputTag("2018PbPb_Efficiency_PixelTracks.root"),
                             fmb = cms.untracked.InputTag("2018PbPb_Efficiency_GeneralTracks_MB.root"),
                             fplus = cms.untracked.InputTag("2018PbPb_Efficiency_GeneralTracks_MB_ChargePlus.root"),
                             fminus = cms.untracked.InputTag("2018PbPb_Efficiency_GeneralTracks_MB_ChargeMinus.root")

)
#process.QWVetoJet20 = cms.EDFilter('QWJetPtFilter',
 #       src = cms.untracked.InputTag('akPu4PFJets'),
  #      dmin = cms.untracked.double(0.),
   #     dmax = cms.untracked.double(20.),
    #    )
