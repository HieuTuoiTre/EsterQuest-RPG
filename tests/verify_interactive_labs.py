import re

def test_interactive_labs():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    print("Verifying Interactive Academy Labs and Button Handlers...")

    # 1. Verify SFX.select and SFX.click exist and Proxy exists
    assert "SFX.select = function" in html, "SFX.select must be defined"
    assert "SFX.click = function" in html, "SFX.click must be defined"
    assert "window.SFX = new Proxy" in html, "Defensive SFX Proxy must exist"

    # 2. Verify Lesson 2 Nomenclature updates
    assert "function updateNomenDisplay()" in html, "updateNomenDisplay must exist"
    assert "subscriptMap" in html, "Chemical formula formatting with subscripts must exist"
    assert "nomenFormulaDisplay" in html, "nomenFormulaDisplay element ID must exist"
    assert "nomenNameDisplay" in html, "nomenNameDisplay element ID must exist"

    # 3. Verify Lesson 3 Boiling Point switches
    assert "function selectBoilingSubstance(key)" in html, "selectBoilingSubstance must exist"
    assert "btnSubstanceEster" in html
    assert "btnSubstanceAlcohol" in html
    assert "btnSubstanceAcid" in html
    assert "boilingLiquid" in html
    assert "boilingPointSpec" in html

    # 4. Verify Lesson 4 Hydrolysis & Silver Mirror subtabs
    assert "function switchHydroLab(mode)" in html, "switchHydroLab must exist"
    assert "btnSubtabHydro" in html
    assert "btnSubtabSilver" in html
    assert "hydroSeparationLab" in html
    assert "silverMirrorLab" in html
    assert "function selectSilverSubstance(key)" in html

    # 5. Verify Lesson 5 Synthesis acid & alcohol selection
    assert "function selectSynthesisAcid(acidKey)" in html, "selectSynthesisAcid must exist"
    assert "function selectSynthesisAlcohol(alcKey)" in html, "selectSynthesisAlcohol must exist"
    assert "function updateSynthEquation()" in html, "updateSynthEquation must exist"
    assert "btnAcidCH3COOH" in html
    assert "btnAcidHCOOH" in html
    assert "btnAcidC2H5COOH" in html
    assert "btnAlcEthanol" in html
    assert "btnAlcMethanol" in html
    assert "btnAlcIsoamyl" in html

    print("✅ All Interactive Lab Handlers, Chemical Subscripts & Defensive Proxy Verified!")

if __name__ == "__main__":
    test_interactive_labs()
