// File: BaseJetProducer.cc
// Author: F.Ratnikov UMd Aug 22, 2006
// $Id: BaseJetProducer.cc,v 1.20 2007/05/30 22:30:45 fedor Exp $
//--------------------------------------------
#include <memory>

#include "DataFormats/Common/interface/EDProduct.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/View.h"
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Provenance/interface/ProductID.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/JetReco/interface/CaloJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/BasicJet.h"
#include "DataFormats/JetReco/interface/GenericJet.h"
#include "DataFormats/JetReco/interface/JetTrackMatch.h"
#include "RecoJets/JetAlgorithms/interface/JetTrackConeAssociator.h"
#include "RecoJets/JetAlgorithms/interface/JetMaker.h"
#include "RecoJets/JetAlgorithms/interface/JetAlgoHelper.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "Geometry/CaloGeometry/interface/CaloGeometry.h"
#include "Geometry/Records/interface/IdealGeometryRecord.h"

#include "RecoJets/JetProducers/interface/BaseJetProducer.h"

using namespace std;
using namespace reco;
using namespace JetReco;

namespace {
  const bool debug = false;

  bool makeCaloJet (const string& fTag) {
    return fTag == "CaloJet";
  }
  bool makePFJet (const string& fTag) {
    return fTag == "PFJet";
  }
  bool makeGenJet (const string& fTag) {
    return fTag == "GenJet";
  }
  bool makeBasicJet (const string& fTag) {
    return fTag == "BasicJet";
  }

  bool makeGenericJet (const string& fTag) {
    return !makeCaloJet (fTag) && !makePFJet (fTag) && !makeGenJet (fTag) && !makeBasicJet (fTag);
  }

  template <class T>  
  void dumpJets (const T& fJets) {
    for (unsigned i = 0; i < fJets.size(); ++i) {
      std::cout << "Jet # " << i << std::endl << fJets[i].print();
    }
  }

  class FakeHandle {
  public:
    FakeHandle (const CandidateCollection* fCollection, edm::ProductID fId) : mCollection (fCollection), mId (fId) {}
    edm::ProductID id () const {return mId;} 
    const CandidateCollection* product () const {return mCollection;}
  private:
    const CandidateCollection* mCollection;
    edm::ProductID mId;
  };

  template <class HandleC>
  void fillInputs (const HandleC& fData, JetReco::InputCollection* fInput, double fEtCut, double fECut) {
    for (unsigned i = 0; i < fData.product ()->size (); i++) {
      // if clone, trace back till the original
      CandidateRef constituent (fData, i);
      while (constituent.isNonnull() && constituent->hasMasterClone ()) {
	CandidateBaseRef baseRef = constituent->masterClone ();
	constituent = baseRef.castTo<CandidateRef>();
      }
      if (constituent.isNull()) {
	edm::LogWarning("Missing MasterClone") << "Constituent is ignored..." << std::endl;
      }
      else if ((fEtCut <= 0 || constituent->et() > fEtCut) &&
	  (fECut <= 0 || constituent->energy() > fECut)) {
	fInput->push_back (constituent);
      }
    }
  }
}

namespace cms
{

  // Constructor takes input parameters now: to be replaced with parameter set.
  BaseJetProducer::BaseJetProducer(const edm::ParameterSet& conf)
    : mSrc(conf.getParameter<edm::InputTag>( "src" )),
      mJetType (conf.getUntrackedParameter<string>( "jetType", "CaloJet")),
      mVerbose (conf.getUntrackedParameter<bool>("verbose", false)),
      mEtInputCut (conf.getParameter<double>("inputEtMin")),
      mEInputCut (conf.getParameter<double>("inputEMin")),
      //      mVertexTracksCone (conf.getParameter<double>("vertexTracksCone"))
      mVertexTracksCone (0)
  {
    std::string alias = conf.getUntrackedParameter<string>( "alias", conf.getParameter<std::string>("@module_label"));
    if (makeCaloJet (mJetType)) {
      produces<CaloJetCollection>().setBranchAlias (alias);
      if (mVertexTracksCone > 0) produces<JetTrackMatch<CaloJetCollection> > ();
    }
    else if (makePFJet (mJetType)) produces<PFJetCollection>().setBranchAlias (alias);
    else if (makeGenJet (mJetType)) produces<GenJetCollection>().setBranchAlias (alias);
    else if (makeBasicJet (mJetType)) produces<BasicJetCollection>().setBranchAlias (alias);
    else if (makeGenericJet (mJetType)) produces<GenericJetCollection>().setBranchAlias (alias);
  }

  // Virtual destructor needed.
  BaseJetProducer::~BaseJetProducer() { } 

