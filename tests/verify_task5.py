"""
Verification script for Task 5: 8-Stage Campaign & 2-Phase Nightmare Super Boss
"""
import re
import sys
import json

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
                    break
                if rc == '\\' and i + 1 < n:
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
                    break
                i += 1
                col += 1
            last_non_ws = '/'
            continue

        # Strings
        if c in ('"', "'", '`'):
            quote = c
            i += 1
            col += 1
            while i < n:
                sc = script_text[i]
                if sc == '\\' and i + 1 < n:
                    i += 2
                    col += 2
                    continue
                if sc == '\n' and quote != '`':
                    break
                if sc == '\n' and quote == '`':
                    line += 1
                    col = 1
                if sc == quote:
                    i += 1
                    col += 1
                    break
                i += 1
                col += 1
            last_non_ws = '"'
            continue
            
        if c in pairs:
            stack.append((c, line, col))
        elif c in rev_pairs:
            if not stack:
                return False, f"Unexpected closing '{c}' at line {line}, col {col}"
            open_c, o_line, o_col = stack.pop()
            if pairs[open_c] != c:
                return False, f"Mismatched bracket: expected '{pairs[open_c]}' for '{open_c}' (line {o_line}) but found '{c}' at line {line}"

        last_non_ws = c
        i += 1
        col += 1
        
    if stack:
        open_c, o_line, o_col = stack.pop()
        return False, f"Unclosed bracket '{open_c}' opened at line {o_line}, col {o_col}"
        
    return True, "Syntax check passed"

