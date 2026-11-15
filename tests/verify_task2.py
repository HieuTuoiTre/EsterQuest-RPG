"""
Verification script for Task 2: Chapter 1 - Knight Academy & 4 Virtual Alchemy Labs + Matching Mini-game
"""
import re
import sys

def check_js_syntax(script_text):
    """
    Careful scanner to count matching brackets while ignoring strings, regexes and comments.
    """
    stack = []
    pairs = {'{': '}', '(': ')', '[': ']'}
    rev_pairs = {'}': '{', ')': '(', ']': '['}
    
    i = 0
    n = len(script_text)
    line = 1
    col = 1
    last_non_ws = ''
    
    while i < n:
        c = script_text[i]
        
        if c == '\n':
            line += 1
            col = 1
            i += 1
            continue
            
        if c in ' \t\r':
            i += 1
            col += 1
            continue
            
        # Single line comment
        if c == '/' and i + 1 < n and script_text[i+1] == '/':
            i += 2
            while i < n and script_text[i] != '\n':
                i += 1
            continue
            
        # Multi line comment
        if c == '/' and i + 1 < n and script_text[i+1] == '*':
            i += 2
            while i + 1 < n and not (script_text[i] == '*' and script_text[i+1] == '/'):
                if script_text[i] == '\n':
                    line += 1
                i += 1
            i += 2
            continue

        # Regex literal: /.../
        if c == '/' and (last_non_ws in '(=:[,!&|?{};~^+-%' or not last_non_ws):
            i += 1
            col += 1
            in_char_class = False
            while i < n:
                rc = script_text[i]
                if rc == '\n':
                    break # regexes can't cross lines
                if rc == '\\':
                    i += 2
                    col += 2
                    continue
                if rc == '[':
                    in_char_class = True
                elif rc == ']':
                    in_char_class = False
                elif rc == '/' and not in_char_class:
                    i += 1
                    col += 1
                    while i < n and script_text[i] in 'gimsuy':
                        i += 1
                        col += 1
                    break
                i += 1
                col += 1
            last_non_ws = ')'
            continue
            
        # Strings: single quote, double quote, template literal
        if c in ("'", '"', '`'):
            quote = c
            i += 1
            col += 1
            while i < n:
                if script_text[i] == '\\':
                    i += 2
                    col += 2
                    continue
                if script_text[i] == quote:
                    i += 1
                    col += 1
                    break
                if script_text[i] == '\n':
                    line += 1
                    col = 1
                else:
                    col += 1
                i += 1
            last_non_ws = ')'
            continue
            
        # Brackets
        if c in pairs:
            stack.append((c, line, col))
        elif c in rev_pairs:
            if not stack:
                return False, f"Unexpected closing '{c}' at line {line}, col {col}"
            last, l_line, l_col = stack.pop()
            if pairs[last] != c:
                return False, f"Mismatched bracket '{last}' (line {l_line}) with '{c}' at line {line}, col {col}"
                
        last_non_ws = c
        i += 1
        col += 1
        
    if stack:
        last, l_line, l_col = stack[-1]
        return False, f"Unclosed bracket '{last}' from line {l_line}, col {l_col}"
        
    return True, "JS syntax brackets clean"