  // Functions that gets called by framework every event
  void BaseJetProducer::produce(edm::Event& e, const edm::EventSetup& fSetup)
  {
    const CaloSubdetectorGeometry* towerGeometry = 0; // cache geometry
    // get input
    InputCollection input;
    CandidateCollection inputCache;
    if (makeGenericJet (mJetType)) {
      edm::Handle<edm::View <Candidate> > genericInputs; 
      e.getByLabel( mSrc, genericInputs ); 
      for (unsigned i = 0; i < genericInputs->size (); ++i) {
	const Candidate* ref = &((*genericInputs)[i]);
	Candidate* c = new LeafCandidate (ref->charge (), ref->p4 (), ref->vertex ());
	inputCache.push_back (c);
      }
      FakeHandle handle (&inputCache, genericInputs.id ());
      fillInputs (handle, &input, mEtInputCut, mEInputCut);
    }
    else { // CandidateCollection
      edm::Handle<CandidateCollection> concreteInputs;
      e.getByLabel( mSrc, concreteInputs );
      fillInputs (concreteInputs, &input, mEtInputCut, mEInputCut);
    }

    if (mVerbose) {
      std::cout << "BaseJetProducer::produce-> INPUT COLLECTION selected from" << mSrc 
		<< " with ET > " << mEtInputCut << " and/or E > " << mEInputCut << std::endl;
      int index = 0;
      for (InputCollection::const_iterator constituent = input.begin();
       constituent != input.end(); ++constituent, ++index) {
	std::cout << "  Input " << index << ", px/py/pz/pt/e: "
		  << (*constituent)->px() << '/' << (*constituent)->py() << '/' << (*constituent)->pz() << '/' 
		  << (*constituent)->pt() << '/' << (*constituent)->energy()
 		  << std::endl;
      }
    }

    // run algorithm
    vector <ProtoJet> output;
    if (input.empty ()) {
      edm::LogInfo ("Empty Event") << "empty input for jet algorithm: bypassing..." << std::endl;
    }
    else {
      runAlgorithm (input, &output);
    }

    // produce output collection
    auto_ptr<CaloJetCollection> caloJets;
    auto_ptr<PFJetCollection> pfJets;
    auto_ptr<GenJetCollection> genJets;
    auto_ptr<BasicJetCollection> basicJets;
    auto_ptr<GenericJetCollection> genericJets;
    if (makeCaloJet (mJetType)) caloJets.reset (new CaloJetCollection);
    else if (makePFJet (mJetType)) pfJets.reset (new PFJetCollection);
    else if (makeGenJet (mJetType)) genJets.reset (new GenJetCollection);
    else if (makeBasicJet (mJetType)) basicJets.reset (new BasicJetCollection);
    else if (makeGenericJet (mJetType)) genericJets.reset (new GenericJetCollection);
    vector <ProtoJet>::const_iterator protojet = output.begin ();
    JetMaker jetMaker;
    for (; protojet != output.end (); protojet++) {
      if (caloJets.get ()) {
	if (!towerGeometry) {
	  edm::ESHandle<CaloGeometry> geometry;
	  fSetup.get<IdealGeometryRecord>().get(geometry);
	  towerGeometry = geometry->getSubdetectorGeometry(DetId::Calo, CaloTowerDetId::SubdetId);
	}
	caloJets->push_back (jetMaker.makeCaloJet (*protojet, *towerGeometry));
      }
      else if (pfJets.get ()) { 
	pfJets->push_back (jetMaker.makePFJet (*protojet));
      }
      else if (genJets.get ()) { 
	genJets->push_back (jetMaker.makeGenJet (*protojet));
      }
      else if (basicJets.get ()) { 
	basicJets->push_back (jetMaker.makeBasicJet (*protojet));
      }
      else if (genericJets.get ()) { 
	genericJets->push_back (jetMaker.makeGenericJet (*protojet));
      }
    }
    // sort and store output
    if (mVerbose) {
      std::cout << "OUTPUT JET COLLECTION:" << std::endl;
    }
    if (caloJets.get ()) {
      GreaterByPt<CaloJet> compJets;
      std::sort (caloJets->begin (), caloJets->end (), compJets);
      if (mVerbose) dumpJets (*caloJets);
      // make jet-track association
      e.put(caloJets);  //Puts Jet Collection into event
    }
    else if (genJets.get ()) {
      GreaterByPt<GenJet> compJets;
      std::sort (genJets->begin (), genJets->end (), compJets);
      if (mVerbose) dumpJets (*genJets);
      e.put(genJets);  //Puts Jet Collection into event
    }
    else if (pfJets.get ()) {
      GreaterByPt<PFJet> compJets;
      std::sort (pfJets->begin (), pfJets->end (), compJets);
      if (mVerbose) dumpJets (*pfJets);
      e.put(pfJets);  //Puts Jet Collection into event
    }
    else if (basicJets.get ()) {
      GreaterByPt<BasicJet> compJets;
      std::sort (basicJets->begin (), basicJets->end (), compJets);
      if (mVerbose) dumpJets (*basicJets);
      e.put(basicJets);  //Puts Jet Collection into event
    }
    else if (genericJets.get ()) {
      GreaterByPt<GenericJet> compJets;
      std::sort (genericJets->begin (), genericJets->end (), compJets);
      if (mVerbose) dumpJets (*genericJets);
      e.put(genericJets);  //Puts Jet Collection into event
    }
    reco::JetTrackMatch<reco::CaloJetCollection> jetTrackMap;
  }
}

