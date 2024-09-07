#include "Pythia8/Pythia.h"
#include <cmath>
using namespace Pythia8;

int main(int argc, char* argv[]) {
  Pythia pythia;
  pythia.readFile(argv[1]);
  
  int nEvent = pythia.mode("Main:numberOfEvents");
  pythia.init();
  
  int dbaru = 0;
  int ebarve = 0;
  int sbaru = 0;
  int sbarc = 0;
  int taubarvtau = 0;
  int mubarvmu = 0;
  int unknown = 0;
  int dbarc = 0;
  int bbarc = 0;
  
  for (int iEvent = 0; iEvent < nEvent; ++ iEvent) {
    pythia.next();
    int iW = 0;
    for (int i = 0; i < pythia.event.size(); ++i) {
      if (pythia.event[i].id() == 24) {
        iW = i;
      }
    }
    // cout << "W boson: " << iW  << " Size of event: " << pythia.event.size() << endl;
    int iDau1 = pythia.event[iW].daughter1();
    int iDau2 = pythia.event[iW].daughter2();
    int Dau1 = pythia.event[iDau1].id();
    int Dau2 = pythia.event[iDau2].id();
    
    // if ( (Dau1 == -1 and Dau2 == 2) or (Dau1 == -11 and Dau2 == 12) or (Dau1 == -3 and Dau2 == 2) or (Dau1 == -3 and Dau2 == 4) or (Dau1 == -15 and Dau2 == 16) or (Dau1 == -13 and Dau2 == 14) or (Dau1 == -1 and Dau2 == 4) or (Dau1 == 90 and Dau2 == 90) or (Dau1 == -5 and Dau2 == 4)) 
    // cout << "Daughter 1: " << pythia.event[iDau1].id() << " Daughter 2: " << pythia.event[iDau2].id() << endl;
   
   
    if (pythia.event[iDau1].id() == -1 and pythia.event[iDau2].id() == 2) dbaru++;
    if (pythia.event[iDau1].id() == -11 and pythia.event[iDau2].id() == 12) ebarve++;
    if (pythia.event[iDau1].id() == -3 and pythia.event[iDau2].id() == 2) sbaru++;
    if (pythia.event[iDau1].id() == -3 and pythia.event[iDau2].id() == 4) sbarc++;
    if (pythia.event[iDau1].id() == -15 and pythia.event[iDau2].id() == 16) taubarvtau++;
    if (pythia.event[iDau1].id() == -13 and pythia.event[iDau2].id() == 14) mubarvmu++;
    if (pythia.event[iDau1].id() == -1 and pythia.event[iDau2].id() == 4) dbarc++;
    if (pythia.event[iDau1].id() == 90 and pythia.event[iDau2].id() == 90) unknown++;
    if (pythia.event[iDau1].id() == -5 and pythia.event[iDau2].id() == 4) bbarc++;
  
    
  }

  int total = dbaru + ebarve + sbaru + sbarc + taubarvtau + mubarvmu + unknown + dbarc + bbarc;
  cout << "Total: " << total << endl;
  cout << "dbar u " << dbaru << "\t\t Branching Ratio: " << (double)dbaru/(double)total << endl;
  cout << "ebar ve " << ebarve << "\t\t Branching Ratio: " << (double)ebarve/(double)total << endl;
  cout << "sbar u " << sbaru << "\t\t Branching Ratio: " << (double)sbaru/(double)total << endl;
  cout << "sbar c " << sbarc << "\t\t Branching Ratio: " << (double)sbarc/(double)total << endl;
  cout << "taubar vtau " << taubarvtau << "\t\t Branching Ratio: " << (double)taubarvtau/(double)total << endl;
  cout << "mubar vmu " << mubarvmu << "\t\t Branching Ratio: " << (double)mubarvmu/(double)total << endl;
  cout << "dbar c " << dbarc << "\t\t Branching Ratio: " << (double)dbarc/(double)total << endl;
  cout << "unknown " << unknown << "\t\t Branching Ratio: " << (double)unknown/(double)total << endl;
  cout << "bbar c " << bbarc << "\t\t Branching Ratio: " << (double)bbarc/(double)total << endl;
  
  pythia.stat();
  return 0;
  
}
