import FWCore.ParameterSet.Config as cms

process = cms.Process("JETRECO")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

# input
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
'/store/relval/CMSSW_3_11_0_pre5/RelValTTbar/GEN-SIM-RECO/START311_V0-v1/0063/08A4DD4C-E223-E011-A7E1-002354EF3BE0.root',
'/store/relval/CMSSW_3_11_0_pre5/RelValTTbar/GEN-SIM-RECO/START311_V0-v1/0063/58EB762D-DB23-E011-8A24-001A92971B94.root',
'/store/relval/CMSSW_3_11_0_pre5/RelValTTbar/GEN-SIM-RECO/START311_V0-v1/0063/5A86074E-DD23-E011-8027-001A92971B94.root',
'/store/relval/CMSSW_3_11_0_pre5/RelValTTbar/GEN-SIM-RECO/START311_V0-v1/0063/7436AFAB-DB23-E011-8A03-002618943927.root',

        )
    )

# output
process.load('Configuration/EventContent/EventContent_cff')
process.output = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = process.RECOSIMEventContent.outputCommands,
    fileName = cms.untracked.string('testJetReco.root')
)
process.output.outputCommands =  cms.untracked.vstring('drop *')
process.output.outputCommands.append('keep recoCaloJets_*_*_*')
process.output.outputCommands.append('keep recoPFJets_*_*_*')
process.output.outputCommands.append('keep recoPFClusterJets_*_*_*')
process.output.outputCommands.append('keep recoGenJets_*_*_*')
process.output.outputCommands.append('keep recoBasicJets_*_*_*')
process.output.outputCommands.append('keep *_*_*_JETRECO')
process.output.outputCommands.append('keep *_trackRefsForJets_*_*')
process.output.outputCommands.append('keep *_pfclusterRefsForJets_*_*')
process.output.outputCommands.append('keep *_generalTracks_*_*')

# jet reconstruction
process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'MC_311_V0::All'


from RecoJets.JetProducers.CaloJetParameters_cfi import *
#CaloJetParameters.doAreaFastjet = True
from RecoJets.JetProducers.PFJetParameters_cfi import *
#PFJetParameters.doAreaFastjet = True

process.load('RecoJets.Configuration.GenJetParticles_cff')
process.load('RecoJets.Configuration.RecoGenJets_cff')
process.load('RecoJets.Configuration.RecoJets_cff')
process.load('RecoJets.Configuration.RecoPFJets_cff')
process.load('RecoJets.Configuration.RecoPFClusterJets_cff')
process.load('RecoJets.JetProducers.TracksForJets_cff')
process.load('RecoJets.Configuration.RecoTrackJets_cff')
process.load('RecoJets.Configuration.JetIDProducers_cff')

#process.kt6PFJets.doRhoFastjet = True;
#process.kt6CaloJets.doRhoFastjet = True;
#process.kt6TrackJets.doRhoFastjet = True;
#process.kt6GenJets.doRhoFastjet = True;

process.recoJets = cms.Path(process.genParticlesForJets+process.recoGenJets+
                            process.recoJets+
                            process.recoPFJets+
                            process.recoPFClusterJets+
                            process.recoTrackJets+
                            process.recoJetIds
                            )

process.recoAllJets = cms.Path(process.genParticlesForJets+process.recoAllGenJets+
                               process.recoAllJets+
                               process.recoAllPFJets+
                               process.recoAllPFClusterJets+
                               process.recoAllTrackJets+
                               process.recoAllJetIds
                               )

process.recoAllJetsPUOffsetCorr = cms.Path(process.recoAllJetsPUOffsetCorr
                                           )

process.out = cms.EndPath(process.output)

# schedule
process.schedule = cms.Schedule(process.recoAllJets,process.out)

# Set the threshold for output logging to 'info'
process.MessageLogger.cerr.threshold = cms.untracked.string('INFO')
#process.MessageLogger.cerr.threshold = cms.untracked.string('DEBUG')
#process.MessageLogger.cout.threshold = cms.untracked.string('DEBUG')
#process.MessageLogger.debugModules = cms.untracked.vstring('*')