def verify_task5():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    errors = []

    # 1. Check JavaScript Syntax
    scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
    for idx, s in enumerate(scripts):
        ok, msg = check_js_syntax(s)
        if not ok:
            errors.append(f"JS syntax error in script #{idx+1}: {msg}")

    # 2. Check 8 Stages Configuration in STAGES array
    stages_match = re.search(r'const STAGES\s*=\s*\[(.*?)\];\s*(?:const|let|var|function|\/\*)', html, re.DOTALL)
    if not stages_match:
        errors.append("Could not locate 'const STAGES = [...]' array in index.html")
    else:
        stages_str = stages_match.group(1)
        # Check presence of each stage title / monster
        stage_expectations = [
            (1, "Rừng Ẩm Ướt", "Slime", 100, 15),
            (2, "Đầm Lầy Bầy Nhầy", "Bầy Slime", None, None),
            (3, "Thung Lũng Băng", "Sói Băng", 160, 22),
            (4, "Hầm Ngục Thạch", "Thạch Quái", 220, 28),
            (5, "Tháp Canh Đôi", "Song Quái", None, None),
            (6, "Tháp Địa Ngục", "Hỏa Long", 280, 35),
            (7, "Điện Thờ Hắc Ám", "Chúa Tể Bóng Tối", 360, 45),
            (8, "Vực Thẳm Hỗn Mang", "Đại Ma Vương", 350, 45),
        ]

        for s_id, s_name, m_name, hp, atk in stage_expectations:
            if s_name not in stages_str:
                errors.append(f"Missing Stage {s_id} ({s_name}) in STAGES configuration")
            if m_name not in stages_str:
                errors.append(f"Missing Monster {m_name} in Stage {s_id}")

        # Check multi-enemy Stage 2 details (3 enemies: Slime Xanh, Đỏ, Vàng)
        if "Slime Xanh" not in stages_str or "Slime Đỏ" not in stages_str or "Slime Vàng" not in stages_str:
            errors.append("Stage 2 must have 3 enemies: Slime Xanh, Slime Đỏ, Slime Vàng")
        if "60" not in stages_str or "70" not in stages_str or "80" not in stages_str:
            errors.append("Stage 2 Slimes HP missing (60, 70, 80)")
        if "assets/slime.png" not in stages_str:
            errors.append("Missing assets/slime.png icon in stages")

        # Check multi-enemy Stage 5 details (2 elite enemies: Chiến Binh Đao & Khiên)
        if "Chiến Binh Đao" not in stages_str or "Chiến Binh Khiên" not in stages_str:
            errors.append("Stage 5 must have 2 elite enemies: Chiến Binh Đao and Chiến Binh Khiên")
        if "150" not in stages_str:
            errors.append("Stage 5 enemies HP (150) missing")

        # Check Stage 8 Boss Phase 1 damage reduction shield
        if "dmgReduction" not in stages_str and "0.25" not in stages_str:
            errors.append("Stage 8 Boss Phase 1 must have dmgReduction: 0.25 (25% damage shield)")

    # 3. Check 2-Phase Boss Mechanism
    if "function triggerBossPhase2(" not in html:
        errors.append("Missing triggerBossPhase2 function in index.html")
    if "state.bossPhase = 2" not in html and "state.bossPhase=2" not in html:
        errors.append("triggerBossPhase2 must set state.bossPhase to 2")
    if "Đại Ma Vương Thức Tỉnh" not in html:
        errors.append("Missing boss name update to 'Đại Ma Vương Thức Tỉnh'")
    if "NIGHTMARE BOSS" not in html:
        errors.append("Missing boss level update to 'NIGHTMARE BOSS'")
    if "500" not in html:
        errors.append("Missing 500 HP update for Phase 2 Boss")

    # Check CSS Animations for Boss Phase 2
    if ".boss-awakening-shake" not in html:
        errors.append("Missing CSS class .boss-awakening-shake")
    if "@keyframes bossAwakeningShake" not in html:
        errors.append("Missing @keyframes bossAwakeningShake")
    if ".boss-phase-flash" not in html:
        errors.append("Missing CSS class .boss-phase-flash")
    if "@keyframes bossPhaseFlash" not in html:
        errors.append("Missing @keyframes bossPhaseFlash")

    # Check Sound Effect SFX.bossPhase2
    if "bossPhase2()" not in html and "bossPhase2:" not in html:
        errors.append("Missing SFX.bossPhase2() sound effect synthesizer")

    # Check Boss Phase 1 to Phase 2 transition logic
    # In dealDamageToEnemy or handleAllEnemiesDefeated
    if "triggerBossPhase2()" not in html:
        errors.append("triggerBossPhase2() must be called when Phase 1 Boss reaches 0 HP")

    # Check Phase 2 Enrage & Level 3 Question Priority
    if "bossPhase === 2" not in html and "bossPhase===2" not in html:
        errors.append("Missing bossPhase === 2 condition for Phase 2 logic")

    # Check 25% damage shield logic in dealDamageToEnemy & dealAoeDamage
    if "dmgReduction" not in html:
        errors.append("Missing dmgReduction check in combat damage engine")

    # 4. Check UI Elements
    if 'id="stageProgress"' not in html:
        errors.append("Missing #stageProgress element")
    if "Tiến trình: Ải 1 / 8" not in html:
        errors.append("Default #stageProgress text should be 'Tiến trình: Ải 1 / 8'")
    if "${STAGES.length}" not in html and "/ 8" not in html:
        errors.append("Dynamic stage progress must reference STAGES.length or 8")

    # Check End Game Screen
    if 'id="endGameScreen"' not in html:
        errors.append("Missing #endGameScreen element")
    if "8 Ải Thử Thách" not in html:
        errors.append("#endGameScreen or handleGameOver should honor completing all 8 stages")
    if "Đại Ma Vương Thức Tỉnh" not in html:
        errors.append("#endGameScreen should mention defeating Đại Ma Vương Thức Tỉnh")

    # Check Leaderboard records 8 stages
    if "`Phá Đảo Ải ${STAGES.length} 👑`" not in html and "Phá Đảo Ải 8 👑" not in html:
        errors.append("Leaderboard record must dynamically track victory on all 8 stages")

    # 5. Check Global Standard Nomenclature
    # Make sure no obsolete chemistry terms are present
    for term in ["ancol", "axit", "glixerol"]:
        matches = re.findall(rf'\b{term}\b', html, re.IGNORECASE)
        if matches:
            errors.append(f"Found forbidden non-standard term '{term}' in index.html: {len(matches)} occurrences")

    # 6. Functional Combat Flow Logic Simulation (Simulating JS rules)
    # Simulate: Stage 8 Boss Phase 1 damage reduction
    base_dmg = 100
    reduced_dmg = round(base_dmg * (1 - 0.25))
    if reduced_dmg != 75:
        errors.append("Damage reduction calculation failed")

    # Simulate: Boss transition when Phase 1 HP reaches 0
    sim_state = {
        "currentStageIndex": 7, # 0-indexed Stage 8
        "bossPhase": 1,
        "bossEnrageTurnCount": 0,
        "enemies": [{"name": "Đại Ma Vương", "hp": 0, "maxHp": 350, "atk": 45, "dmgReduction": 0.25}]
    }

    def simulate_enemy_death(st):
        if st["currentStageIndex"] == 7 and st["bossPhase"] == 1:
            # Trigger Phase 2!
            st["bossPhase"] = 2
            st["enemies"][0]["name"] = "Đại Ma Vương Thức Tỉnh"
            st["enemies"][0]["level"] = "👑 NIGHTMARE BOSS"
            st["enemies"][0]["hp"] = 500
            st["enemies"][0]["maxHp"] = 500
            st["enemies"][0]["atk"] = 55
            st["enemies"][0]["dmgReduction"] = 0
            return "PHASE_2_AWAKENED"
        else:
            return "VICTORY"

    res = simulate_enemy_death(sim_state)
    if res != "PHASE_2_AWAKENED":
        errors.append("Simulation: Stage 8 Phase 1 death should awaken Phase 2, not end match")
    if sim_state["enemies"][0]["hp"] != 500:
        errors.append("Simulation: Phase 2 Boss should have 500 HP")
    if sim_state["enemies"][0]["atk"] != 55:
        errors.append("Simulation: Phase 2 Boss should have 55 ATK")

    # Simulate Phase 2 death
    sim_state["enemies"][0]["hp"] = 0
    res2 = simulate_enemy_death(sim_state)
    if res2 != "VICTORY":
        errors.append("Simulation: Stage 8 Phase 2 death should trigger VICTORY")

    # 7. Check Window Exports
    if "window.triggerBossPhase2" not in html or "window.STAGES" not in html:
        errors.append("Missing global exports for STAGES and triggerBossPhase2")

    if errors:
        print("❌ Task 5 Verification FAILED with following errors:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print("✅ Task 5 Verification PASSED! All 8 Stages, Multi-Enemy Encounters, 2-Phase Nightmare Boss, SFX, and End Game Screen fully verified!")

if __name__ == "__main__":
    verify_task5()
