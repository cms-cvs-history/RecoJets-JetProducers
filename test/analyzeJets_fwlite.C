/*   A macro for making a histogram of jet stuff
*/

#include "DataFormats/FWLite/interface/Handle.h"
#include "DataFormats/FWLite/interface/Event.h"
#include "TFile.h"
#include "TH1.h"
#include "TMath.h"
#include "TCanvas.h"
#include "TLegend.h"


#if !defined(__CINT__) && !defined(__MAKECINT__)
#include "DataFormats/JetReco/interface/CaloJet.h"
#endif

#include <iostream>
#include <cmath>      //necessary for absolute function fabs()

using namespace std;

void analyzeJets_fwlite( const char * fileName,
			 const char * outputName = "analyzeJets_fwlite.root")
{
  TFile  * inputFile = new TFile(fileName);

  fwlite::Event ev(inputFile);

  TFile * outputFile = new TFile(outputName, "RECREATE");
  TH1D * hist_jetPt = new TH1D("hist_jetPt", "Jet p_{T}", 100, 0, 1000 );
  TH1D * hist_jetEta = new TH1D("hist_jetEta", "Jet #eta", 100, -5.0, 5.0 );
  TH1D * hist_jetPhi = new TH1D("hist_jetPhi", "Jet #phi", 100, -TMath::Pi(), TMath::Pi() );
  TH1D * hist_jetEMF = new TH1D("hist_jetEMF", "Jet EMF", 100, 0, 1);

  //loop through each event
  for( ev.toBegin();
       ! ev.atEnd();
       ++ev) {
    edm::EventBase & event = ev;
    edm::Handle<std::vector<reco::CaloJet> > h_jet;
    event.getByLabel(edm::InputTag("ak5CaloJets"), h_jet);
    if (!h_jet.isValid() ) continue;
    vector<reco::CaloJet> const & jets = *h_jet;
    
    //loop through each Jet
    vector<reco::CaloJet>::const_iterator iter;
    for ( iter = jets.begin(); iter != jets.end() ; ++iter) {
      

      hist_jetPt->Fill( iter->pt() );
      hist_jetEta->Fill( iter->eta() );
      hist_jetPhi->Fill( iter->phi() );
      hist_jetEMF->Fill( iter->emEnergyFraction() );
    }   //end Jet loop   
  }   //end event loop


  outputFile->cd();
  hist_jetPt->Write();
  hist_jetEta->Write();
  hist_jetPhi->Write();
  hist_jetEMF->Write();
  delete hist_jetPt;
  delete hist_jetEta;
  delete hist_jetPhi;
  delete hist_jetEMF;
  
  outputFile->Close();
  delete outputFile;
}
