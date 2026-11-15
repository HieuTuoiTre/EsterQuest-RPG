# -*- coding: utf-8 -*-
"""
Verification suite for Question Bank accuracy and pedagogical explanations.
"""
import re
import json

def verify_bank():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract QUESTION_BANK
    start_anchor = "const QUESTION_BANK = ["
    end_anchor = "const SKILL_LIBRARY = ["
    assert start_anchor in html, "QUESTION_BANK must exist in index.html"
    assert end_anchor in html, "SKILL_LIBRARY must exist in index.html"

    bank_str = html[html.find(start_anchor):html.find(end_anchor)]

    pattern = re.compile(
        r'id:\s*(\d+),\s*level:\s*(\d+),\s*skillType:\s*(\d+),\s*'
        r'q:\s*"([^"]*)",\s*'
        r'options:\s*(\[[^\]]*\]),\s*'
        r'answer:\s*(\d+),\s*'
        r'hint:\s*"([^"]*)",\s*'
        r'explain:\s*"([^"]*)"',
        re.DOTALL
    )

    questions = {}
    for m in pattern.finditer(bank_str):
        qid = int(m.group(1))
        questions[qid] = {
            'id': qid,
            'level': int(m.group(2)),
            'skillType': int(m.group(3)),
            'q': m.group(4),
            'options': json.loads(m.group(5)),
            'answer': int(m.group(6)),
            'hint': m.group(7),
            'explain': m.group(8)
        }

    print(f"Verified {len(questions)} parsed questions in QUESTION_BANK.")
    assert len(questions) >= 160, f"Expected >= 160 questions, got {len(questions)}"

    # 1. Verify ID 134 (User reported: Tráng bạc must be A = HCOOCH3)
    q134 = questions[134]
    assert q134['answer'] == 0, f"ID 134 answer must be 0 (A: HCOOCH3), got {q134['answer']}"
    assert "HCOOCH3" in q134['options'][q134['answer']], "Option A must be HCOOCH3"
    assert "formyl" in q134['explain'] or "tráng bạc" in q134['explain'], "Explain must be pedagogical"
    print("✅ ID 134 (Tráng bạc => HCOOCH3 - Option A) verified!")

    # 2. Verify ID 144 (User reported: Explain for 22g must not be templated 'tạo thành 22 gam')
    q144 = questions[144]
    assert q144['answer'] == 2, f"ID 144 answer must be 2 (C: 22 gam), got {q144['answer']}"
    assert "phân cắt liên kết C-O tạo thành 22 gam" not in q144['explain'], "Must remove awkward templated phrase"
    assert "0,2" in q144['explain'] and "110" in q144['explain'], "Explain must detail stoichiometric calculation"
    print("✅ ID 144 (22 gam calculation explanation) verified!")

    # 3. Verify ID 145 (Limiting reagent NaOH: 3.28g, not 8.2g)
    q145 = questions[145]
    assert q145['answer'] == 1, f"ID 145 answer must be 1 (B: 3,28 gam), got {q145['answer']}"
    assert "3,28" in q145['options'][q145['answer']]
    print("✅ ID 145 (Limiting reagent NaOH => 3.28g) verified!")

    # 4. Verify ID 99 (Pineapple scent => ethyl butyrate)
    q99 = questions[99]
    assert q99['answer'] == 2, f"ID 99 answer must be 2 (C: ethyl butyrate), got {q99['answer']}"
    assert "CH3CH2CH2COOC2H5" in q99['options'][q99['answer']]
    print("✅ ID 99 (Pineapple scent => ethyl butyrate) verified!")

    # 5. Verify ID 116 (Unsaturated 1 C=C => CnH2n-2O2)
    q116 = questions[116]
    assert q116['answer'] == 3, f"ID 116 answer must be 3 (D: CnH2n-2O2), got {q116['answer']}"
    print("✅ ID 116 (Unsaturated 1 C=C ester formula) verified!")

    # 6. Verify ID 133 (Produces methyl alcohol => HCOOCH3)
    q133 = questions[133]
    assert q133['answer'] == 1, f"ID 133 answer must be 1 (B: HCOOCH3), got {q133['answer']}"
    print("✅ ID 133 (Produces methyl alcohol) verified!")

    # 7. Verify ID 138 (Acid hydrolysis produces C2H5OH => other product is CH3COOH)
    q138 = questions[138]
    assert q138['answer'] == 1, f"ID 138 answer must be 1 (B: CH3COOH), got {q138['answer']}"
    print("✅ ID 138 (Acid hydrolysis => CH3COOH) verified!")

    # 8. Verify ID 148 (Combustion 0.15 mol ester => 0.45 mol CO2 => 3C => C3H6O2)
    q148 = questions[148]
    assert q148['answer'] == 0, f"ID 148 answer must be 0 (A: C3H6O2), got {q148['answer']}"
    print("✅ ID 148 (Combustion calculation => C3H6O2) verified!")

    # 9. Verify ID 158 (X reacts with Na and tráng bạc => HOCH2CHO; Y reacts Na and CaCO3 => CH3COOH)
    q158 = questions[158]
    assert q158['answer'] == 0, f"ID 158 answer must be 0 (A: HOCH2CHO, CH3COOH), got {q158['answer']}"
    print("✅ ID 158 (C2H4O2 isomers) verified!")

    # 10. Verify ID 159 (Hydrolysis => Z reacts with Na => HCOO-CH2CHO)
    q159 = questions[159]
    assert q159['answer'] == 1, f"ID 159 answer must be 1 (B: HCOO-CH2CHO), got {q159['answer']}"
    print("✅ ID 159 (Z reacts with Na => HCOO-CH2CHO) verified!")

    # 11. Verify NO awkward templated phrases in any question
    awkward_phrases = [
        "phân cắt liên kết C-O tạo thành",
        "Đáp án chính xác là",
        "Methanol. có cấu trúc dạng R-COO-R' nên thuộc loại ester."
    ]
    for qid, q in questions.items():
        for phrase in awkward_phrases:
            assert phrase not in q['explain'], f"Question ID {qid} still contains awkward phrase '{phrase}': {q['explain']}"

    print("✅ All awkward/templated explanation phrases eliminated across all questions!")
    # 12. Verify Question 73 explains 'x' and formats subscripts properly
    q73 = questions[73]
    assert "x là số nhóm chức" in q73['q'] or "x là số nhóm chức" in q73['hint'], "Question 73 must explain what x is"
    assert "C_{n}H_{2n+2-2k}O_{2x}" in q73['options'][0], "Option A must format subscripts for n, 2n+2-2k, and 2x"
    print("✅ Question 73 (Defined 'x' as number of ester groups & proper subscripts) verified!")

    # 13. Verify formatFormula regex in index.html handles algebraic subscripts
    assert "C<sub>n</sub>" in html, "formatFormula must format Cn to C<sub>n</sub>"
    assert "H<sub>$1</sub>" in html, "formatFormula must format H algebraic expressions"
    assert "O<sub>$1</sub>" in html, "formatFormula must format O algebraic expressions"
    print("✅ formatFormula algebraic subscript parsing verified!")

    print("\n🎉 ALL 13 VERIFICATION CHECKS PASSED PERFECTLY! 🧪")

if __name__ == "__main__":
    verify_bank()
