"""
Verification script for Task 3 & Task 4:
- Task 3: Active Skill Deck Loadout (10 Alchemy Skills Grimoire, 4 Equipped Slots, Hotkeys 1-4)
- Task 4: Multi-Enemy Arena Engine (1-3 Monsters, Click-to-Target, AOE Execution, Sequential Counter-Attacks)
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
            last_non_ws = 's'
            continue
            
        # Brackets
        if c in pairs:
            stack.append((c, line, col))
            last_non_ws = c
        elif c in rev_pairs:
            if not stack:
                return False, f"Unexpected closing bracket '{c}' at line {line}, col {col}"
            open_c, o_line, o_col = stack.pop()
            if rev_pairs[c] != open_c:
                return False, f"Mismatched bracket: opened '{open_c}' at line {o_line}, col {o_col} but closed with '{c}' at line {line}, col {col}"
            last_non_ws = c
        else:
            last_non_ws = c
            
        i += 1
        col += 1
        
    if stack:
        open_c, o_line, o_col = stack[-1]
        return False, f"Unclosed bracket '{open_c}' from line {o_line}, col {o_col}"
        
    return True, "Syntax brackets match correctly!"

def verify_task3_4():
    print("Reading and verifying index.html for Task 3 & Task 4...")
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    errors = []

    # 1. Check JS bracket syntax
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if not script_match:
        errors.append("No <script> tag found in index.html")
    else:
        raw_script = script_match.group(1)
        valid, msg = check_js_syntax(raw_script)
        if not valid:
            errors.append(f"JS syntax bracket check error: {msg}")

    # 2. Check 10 Skills Library in JS (SKILL_LIBRARY)
    expected_skills = [
        (1, "Đòn Acid Chấn Động", "single"),
        (2, "Hỏa Cầu Ester Hóa", "single"),
        (3, "Khiên Dung Môi Hữu Cơ", "self"),
        (4, "Bão Xà Phòng Hóa", "single"),
        (5, "Độc Khí Ester Thơm", "single"),
        (6, "Chiết Tách Dung Môi", "single"),
        (7, "Gương Bạc Lóa Mắt", "single"),
        (8, "Bộc Phá Oxi Hóa", "single"),
        (9, "Sóng Thủy Phân Toàn Diện", "all"),
        (10, "Bão Nhiệt Phản Ứng", "all")
    ]
    for s_id, s_name, s_target in expected_skills:
        if s_name not in content:
            errors.append(f"Skill name '{s_name}' (ID {s_id}) missing from index.html")
    
    # Check AOE skills distinction
    if "Sóng Thủy Phân Toàn Diện" in content and "Bão Nhiệt Phản Ứng" in content:
        # Check targetType or type
        if "targetType" not in content and "type:" not in content:
            errors.append("Skill library lacks targetType / type differentiation")

    # 3. Check Deck UI Modal & Buttons
    deck_elements = [
        "deckModal", "deckScreen", "btnMenuDeck", "btnBattleDeck",
        "deckActiveSlots", "deckLibraryGrid", "btnSaveDeck", "btnResetDefaultDeck"
    ]
    for el in deck_elements:
        if f'id="{el}"' not in content:
            errors.append(f"Missing Deck UI element ID: {el}")

    # Check button text on menuScreen
    if "Trang Bị Kỹ Năng" not in content:
        errors.append("Missing 'Trang Bị Kỹ Năng' button label on menuScreen")
    if "Đổi Kỹ Năng" not in content:
        errors.append("Missing 'Đổi Kỹ Năng' button label on battleScreen")

    # 4. Check State Variables
    for state_prop in ["activeSkills", "enemies", "selectedEnemyIndex"]:
        if state_prop not in content:
            errors.append(f"Missing state property: state.{state_prop}")

    # 5. Check Multi-Enemy Arena & Elements
    if 'id="enemiesContainer"' not in content:
        errors.append("Missing id='enemiesContainer' in arena-container")
    if '.enemies-container' not in content:
        errors.append("Missing CSS class .enemies-container")
    if '.enemy-unit' not in content:
        errors.append("Missing CSS class .enemy-unit")
    if '.is-targeted' not in content:
        errors.append("Missing CSS class .is-targeted for click-to-target")
    if '.target-indicator' not in content:
        errors.append("Missing CSS class .target-indicator")

    # 6. Check Multi-Enemy Stage definition
    if 'Slime Xanh' not in content or 'Slime Đỏ' not in content or 'Slime Vàng' not in content:
        errors.append("Missing 3 Slimes (Slime Xanh, Đỏ, Vàng) in stage configuration")

    # 7. Check Key Combat Functions
    combat_fns = [
        "openDeckModal", "closeDeckModal", "saveDeckLoadout", "resetDefaultDeck",
        "renderDeckUI", "renderBattleSkills", "castEquippedSkill", "castSkill",
        "renderEnemies", "selectEnemyTarget", "autoSelectNextLivingEnemy",
        "dealAoeDamage", "dealDamageToEnemy", "enemyTurnSequence", "executeNextEnemyAttack"
    ]
    for fn in combat_fns:
        pattern = rf"(function\s+{fn}|{fn}\s*=|{fn}\s*\()"
        if not re.search(pattern, content):
            errors.append(f"Missing combat/deck JS function: {fn}")

    # 8. Check Status Effect Mechanics
    # DoT, Stun, Blind, Weaken, Shield, LifeSteal, ManaBurst
    if "dotTurns" not in content or "dotDmg" not in content:
        errors.append("Missing DoT (damage over time) mechanism for Skill 5")
    if "isStunned" not in content:
        errors.append("Missing Stun mechanism for Skill 4")
    if "isBlind" not in content:
        errors.append("Missing Blind mechanism for Skill 7")
    if "atkDebuff" not in content and "baseAtk" not in content:
        errors.append("Missing Weaken (-25% ATK) debuff mechanism for Skill 10")
    if "dealAoeDamage" not in content:
        errors.append("Missing dealAoeDamage function for AOE skills")

    # 9. Check Keyboard Shortcuts 1, 2, 3, 4
    for key_code in ["Digit1", "Digit2", "Digit3", "Digit4"]:
        if key_code not in content and f'key === "{key_code[-1]}"' not in content:
            errors.append(f"Missing keyboard shortcut handling for key {key_code[-1]}")

    # 10. Standardized Chemical Terminology Check
    # Verify that 'ester', 'acid', 'alcohol', 'glycerol' are used, not obsolete forms in newly introduced code
    deck_code_match = re.search(r'const SKILL_LIBRARY = \[(.*?)\];', content, re.DOTALL)
    if deck_code_match:
        skill_text = deck_code_match.group(1)
        bad_patterns = [
            (r'\beste\b', "Obsolete term 'este' found in SKILL_LIBRARY (use 'ester')"),
            (r'\baxit\b', "Obsolete term 'axit' found in SKILL_LIBRARY (use 'acid')"),
            (r'\bancol\b', "Obsolete term 'ancol' found in SKILL_LIBRARY (use 'alcohol')"),
            (r'\bglixerol\b', "Obsolete term 'glixerol' found in SKILL_LIBRARY (use 'glycerol')")
        ]
        for pat, err_msg in bad_patterns:
            if re.search(pat, skill_text, re.IGNORECASE):
                errors.append(err_msg)

    # Summary
    if errors:
        print(f"❌ Task 3 & 4 Verification FAILED with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("✅ Task 3 & 4 Verification PASSED! 10 Skills Grimoire, 4-Deck Loadout, Multi-Enemy Target & AOE Engine verified!")
        return True

if __name__ == "__main__":
    success = verify_task3_4()
    sys.exit(0 if success else 1)
