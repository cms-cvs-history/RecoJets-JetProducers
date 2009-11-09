import FWCore.ParameterSet.Config as cms

process = cms.Process("JETRECO")

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

# input
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/042/3EE31BC1-FECC-DE11-9FC2-001617C3B79A.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/041/B6B6AC8F-D6CC-DE11-AE87-001617DBD556.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/040/223AEAD9-B4CC-DE11-9A6A-0030487A18A4.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/037/D4B435D4-79CC-DE11-AD5E-000423D94534.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/026/0A048478-7FCC-DE11-8B8E-0030487A18F2.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/025/CCE960AF-69CC-DE11-B39F-001D09F253FC.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/024/906A6419-58CC-DE11-8E12-001617E30D12.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/022/D0B84DC6-51CC-DE11-9BC4-001617C3B76E.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/020/D81D3B2C-5FCC-DE11-8BE5-0030487A322E.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/020/CA2733D8-5FCC-DE11-865B-000423D94C68.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/018/8CFB9DA2-08CC-DE11-9E55-001617C3B6FE.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/015/3EDA5631-80CC-DE11-A980-0030487A3C9A.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/120/013/D6DFB876-D7CB-DE11-A431-000423D98930.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/994/A09304DB-D1CB-DE11-8BC1-001D09F24F1F.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/986/88A8D905-99CB-DE11-86C0-001617DBCF6A.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/972/760E72AB-ACCB-DE11-A3A6-001D09F2437B.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/971/1A8CDD9B-2ACB-DE11-9582-001617E30CC8.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/970/5C4D9438-29CB-DE11-89F8-0030487A1FEC.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/967/40DE37DD-1BCB-DE11-8FA8-000423D99658.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/959/107203C1-12CB-DE11-AEBD-00304879FA4A.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/950/08DA9B50-03CB-DE11-BBF1-00304879FBB2.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/939/9462B412-F6CA-DE11-B1A5-001D09F241F0.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/924/B0DC6D54-0ACB-DE11-BFC9-000423D99614.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/919/AA8C6703-EACA-DE11-8B13-001D09F24493.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/911/42EAA26E-0CCB-DE11-8537-000423D944FC.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/901/7A55A840-E2CA-DE11-A3AB-001D09F297EF.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/894/787854DB-06CB-DE11-A08D-001D09F295FB.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/889/F0C397EA-FACA-DE11-88BB-001D09F2532F.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/846/DA5DED39-4ACB-DE11-B1F0-000423D99AA2.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/833/A209F925-C6CA-DE11-BBC1-0016177CA778.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/824/22DA6C64-C3CA-DE11-8452-0019B9F72BAA.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/794/F0CF6AA6-56CA-DE11-BB61-000423D6CA6E.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/695/B0AFA546-63CA-DE11-860D-001D09F24934.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/695/7EB4B4FF-63CA-DE11-ADA2-001D09F24FBA.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/695/4CB9B69F-62CA-DE11-B689-003048D37580.root',
       '/store/data/BeamCommissioning09/BeamHalo/RECO/v1/000/119/665/2CC53997-1FCA-DE11-A5DE-000423D94A20.root'
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
process.output.outputCommands.append('keep recoGenJets_*_*_*')
process.output.outputCommands.append('keep recoBasicJets_*_*_*')
process.output.outputCommands.append('keep *_*_*_JETRECO')


# jet reconstruction
process.load('Configuration.StandardSequences.Geometry_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')

process.load('RecoJets.Configuration.GenJetParticles_cff')
process.load('RecoJets.Configuration.RecoGenJets_cff')
process.load('RecoJets.Configuration.RecoJets_cff')
process.load('RecoJets.Configuration.RecoPFJets_cff')
process.load('RecoJets.JetProducers.TracksForJets_cff')
process.load('RecoJets.Configuration.RecoTrackJets_cff')
process.load('RecoJets.Configuration.JetIDProducers_cff')

process.recoJetsSplash = cms.Path(process.ak5CaloJets+
                                  process.iterativeCone5CaloJets
                                  )


process.out = cms.EndPath(process.output)

# schedule
process.schedule = cms.Schedule(process.recoJetsSplash,
                                process.out)

# Set the threshold for output logging to 'info'
process.MessageLogger.cerr.FwkReport.reportEvery = 100
#process.MessageLogger.cerr.threshold = cms.untracked.string('INFO')
#process.MessageLogger.cerr.threshold = cms.untracked.string('DEBUG')
#process.MessageLogger.cout.threshold = cms.untracked.string('DEBUG')
#process.MessageLogger.debugModules = cms.untracked.vstring('*')
