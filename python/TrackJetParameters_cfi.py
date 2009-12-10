import FWCore.ParameterSet.Config as cms

TrackJetParameters = cms.PSet(
    src            = cms.InputTag('trackRefsForJets'),
    srcPVs         = cms.InputTag('offlinePrimaryVertices'),
    jetType        = cms.string('TrackJet'),
    jetPtMin       = cms.double(0.3),
    inputEMin      = cms.double(0.0),
    inputEtMin     = cms.double(0.0),
    doPVCorrection = cms.bool(False), # not used
    doPUOffsetCorr = cms.bool(False), # not used
    doPUFastjet    = cms.bool(False), # not used
    # only use the tracks that were used to fit the vertex
    UseOnlyVertexTracks = cms.bool(False),
    # only consider the highest-sum-pT PV for clustering
    UseOnlyOnePV        = cms.bool(True),
    # maximum z-distance bweteen track and vertex for association (in cm)
    DzTrVtxMax          = cms.double(0.5)
)
