import FWCore.ParameterSet.Config as cms

from SimGeneral.HepPDTESSource.pythiapdt_cfi import *

#
# MODULES
#

# track selection, could eventually be merged into PhysicsTools/RecoAlgos/python/TrackWithVertexRefSelector_cfi.py
trackWithVertexRefSelector = cms.EDFilter("TrackWithVertexRefSelector",
    # the track collection
    src = cms.InputTag('generalTracks'),
    # kinematic cuts  (pT in GeV)
    etaMin = cms.double(0.0),
    etaMax = cms.double(5.0),
    ptMin = cms.double(0.0),
    ptMax = cms.double(500.0),
    # impact parameter cut (in cm)
    d0Max = cms.double(10.0),
    dzMax = cms.double(35.0),
    # quality cuts (valid hits, normalized chi2)
    normalizedChi2 = cms.double(100.0),
    numberOfValidHits = cms.uint32(8),
    numberOfLostHits = cms.uint32(999), ## at most 999 lost hits
    numberOfValidPixelHits = cms.uint32(0), ## at least <n> hits inthe pixeles
    # compatibility with a vertex ?
    useVtx = cms.bool(True),
    vertexTag = cms.InputTag('offlinePrimaryVertices'),
    nVertices = cms.uint32(2), ## how many vertices to look at before dropping the track
    vtxFallback = cms.bool(True), ## falback to beam spot if there are no vertices
    # uses vtx=(0,0,0) with deltaZeta=15.9, deltaRho = 0.2
    zetaVtx = cms.double(1.0),
    rhoVtx = cms.double(0.3), ## tags used by b-tagging folks
    # should _not_ be used for the TrackWithVertexRefSelector
    copyExtras = cms.untracked.bool(False), ## copies also extras and rechits on RECO
    copyTrajectories = cms.untracked.bool(False), # don't set this to true on AOD!
)


tracksForJets = cms.EDProducer("ChargedCandidateProducer",
    src          = cms.InputTag('trackWithVertexRefSelector'),
    particleType = cms.string('pi+')
)


trackRefsForJets = cms.EDProducer("ChargedRefCandidateProducer",
    src          = cms.InputTag('trackWithVertexRefSelector'),
    particleType = cms.string('pi+')
)
