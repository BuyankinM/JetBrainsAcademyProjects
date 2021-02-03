spin, el_charge = input(), input()

if spin == "1/2":
    if el_charge == "-1/3":
        print("Strange Quark")
    elif el_charge == "2/3":
        print("Charm Quark")
    elif el_charge == "-1":
        print("Electron Lepton")
    else:
        print("Muon Lepton")
elif spin == "1":
    print("Photon Boson")
else:
    print("Higgs boson Boson")
