// File: KtPilupSubtractionJetProducer.cc
// Description:  see KtPilupSubtractionJetProducer.h
// Author:  Andreas Oehler, University Karlsruhe (TH)
// Creation Date:  Nov. 06 2006 Initial version.
//--------------------------------------------
#include <memory>

#include "KtPilupSubtractionJetProducer.h"

using namespace std;
using namespace reco;
using namespace JetReco;

namespace {
  const bool debug = false;

}

namespace cms
{

  // Constructor takes input parameters now: to be replaced with parameter set.
  KtPilupSubtractionJetProducer::KtPilupSubtractionJetProducer(const edm::ParameterSet& conf)
    : BasePilupSubtractionJetProducer (conf), alg_(conf)

  {}

  // run algorithm itself
  bool KtPilupSubtractionJetProducer::runAlgorithm (const InputCollection& fInput, 
		     OutputCollection* fOutput) {
    alg_.run (fInput, fOutput);

    return true;
  }
}
