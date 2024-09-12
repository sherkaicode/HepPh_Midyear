// -*- C++ -*-
#include "Rivet/Analysis.hh"
#include "Rivet/Projections/PromptFinalState.hh"

namespace Rivet {


  /// @brief Study of prompt dilepton kinematics sensitive to boson polarizations
  class MY_TEST : public Analysis {
  public:

    /// Constructor
    RIVET_DEFAULT_ANALYSIS_CTOR(MY_TEST);


    /// @name Analysis methods
    /// @{

    /// Book histograms and initialise projections before the run
    void init() {

      
      // set FS cuts from input options
      const double etacut = getOption<double>("ABSETALMAX", 5.);
      const double ptcut = getOption<double>("PTLMIN", 10.);
      
      // Initialise and register projections
      declare(PromptFinalState((Cuts::abspid == PID::ELECTRON || Cuts::abspid == PID::MUON)
                               && Cuts::abseta < etacut && Cuts::pT > ptcut*GeV), "Leptons");

      // Book histograms
      book(_h_pt_l1, "lep1_pt", logspace(40, 10, 400));
      book(_h_costheta_l1, "lep1_costheta", linspace(25, -1, 1));
      book(_h_ppara_l1, "lep1_ppara", linspace(40, -50, 350));
      book(_h_pperp_l1, "lep1_pperp", linspace(25, 0, 100));
      //
      book(_h_pt_l2, "lep2_pt", logspace(40, 10, 400));
      book(_h_costheta_l2, "lep2_costheta", linspace(25, -1, 1));
      book(_h_ppara_l2, "lep2_ppara", linspace(40, -50, 350));
      book(_h_pperp_l2, "lep2_pperp", linspace(25, 0, 100));
      //
      book(_h_costheta_com_l1, "com_costheta_l1", linspace(25, -1, 1));
      book(_h_costheta_com_l2, "com_costheta_l2", linspace(25, -1, 1));
      book(_h_ppara_com_l1, "com_ppara_l1", linspace(25, -50, 50));
      book(_h_ppara_com_l2, "com_ppara_l2", linspace(25, -50, 50));
      //
      book(_h_costheta_com, "com_costheta", linspace(25, -1, 1));
      book(_h_ppara_com, "com_ppara", linspace(25, -50, 50));
      book(_h_pperp_com, "com_pperp", linspace(25, 0, 100));
      
      // Added for invariant mass
      book(_h_mass_ee, "ee_mass", linspace(100, 0, 200)); 

    }


    /// Perform the per-event analysis
    void analyze(const Event& event) {
      const Particles& leptons = apply<FinalState>(event, "Leptons").particlesByPt();
      if (leptons.size() != 2) vetoEvent;
      const Particle& l1 = leptons[0];
      const Particle& l2 = leptons[1];
      _h_pt_l1->fill(l1.pT()/GeV);
      _h_pt_l2->fill(l2.pT()/GeV);

      const FourMomentum pcom = l1.mom() + l2.mom();
      _h_mass_ee->fill(pcom.mass()/GeV); 
      
      const Vector3 betacom = pcom.betaVec();
      const Vector3 unitboostvec = betacom.unit();
      const LorentzTransform comboost = LorentzTransform::mkFrameTransformFromBeta(betacom);

      const double l1_costheta = cos(l1.p3().angle(unitboostvec));
      const double l1_ppara = l2.p3().dot(unitboostvec);
      const double l1_pperp = l2.p3().cross(unitboostvec).mod();
      _h_costheta_l1->fill(l1_costheta);
      _h_ppara_l1->fill(l1_ppara);
      _h_pperp_l1->fill(l1_pperp);

      const double l2_costheta = cos(l2.p3().angle(unitboostvec));
      const double l2_ppara = l2.p3().dot(unitboostvec);
      const double l2_pperp = l2.p3().cross(unitboostvec).mod();
      _h_costheta_l2->fill(l2_costheta);
      _h_ppara_l2->fill(l2_ppara);
      _h_pperp_l2->fill(l2_pperp);

      const FourMomentum p1com = comboost.transform(l1.mom());
      const FourMomentum p2com = comboost.transform(l2.mom());
      const double com_costheta1 = cos(p1com.p3().angle(unitboostvec));
      const double com_costheta2 = cos(p2com.p3().angle(unitboostvec));
      MSG_DEBUG("CoM cos(th)s: " << com_costheta1 << ", " << com_costheta2);
      // assert(com_costheta1 == com_costheta2 && "CoM cos(th)s differ");
      const double com_ppara1 = p1com.p3().dot(unitboostvec);
      const double com_ppara2 = p2com.p3().dot(unitboostvec);
      MSG_DEBUG("CoM p_paras: " << com_ppara1 << ", " << com_ppara2);
      // assert(com_ppara1 == com_ppara2 && "CoM p_paras differ");
      const double com_pperp1 = p1com.p3().cross(unitboostvec).mod();
      const double com_pperp2 = p2com.p3().cross(unitboostvec).mod();
      MSG_DEBUG("CoM p_pperps: " << com_pperp1 << ", " << com_pperp2);
      // assert(com_pperp1 == com_pperp2 && "CoM p_perps differ");
      _h_costheta_com_l1->fill(com_costheta1);
      _h_costheta_com_l2->fill(com_costheta2);
      _h_costheta_com->fill(com_costheta1, 0.5);
      _h_costheta_com->fill(com_costheta2, 0.5);
      _h_ppara_com_l1->fill(com_ppara1);
      _h_ppara_com_l2->fill(com_ppara2);
      _h_ppara_com->fill(com_ppara1, 0.5);
      _h_ppara_com->fill(com_ppara2, 0.5);
      _h_pperp_com->fill(com_pperp1);
    }


    /// Normalise histograms etc., after the run
    void finalize() {
      normalize(_h_pt_l1); normalize(_h_pt_l2); normalize(_h_ppara_com);
      normalize(_h_pperp_com); normalize(_h_costheta_com); normalize(_h_ppara_com_l1);
      normalize(_h_ppara_com_l2); normalize(_h_costheta_com_l1); normalize(_h_costheta_com_l2);
      normalize(_h_ppara_l1); normalize(_h_pperp_l1); normalize(_h_costheta_l1);
      normalize(_h_ppara_l2); normalize(_h_pperp_l2); normalize(_h_costheta_l2);
    }

    /// @}


    /// @name Histograms
    /// @{
    Histo1DPtr _h_pt_l1, _h_pt_l2;
    Histo1DPtr _h_ppara_com, _h_pperp_com, _h_costheta_com;
    Histo1DPtr _h_ppara_com_l1, _h_ppara_com_l2, _h_costheta_com_l1, _h_costheta_com_l2;
    Histo1DPtr _h_ppara_l1, _h_pperp_l1, _h_costheta_l1;
    Histo1DPtr _h_ppara_l2, _h_pperp_l2, _h_costheta_l2;
    Histo1DPtr _h_mass_ee;
    /// @}


  };


  RIVET_DECLARE_PLUGIN(MY_TEST);


}
