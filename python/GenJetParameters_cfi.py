import FWCore.ParameterSet.Config as cms

# Standard CalooJets parameters
# $Id: GenJetParameters_cfi.py,v 1.3 2008/08/20 15:51:08 oehler Exp $
GenJetParameters = cms.PSet(
    src = cms.InputTag("genParticlesForJets"),
    verbose = cms.untracked.bool(False),
    jetPtMin = cms.double(5.0),
    inputEtMin = cms.double(0.0),
    jetType = cms.untracked.string('GenJet'),
    inputEMin = cms.double(0.0)
)

