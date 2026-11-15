import re

def test_interactive_labs():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    print("Verifying Interactive Academy Labs and Button Handlers...")

    # 1. Verify SFX.select and SFX.click exist and Proxy exists
    assert "SFX.select = function" in html, "SFX.select must be defined"
    assert "SFX.click = function" in html, "SFX.click must be defined"
    assert "window.SFX = new Proxy" in html, "Defensive SFX Proxy must exist"

    # 2. Verify Lesson 1 Radicals Table & Lesson 2 Nomenclature updates
    assert "radicals-table" in html, "Radicals reference table must exist in Lesson 1"
    assert "allyl" in html, "allyl radical must exist"
    assert "phenyl" in html, "phenyl radical must exist"
    assert "isopropyl" in html, "isopropyl radical must exist"
    assert "methacrylate" in html, "methacrylate radical must exist"
    assert "oxalate" in html, "oxalate radical must exist"
    assert "function updateNomenDisplay()" in html, "updateNomenDisplay must exist"
    assert "subscriptMap" in html, "Chemical formula formatting with subscripts must exist"
    assert "nomenFormulaDisplay" in html, "nomenFormulaDisplay element ID must exist"
    assert "nomenNameDisplay" in html, "nomenNameDisplay element ID must exist"

    # 3. Verify Lesson 3 Boiling Point switches & Calibrated Temperature Slider (Smooth 60fps & Jitter-free)
    assert "function selectBoilingSubstance(key)" in html, "selectBoilingSubstance must exist"
    assert "btnSubstanceEster" in html
    assert "btnSubstanceAlcohol" in html
    assert "btnSubstanceAcid" in html
    assert "boilingLiquid" in html
    assert "boilingPointSpec" in html
    assert "boilingTargetMarker" in html, "Dynamic boiling target pin marker must exist"
    assert "boilingTargetTag" in html, "Target pin tag must exist"
    assert "function adjustBoilingTemp" in html, "adjustBoilingTemp helper must exist"
    assert "function setBoilingTempPreset" in html, "setBoilingTempPreset helper must exist"
    assert "function handleSliderDrag" in html, "handleSliderDrag RAF handler must exist"
    assert "requestAnimationFrame" in html, "requestAnimationFrame must be used for smooth drag"
    assert "touch-action: pan-x" in html, "touch-action must prevent mobile scroll conflict"
    assert "will-change: height" in html, "will-change must be set on thermometer mercury"
    assert "pinPct: 43.85" in html, "Mathematically accurate pin percentage for ester must be 43.85%"
    assert "pinPct: 44.85" in html, "Mathematically accurate pin percentage for alcohol must be 44.85%"
    assert "pinPct: 75.38" in html, "Mathematically accurate pin percentage for acid must be 75.38%"

    # 4. Verify Lesson 4 Hydrolysis & Silver Mirror subtabs and reversible arrow display
    assert "function switchHydroLab(mode)" in html, "switchHydroLab must exist"
    assert "btnSubtabHydro" in html
    assert "btnSubtabSilver" in html
    assert "btnSilverFormate" in html, "btnSilverFormate for Formate ester silver mirror test must exist"
    assert "hydroSeparationLab" in html
    assert "silverMirrorLab" in html
    assert "function selectSilverSubstance(key)" in html
    assert "chem-arrow-stack" in html, "Textbook chemical arrow stack must exist"
    assert "chem-arrow-condition" in html, "Chemical condition above arrow must exist"

    # 5. Verify Lesson 5 Synthesis acid & alcohol selection and all textbook radicals
    assert "function selectSynthesisAcid(acidKey)" in html, "selectSynthesisAcid must exist"
    assert "function selectSynthesisAlcohol(alcKey)" in html, "selectSynthesisAlcohol must exist"
    assert "function getSynthesisSpec(acidKey, alcKey)" in html, "getSynthesisSpec dynamic generator must exist"
    assert "function updateSynthEquation()" in html, "updateSynthEquation must exist"
    assert "function onSynthIngredientsChanged" in html, "onSynthIngredientsChanged handler must exist"
    assert "const SYNTHESIS_SPECS" in html, "SYNTHESIS_SPECS lookup registry must exist"
    assert "HCOOH_isoamyl" in html, "HCOOH + isoamyl combination must exist"
    assert "Isoamyl formate" in html, "Isoamyl formate must be in synthesis specs"
    assert "btnAcidCH3COOH" in html
    assert "btnAcidHCOOH" in html
    assert "btnAcidC2H5COOH" in html
    assert "btnAcidC3H7COOH" in html
    assert "btnAcidAcrylic" in html
    assert "btnAcidMethacrylic" in html
    assert "btnAcidC6H5COOH" in html
    assert "btnAlcEthanol" in html
    assert "btnAlcMethanol" in html
    assert "btnAlcIsoamyl" in html
    assert "btnAlcPropyl" in html
    assert "btnAlcIsopropyl" in html
    assert "btnAlcAllyl" in html
    assert "btnAlcBenzyl" in html
    assert "btnAlcPhenol" in html
    assert "KHÔNG THỂ ĐIỀU CHẾ TRỰC TIẾP PHENYL ESTER" in html, "Trap warning for phenol esterification must exist"

    # 6. Verify Graduation flow & Start Game from Academy
    assert "function startGameFromAcademy()" in html, "startGameFromAcademy function must exist"
    assert "document.getElementById(\"academyScreen\").style.display = \"none\"" in html or "academy.style.display = \"none\"" in html, "Must hide academyScreen when starting game"
    assert "state.potions = 3" in html, "Must award +1 potion bonus on graduation"

    print("✅ All Interactive Lab Handlers, Chemical Subscripts & Defensive Proxy Verified!")

if __name__ == "__main__":
    test_interactive_labs()
