#include "L1AnalysisL1CaloTowerDataFormat.h"
#include "TH2F.h"
#include <map> // Include the map header

void HF_l1_corln() {
  TChain *ch2 = new TChain("hiEvtAnalyzer/HiTree");
  TChain *ch4 = new TChain("l1CaloTowerEmuTree/L1CaloTowerTree");

  // ... (code to add files to ch2 and ch4)
  ch2->Add("/eos/cms/store/group/phys_heavyions/tsheng/Forest2024/*.root");
  ch4->Add("/eos/cms/store/group/phys_heavyions/rosingh/L1ntuples_24/L1Ntuple_640b_LS62_64.root");
  float HFsum;
  ULong64_t evt_off;
  UInt_t lumi_off;
  // Create a map to store HFsum information associated with events
  std::map<ULong64_t, float> eventHFsumMap;
TFile* l1File_p = new TFile("/eos/cms/store/group/phys_heavyions/rosingh/L1ntuples_24/L1Ntuple_640b_LS62_64.root", "READ");

  TTree* eventTree_p = (TTree*)l1File_p->Get("l1EventTree/L1EventTree");
  TTreeReader eventReader(eventTree_p);
  TTreeReaderValue<UInt_t> lumi(eventReader, "lumi");
  TTreeReaderValue<ULong64_t> event(eventReader, "event");
  L1Analysis::L1AnalysisL1CaloTowerDataFormat *L1CaloTower = new L1Analysis::L1AnalysisL1CaloTowerDataFormat();

  TH2F *h2 = new TH2F("L1HF_HF","",1000,0,10000,1400,0.,14000.0);
  //ch1->SetBranchAddress("HLT_HIMinimumBiasHF1AND_v2",&HLT_MBHF1AND);                                                     
  ch2->SetBranchAddress("hiHF",&HFsum);
  ch2->SetBranchAddress("evt",&evt_off);
  ch2->SetBranchAddress("lumi",&lumi_off);                                                                               
  ch4->SetBranchAddress("L1CaloTower", &L1CaloTower);
  int nentries = ch2->GetEntries();
  int lentries= ch4->GetEntries();
  
  cout<<nentries<<",  "<<lentries<<endl;    

  for (int i = 0; i < nentries; i++) {
    ch2->GetEntry(i);
    // Store the HFsum information associated with evt_off in the map
    eventHFsumMap[evt_off] = HFsum;
  }
  // Iterate through ch4 to combine L1CaloTower information with HFsum
  for (int j = 0; j < lentries; j++) {
    ch2->GetEntry(j);
    eventReader.Next();	      

    ULong64_t evt_on = *(event.Get());
    ULong64_t lumi_on = *(lumi.Get());
    ch4->GetEntry(j);
    //if(j%1000==0)cout<<evt_off<<" ,  "<<evt_on<<",  "<<lumi_off<<",  "<<lumi_on<<endl;
    // Check if evt_on is in the eventHFsumMap
    auto it = eventHFsumMap.find(evt_on);
    if (it != eventHFsumMap.end()) {
    HFsum = it->second; // Get the corresponding HFsum
         if(j%1000==0)cout<<j<<"th event with HFsum= "<<HFsum<<endl;
      int l1_etsumPlus = 0;
      int l1_etsumMinus = 0;

      for (int k = 0; k < L1CaloTower->nTower; k++) {
	if (L1CaloTower->ieta[k] > 29) l1_etsumPlus += L1CaloTower->iet[k];
	if (L1CaloTower->ieta[k] < -29) l1_etsumMinus += L1CaloTower->iet[k];
      }
      double L1etsum=(l1_etsumPlus + l1_etsumMinus)/2;
      h2->Fill( HFsum,L1etsum);
    }
  }
  TFile f("HF_L1HF_corr_2024.root","RECREATE"); 
  h2->Write();                                    
  f.Close();                                      

}
