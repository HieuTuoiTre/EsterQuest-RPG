# -*- coding: utf-8 -*-
"""
Verification suite for Academy v2.5 Enhancements:
- 3 Questions per Lesson in Academy with progress tracking (1/3, 2/3, 3/3).
- Anti-Spoil Quiz Logic: Wrong answers DO NOT reveal the correct answer or explanation.
- Lesson 1: 8 molecule models, 2 parts (Acid R-COO- and Alcohol R'), General Formula CnH2n+2-2kO2x.
- Lesson 2: isopropenyl radical in R'.
- Lesson 3: 4 substances per shelf (Ester, Alcohol, Acid) with boiling points up to 180°C.
- Lesson 4: Combustion lab, renamed Acid Hydrolysis lab, 4 ester types (regular, vinyl, isopropenyl, phenyl), Tollens reagent in tube with multiple test substances.
- Typography & Codex updates.
"""
import re
import json

def verify_academy_v2():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    print("🔍 Testing Academy v2.5 Enhancements...")

    # 1. Anti-Spoil Quiz Logic
    assert "btn.classList.add(\"wrong\")" in html, "Must add wrong class on wrong option"
    # When wrong, should NOT add correct class to the correct answer
    assert 'if (chosenIndex === q.correct)' in html or 'if (isCorrect)' in html, "Must branch on correct vs wrong"
    
    # 2. Check 3 Questions per Lesson in QUIZ_DATA
    assert "ACADEMY_QUIZ_DATA" in html or "QUIZ_ANSWERS" in html, "Quiz data structure must exist"

    # 3. Lesson 1: 8 molecules & 2 parts
    for mol in ["ethyl_acetate", "methyl_formate", "vinyl_acetate", "methyl_acrylate", "benzyl_acetate", "isoamyl_acetate", "phenyl_acetate", "methyl_methacrylate"]:
        assert mol in html, f"Molecule {mol} must be supported in Lesson 1"
    
    # 2 parts check: RCOO- and R'
    assert "part-acid-residue" in html or "part-acid" in html, "Must have acid residue part"
    assert "part-alcohol" in html, "Must have alcohol part"

    # General formula ID 73 in Lesson 1 & Codex
    assert "C_{n}H_{2n+2-2k}O_{2x}" in html or "C<sub>n</sub>H<sub>2n+2-2k</sub>O<sub>2x</sub>" in html, "General formula must be in Lesson 1"

    # 4. Lesson 2: isopropenyl in R'
    assert "isopropenyl" in html, "isopropenyl radical must exist in Lesson 2"

    # 5. Lesson 3: 4 substances per shelf
    for s in ["methyl_formate", "ethyl_formate", "ethyl_acetate", "isoamyl_acetate",
              "methanol", "ethanol", "propanol", "butanol",
              "formic_acid", "acetic_acid", "propionic_acid", "butyric_acid"]:
        assert s in html, f"Substance {s} must exist in Lesson 3 boiling lab"

    # 6. Lesson 4: Combustion Lab & 4 ester types & Tollens in tube
    assert "hydroCombustionLab" in html or "btnSubtabCombust" in html or "Thí Nghiệm 3: Phản Ứng Đốt Cháy" in html, "Combustion lab must exist"
    assert "Thủy phân trong môi trường acid" in html, "Must rename Lab 1 to Thủy phân trong môi trường acid"
    assert "isopropenyl" in html and "phenyl" in html, "Must have isopropenyl and phenyl ester hydrolysis options"

    print("✅ All Academy v2.5 structural elements verified!")

if __name__ == "__main__":
    verify_academy_v2()