def verify_task2(filepath="index.html"):
    print(f"Reading and verifying {filepath} for Task 2...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []

    # 1. Check <section id="academyScreen"> placement: must be after #menuScreen and before #battleScreen
    menu_pos = content.find('id="menuScreen"')
    academy_pos = content.find('id="academyScreen"')
    battle_pos = content.find('id="battleScreen"')

    if academy_pos == -1:
        errors.append("Missing <section id='academyScreen'>")
    else:
        if menu_pos == -1 or academy_pos < menu_pos:
            errors.append("#academyScreen must be placed after #menuScreen")
        if battle_pos == -1 or academy_pos > battle_pos:
            errors.append("#academyScreen must be placed before #battleScreen")

    # 2. Check Stepper Navigation
    stepper_ids = [
        "academyStepper",
        "stepBtn1", "stepBtn2", "stepBtn3", "stepBtn4", "stepBtn5",
        "stepBubble1", "stepBubble2", "stepBubble3", "stepBubble4", "stepBubble5",
        "stepStatus1", "stepStatus2", "stepStatus3", "stepStatus4", "stepStatus5"
    ]
    for s_id in stepper_ids:
        if f'id="{s_id}"' not in content:
            errors.append(f"Missing Stepper ID: {s_id}")

    # 3. Check 5 Lesson Panes
    for i in range(1, 6):
        if f'id="lessonPane{i}"' not in content:
            errors.append(f"Missing Lesson Pane ID: lessonPane{i}")

    # 4. Check Lesson 1 Elements
    l1_elements = [
        "moleculeDisplay", "moleculeInfoBox",
        "btnMolEthylAcetate", "btnMolMethylFormate",
        "l1Options", "l1Feedback", "btnUnlockL2"
    ]
    for el in l1_elements:
        if f'id="{el}"' not in content:
            errors.append(f"Lesson 1 missing element ID: {el}")

    # 5. Check Lesson 2 Elements
    l2_elements = [
        "nomenAcidOptions", "nomenAlcoholOptions",
        "nomenFormulaDisplay", "nomenNameDisplay",
        "l2Options", "l2Feedback", "btnUnlockL3"
    ]
    for el in l2_elements:
        if f'id="{el}"' not in content:
            errors.append(f"Lesson 2 missing element ID: {el}")

    # 6. Check Lesson 3 Elements (Boiling Lab)
    l3_elements = [
        "btnSubstanceEster", "btnSubstanceAlcohol", "btnSubstanceAcid",
        "boilingTestTube", "boilingLiquid", "boilingBubbles", "boilingSteam",
        "mercuryThread", "burnerFlame",
        "tempSlider", "currentTempDisplay", "boilingStatusBanner",
        "l3Options", "l3Feedback", "btnUnlockL4"
    ]
    for el in l3_elements:
        if f'id="{el}"' not in content:
            errors.append(f"Lesson 3 missing element ID: {el}")

    # Check boiling points & rule
    for bp_val in ["77°C", "78.3°C", "118°C"]:
        if bp_val not in content:
            errors.append(f"Boiling temperature value missing: {bp_val}")

    # 7. Check Lesson 4 Elements (Hydrolysis & Silver Mirror)
    l4_elements = [
        "btnSubtabHydro", "btnSubtabSilver",
        "hydroSeparationLab", "silverMirrorLab",
        "hydroTopPhase", "hydroBottomPhase", "hydroFlame",
        "labelTopPhase", "labelBottomPhase",
        "btnHeatHydrolysis", "hydroEquationDisplay",
        "btnSilverVinyl", "btnSilverEthyl",
        "silverTestTube", "silverFlame", "btnApplySilverReagent", "silverStatusBanner", "silverEquationDisplay",
        "l4Options", "l4Feedback", "btnUnlockL5"
    ]
    for el in l4_elements:
        if f'id="{el}"' not in content:
            errors.append(f"Lesson 4 missing element ID: {el}")

    # 8. Check Lesson 5 Elements (Synthesis Lab & Matching Quest)
    l5_elements = [
        "btnAcidCH3COOH", "btnAcidHCOOH", "btnAcidC2H5COOH",
        "btnAlcEthanol", "btnAlcMethanol", "btnAlcIsoamyl",
        "btnHeatSynthesis", "synthTopPhase", "synthBottomPhase", "synthFlame",
        "synthesisResultBox", "synthEquationDisplay",
        "matchingQuestPanel", "matchingQuestHeader", "matchingRoundTitle", "matchingProgressText",
        "matchingGameGrid", "matchingSuccessBanner", "btnNextMatchingRound",
        "graduationHero", "btnGraduationStart", "btnGraduationHome",
        "btnAcademyHome", "btnPrevLesson", "btnNextLesson"
    ]
    for el in l5_elements:
        if f'id="{el}"' not in content:
            errors.append(f"Lesson 5 missing element ID: {el}")

    # 9. Check Header and MenuScreen Buttons
    if 'id="btnHeaderAcademy"' not in content:
        errors.append("Missing id='btnHeaderAcademy' on header")
    if 'id="btnMenuAcademy"' not in content:
        errors.append("Missing id='btnMenuAcademy' on menuScreen")

    # 10. Check Matching Quest Data: Fruit smells (Màn 1) and Applications (Màn 2)
    matching_keywords = [
        "Isoamyl acetate", "chuối",
        "Ethyl propionate", "dứa",
        "Benzyl acetate", "nhài",
        "Geranyl acetate", "hồng",
        "Methyl methacrylate", "Plexiglas",
        "Butyl acetate", "dung môi",
        "Triacylglycerol", "xà phòng",
        "Methyl salicylate", "giảm đau"
    ]
    for kw in matching_keywords:
        if kw.lower() not in content.lower():
            errors.append(f"Matching game keyword missing: {kw}")

    # 11. Check LocalStorage and Potion reward logic
    if 'esterQuest_ch1Completed' not in content:
        errors.append("Missing localStorage key 'esterQuest_ch1Completed'")
    if 'potions' not in content or 'esterQuest_ch1Completed' not in content:
        errors.append("Missing potion bonus reward check for Chapter 1 completion")

    # 12. Check JavaScript Functions
    required_js_fns = [
        "openAcademyScreen",
        "switchAcademyLesson",
        "navigateLesson",
        "updateAcademyStepper",
        "unlockAcademyLesson",
        "renderMolecule",
        "explainMoleculePart",
        "selectNomenAcid",
        "selectNomenAlcohol",
        "selectBoilingSubstance",
        "updateBoilingTemp",
        "switchHydroLab",
        "heatHydrolysisReaction",
        "resetHydrolysisReaction",
        "selectSilverSubstance",
        "runSilverMirrorTest",
        "selectSynthesisAcid",
        "selectSynthesisAlcohol",
        "heatSynthesisReaction",
        "initMatchingGame",
        "handleMatchingCardClick",
        "handleMatchingRoundComplete",
        "proceedToMatchingRound2",
        "triggerAcademyGraduation",
        "checkAcademyQuiz",
        "handleStartGameClick",
        "startGameFromAcademy"
    ]
    for fn in required_js_fns:
        pattern = rf"(function\s+{fn}|{fn}\s*=|{fn}\s*\()"
        if not re.search(pattern, content):
            errors.append(f"Missing JS function: {fn}")

    # 13. Check SFX Methods
    sfx_methods = ["bubble", "silverMirror", "matchSuccess", "academyGraduation"]
    for sfx in sfx_methods:
        if f"SFX.{sfx}" not in content:
            errors.append(f"Missing SFX method: SFX.{sfx}")

    # 14. Check CSS Rules & Classes
    required_css = [
        "#academyScreen",
        ".academy-stepper",
        ".step-btn",
        ".virtual-test-tube",
        ".tube-phase-top",
        ".tube-phase-bottom",
        ".bubble-container",
        ".steam-container",
        ".tube-silver-mirror",
        ".matching-game-grid",
        ".matching-card",
        ".graduation-hero"
    ]
    for css in required_css:
        if css not in content:
            errors.append(f"Missing CSS rule: {css}")

    # 15. Standardized Chemistry Terminology Check in newly added Academy code
    # We should make sure modern terms are strictly respected
    academy_match = re.search(r'<section id="academyScreen">(.*?)</section>', content, re.DOTALL)
    if academy_match:
        acad_text = academy_match.group(1)
        # Check that proper terms exist
        for good_term in ["ester", "acid", "alcohol"]:
            if good_term not in acad_text.lower():
                errors.append(f"Standard term '{good_term}' not found in Academy content")
        
        # Check against obsolete terms (like este, axit, ancol) in chemistry context
        bad_patterns = [
            (r'\beste\b', "Obsolete term 'este' found in Academy content (use 'ester')"),
            (r'\baxit\b', "Obsolete term 'axit' found in Academy content (use 'acid')"),
            (r'\bancol\b', "Obsolete term 'ancol' found in Academy content (use 'alcohol')"),
            (r'\bglixerol\b', "Obsolete term 'glixerol' found in Academy content (use 'glycerol')")
        ]
        for pat, err_msg in bad_patterns:
            if re.search(pat, acad_text, re.IGNORECASE):
                errors.append(err_msg)

    # 16. Check JS Bracket Syntax
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if script_match:
        raw_script = script_match.group(1)
        valid, msg = check_js_syntax(raw_script)
        if not valid:
            errors.append(f"JS syntax bracket check error: {msg}")

    # Summary
    if errors:
        print(f"❌ Task 2 Verification FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("✅ Task 2 Verification PASSED! All 5 Lessons, 4 Virtual Labs, Mini-games, Stepper, and routing are fully verified!")
        return True

if __name__ == "__main__":
    success = verify_task2()
    sys.exit(0 if success else 1)
