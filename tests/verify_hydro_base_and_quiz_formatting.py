# -*- coding: utf-8 -*-
"""
Verification suite for:
1. Chemistry formula formatting in Academy Quiz (solving raw LaTeX strings like C_{n}H_{2n+2-2k}O_{2x}).
2. Fix for "Oxygen" word mangling (never turns into O_x_ygen).
3. Hydrolysis in Alkaline Medium (Virtual Lab 2: Xà Phòng Hóa) with 4 ester substances (regular, vinyl, isopropenyl, phenyl).
"""
import re

def test_quiz_formula_formatting_and_base_hydro():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    print("🧪 Running Hydro Base Lab & Quiz Formula Formatting Verification...")

    # 1. Check formatFormula logic
    assert "formatted.replace(/_\\{([^}]+)\\}/g, \"<sub>$1</sub>\")" in html, "Must replace LaTeX _{...}"
    assert "formatted.replace(/_([a-zA-Z0-9+\\-]+)/g, \"<sub>$1</sub>\")" in html, "Must replace _(...) subscripts"
    assert "(?![a-zA-Z])" in html, "Oxygen guard (?![a-zA-Z]) must be in Oxygen subscript regex"

    # 2. Check Academy Quiz render calls formatFormula
    assert "qTextEl.innerHTML = formatFormula(q.q);" in html, "qTextEl must use formatFormula"
    assert "<span>${formatFormula(opt)}</span>" in html, "Quiz options must use formatFormula"
    assert "${formatFormula(q.explain)}" in html, "Quiz explanation feedback must use formatFormula"

    # 3. Check Subtab 2: Alkaline Hydrolysis exists
    assert "btnSubtabBaseHydro" in html, "btnSubtabBaseHydro tab button must exist"
    assert "Thủy phân trong môi trường kiềm (Xà phòng hóa)" in html, "Tab title must mention kiềm / xà phòng hóa"
    assert "hydroBaseLab" in html, "hydroBaseLab container must exist"

    # 4. Check Apparatus and Phase elements for Base Hydrolysis
    assert "hydroBaseTopPhase" in html, "hydroBaseTopPhase element must exist"
    assert "hydroBaseBottomPhase" in html, "hydroBaseBottomPhase element must exist"
    assert "hydroBaseFlame" in html, "hydroBaseFlame element must exist"
    assert "labelBaseTopPhase" in html, "labelBaseTopPhase element must exist"
    assert "labelBaseBottomPhase" in html, "labelBaseBottomPhase element must exist"
    assert "btnHeatBaseHydrolysis" in html, "btnHeatBaseHydrolysis button must exist"

    # 5. Check 4 Ester selection buttons in Base Hydrolysis
    assert "btnHydroBaseRegular" in html, "btnHydroBaseRegular must exist"
    assert "btnHydroBaseVinyl" in html, "btnHydroBaseVinyl must exist"
    assert "btnHydroBaseIsopropenyl" in html, "btnHydroBaseIsopropenyl must exist"
    assert "btnHydroBasePhenyl" in html, "btnHydroBasePhenyl must exist"

    # 6. Check JavaScript functions & Specs for Base Hydrolysis
    assert "HYDRO_BASE_SPECS" in html, "HYDRO_BASE_SPECS lookup object must exist"
    assert "selectHydroBaseEsterType" in html, "selectHydroBaseEsterType function must exist"
    assert "heatHydroBaseReaction" in html, "heatHydroBaseReaction function must exist"
    assert "resetHydroBaseReaction" in html, "resetHydroBaseReaction function must exist"

    # 7. Check 4 Substances in HYDRO_BASE_SPECS
    assert "CH₃COOC₂H₅ + NaOH" in html, "Regular ester base reaction must exist"
    assert "CH₃COONa + C₂H₅OH" in html, "Regular ester products must exist"
    assert "CH₃COOCH=CH₂ + NaOH" in html, "Vinyl ester base reaction must exist"
    assert "CH₃COONa + CH₃CHO" in html, "Vinyl ester products (aldehyde) must exist"
    assert "CH₃COOC(CH₃)=CH₂ + NaOH" in html, "Isopropenyl ester base reaction must exist"
    assert "CH₃COONa + CH₃COCH₃" in html, "Isopropenyl ester products (acetone) must exist"
    assert "CH₃COOC₆H₅ + 2NaOH" in html, "Phenyl ester base reaction with 2NaOH must exist"
    assert "CH₃COONa + C₆H₅ONa + H₂O" in html, "Phenyl ester 2 salts products must exist"

    # 8. Check Acid Hydrolysis specs for phenyl acetate
    assert "CH₃COOC₆H₅ + H₂O" in html, "Phenyl acetate in acid hydrolysis must react with H2O"
    assert "CH₃COOH + C₆H₅OH" in html, "Phenyl acetate in acid hydrolysis must produce CH3COOH and phenol"

    # 9. Check switchHydroLab supports 'base'
    assert 'mode === "base"' in html, "switchHydroLab must support base mode"
    assert 'btnSubtabBaseHydro' in html, "switchHydroLab must toggle btnSubtabBaseHydro"

    # 10. Check test tube homogeneous behavior in base hydrolysis
    # In base hydrolysis, topPhase goes to 0% and bottomPhase goes to 100%
    base_heat_idx = html.find("function heatHydroBaseReaction()")
    assert base_heat_idx != -1, "heatHydroBaseReaction function must exist"
    heat_code = html[base_heat_idx:base_heat_idx + 1200]
    assert 'topPhase.style.height = "0%"' in heat_code, "Top phase must disappear to 0% in base hydrolysis (complete reaction)"
    assert 'bottomPhase.style.height = "100%"' in heat_code, "Bottom phase must expand to 100% (homogeneous solution)"

    print("🎉 ALL 10 TESTS IN VERIFY_HYDRO_BASE_AND_QUIZ_FORMATTING PASSED! ✅")

if __name__ == "__main__":
    test_quiz_formula_formatting_and_base_hydro()
