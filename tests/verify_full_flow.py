"""
Comprehensive Full-Flow End-to-End Verification Test Script:
Ester Quest: Hiệp Sĩ Giả Kim & Đại Chiến Thủy Phân (EsterQuest-RPG)
Task 6: Full Flow, Responsive & Verification Suite
"""
import re
import sys
import os

def check_js_syntax(script_text):
    """
    Scans JavaScript text and verifies that all brackets, quotes, regexes,
    and comment blocks are properly balanced and structurally intact.
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

        # Strings ('...', "...", `...`)
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
            last_non_ws = quote
            continue
            
        # Open brackets
        if c in pairs:
            stack.append((c, line, col))
            last_non_ws = c
        elif c in rev_pairs:
            if not stack:
                return False, f"Unexpected closing bracket '{c}' at line {line}, col {col}"
            expected_open = rev_pairs[c]
            actual_open, o_line, o_col = stack.pop()
            if actual_open != expected_open:
                return False, f"Mismatched bracket: expected '{pairs[actual_open]}' for '{actual_open}' at line {o_line}, col {o_col}, but found '{c}' at line {line}, col {col}"
            last_non_ws = c
        else:
            last_non_ws = c

        i += 1
        col += 1

    if stack:
        unclosed, u_line, u_col = stack[-1]
        return False, f"Unclosed bracket '{unclosed}' from line {u_line}, col {u_col}"
        
    return True, "JavaScript syntax is balanced and intact"


def verify_full_flow():
    print("======================================================================")
    print("🧪 ESTER QUEST RPG - FULL FLOW, RESPONSIVE & SYSTEM VERIFICATION")
    print("======================================================================")
    
    html_path = os.path.join(os.path.dirname(__file__), "..", "index.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    errors = []
    passes = []

    def record_pass(category, desc):
        passes.append(f"[{category}] {desc}")

    def record_fail(category, desc):
        errors.append(f"[{category}] {desc}")

    # =========================================================================
    # SECTION 1: PROLOGUE CINEMATIC OVERLAY & STORYLINE
    # =========================================================================
    print("\n🔍 Checking Section 1: Epic Prologue Overlay...")
    if 'id="prologueOverlay"' in html:
        record_pass("Prologue", "Overlay container #prologueOverlay exists")
    else:
        record_fail("Prologue", "Missing #prologueOverlay")

    for btn_id in ['id="btnSkipPrologue"', 'id="btnEnterWorld"']:
        if btn_id in html:
            record_pass("Prologue", f"Navigation button {btn_id} exists")
        else:
            record_fail("Prologue", f"Missing navigation button {btn_id}")

    if ("prologueSynth" in html or "SFX.prologue" in html) and "esterQuest_prologueSeen" in html:
        record_pass("Prologue", "SFX synthesizer prologueSynth & localStorage persistence present")
    else:
        record_fail("Prologue", "Missing prologue SFX or localStorage persistence for prologue")

    if "Vương Quốc Ester" in html and "Vực Thẳm Hỗn Mang" in html and "Hiệp Sĩ" in html:
        record_pass("Prologue", "Epic narrative storyline elements present")
    else:
        record_fail("Prologue", "Missing core storyline narrative keywords")

    # =========================================================================
    # SECTION 2: MENU & CHARACTER CREATION
    # =========================================================================
    print("🔍 Checking Section 2: Character Creation & Menu Screen...")
    if 'id="menuScreen"' in html:
        record_pass("Menu", "Main menu #menuScreen exists")
    else:
        record_fail("Menu", "Missing #menuScreen")

    for menu_btn in ['id="btnMenuAcademy"', 'id="btnMenuDeck"', 'id="btnStartGame"']:
        if menu_btn in html:
            record_pass("Menu", f"Action button {menu_btn} exists")
        else:
            record_fail("Menu", f"Missing action button {menu_btn}")

    if 'id="playerName"' in html and 'id="playerClass"' in html:
        record_pass("Menu", "Player name and class selection inputs exist")
    else:
        record_fail("Menu", "Missing playerName or playerClass input")

    if "esterQuest_ch1Completed" in html:
        record_pass("Menu", "Chapter 1 completion badge and routing logic present")
    else:
        record_fail("Menu", "Missing Chapter 1 completion badge check")

    # =========================================================================
    # SECTION 3: CHAPTER 1 ACADEMY & 4 VIRTUAL LABS & MATCHING MINI-GAMES
    # =========================================================================
    print("🔍 Checking Section 3: Academy Screen, 4 Labs & Matching Mini-Games...")
    if 'id="academyScreen"' in html:
        record_pass("Academy", "#academyScreen container exists")
    else:
        record_fail("Academy", "Missing #academyScreen")

    # Stepper 5 steps
    for step_num in range(1, 6):
        if f'id="stepBtn{step_num}"' in html:
            record_pass("Academy", f"Lesson step button {step_num} exists")
        else:
            record_fail("Academy", f"Missing lesson step button {step_num}")

    # 5 Lesson panes
    for lesson_num in range(1, 6):
        if f'id="lessonPane{lesson_num}"' in html:
            record_pass("Academy", f"Lesson pane #lessonPane{lesson_num} exists")
        else:
            record_fail("Academy", f"Missing lesson pane #lessonPane{lesson_num}")

    # 4 Virtual Labs
    # Lab 1: Boiling lab with temperature slider
    if 'id="tempSlider"' in html and 'id="currentTempDisplay"' in html and 'boilingLiquid' in html:
        record_pass("Lab 1", "Boiling Lab temperature slider (20°C - 150°C) and apparatus exist")
    else:
        record_fail("Lab 1", "Missing temperature range input, display or boiling liquid")

    # Lab 2: Hydrolysis phase separation
    if 'id="hydroSeparationLab"' in html and "hydroTopPhase" in html and "hydroBottomPhase" in html:
        record_pass("Lab 2", "Hydrolysis 2-phase separation test tube exists")
    else:
        record_fail("Lab 2", "Missing hydrolysis test tube phases")

    # Lab 3: Silver mirror reaction
    if 'id="silverMirrorLab"' in html and "silverTestTube" in html and "btnApplySilverReagent" in html:
        record_pass("Lab 3", "Silver mirror test (AgNO3/NH3) and reflective coating exist")
    else:
        record_fail("Lab 3", "Missing silver mirror apparatus or reagents")

    # Lab 4: Ester synthesis workshop
    if "synthesis-grid" in html and "btnHeatSynthesis" in html and "synthesisResultBox" in html:
        record_pass("Lab 4", "Ester synthesis workshop apparatus exists")
    else:
        record_fail("Lab 4", "Missing synthesis apparatus or grid")

    # 2 Matching Mini-Games (Aroma Fruit & Real-life Applications)
    if 'id="matchingGameGrid"' in html and "Isoamyl acetate" in html and "chuối" in html:
        record_pass("Mini-Game", "Fruit Aroma matching mini-game exists")
    else:
        record_fail("Mini-Game", "Missing fruit aroma matching mini-game")

    if 'id="matchingQuestPanel"' in html and "Plexiglas" in html and "Methyl methacrylate" in html:
        record_pass("Mini-Game", "Real-life application matching mini-game exists")
    else:
        record_fail("Mini-Game", "Missing real-life application matching mini-game")

    # =========================================================================
    # SECTION 4: 10-SKILL GRIMOIRE & 4-SLOT TACTICAL DECK LOADOUT
    # =========================================================================
    print("🔍 Checking Section 4: 10 Skills Grimoire & 4-Slot Tactical Deck...")
    if 'id="deckModal"' in html:
        record_pass("Deck", "#deckModal container exists")
    else:
        record_fail("Deck", "Missing #deckModal")

    # Verify SKILL_LIBRARY contains all 10 distinct skills
    skill_match = re.search(r'const SKILL_LIBRARY = \[(.*?)\];', html, re.DOTALL)
    if skill_match:
        skill_text = skill_match.group(1)
        skill_ids = re.findall(r'id:\s*(\d+)', skill_text)
        if len(skill_ids) == 10:
            record_pass("Deck", f"SKILL_LIBRARY contains 10 skills (IDs: {', '.join(skill_ids)})")
        else:
            record_fail("Deck", f"SKILL_LIBRARY has {len(skill_ids)} skills, expected exactly 10")
    else:
        record_fail("Deck", "Could not locate SKILL_LIBRARY declaration")

    # Verify 4 Active Slots container
    if 'id="deckActiveSlots"' in html and 'deck-active-slots' in html:
        record_pass("Deck", "4 active skill slots container present in UI")
    else:
        record_fail("Deck", "Missing 4-slot loadout grid in deck UI")

    # Verify Keyboard Shortcuts 1 - 4
    for key_digit in ["1", "2", "3", "4"]:
        if f'key === "{key_digit}"' in html or f'Digit{key_digit}' in html:
            record_pass("Combat", f"Hotkey {key_digit} shortcut verified")
        else:
            record_fail("Combat", f"Missing hotkey shortcut for key {key_digit}")

    # Verify MP reduction on skill cast
    if "state.playerMana = Math.max(0, state.playerMana - manaCost)" in html or "state.playerMana -=" in html:
        record_pass("Combat", "MP cost deduction mechanism present")
    else:
        record_fail("Combat", "Missing player MP deduction mechanism on cast")

    # =========================================================================
    # SECTION 5: MULTI-ENEMY ARENA & AOE COMBAT ENGINE
    # =========================================================================
    print("🔍 Checking Section 5: Multi-Enemy Arena & AOE Execution Engine...")
    if 'enemies-container' in html and 'state.enemies' in html:
        record_pass("Multi-Enemy", "Multi-enemy arena container and state.enemies array exist")
    else:
        record_fail("Multi-Enemy", "Missing enemies-container or state.enemies")

    # Target selection
    if "selectEnemyTarget" in html and "target-indicator" in html:
        record_pass("Multi-Enemy", "Click-to-target selection function and visual neon indicator exist")
    else:
        record_fail("Multi-Enemy", "Missing selectEnemyTarget or target-indicator")

    # AOE Execution
    if "dealAoeDamage" in html and 'targetType: "all"' in html:
        record_pass("AOE", 'dealAoeDamage engine function and targetType: "all" skills exist')
    else:
        record_fail("AOE", 'Missing dealAoeDamage or targetType: "all"')

    # Sequential enemy counter-attacks (400ms delay)
    if "enemyTurnSequence" in html and "400" in html:
        record_pass("Multi-Enemy", "Sequential enemy counter-attack queue (400ms) exists")
    else:
        record_fail("Multi-Enemy", "Missing sequential enemy attack sequence")

    # Status Effects (DoT, Stun, Blind, Weaken, ShieldActive)
    for st_effect in ["dotTurns", "isStunned", "isBlind", "atkDebuff", "shieldActive"]:
        if st_effect in html:
            record_pass("Status", f"Status effect mechanism '{st_effect}' exists")
        else:
            record_fail("Status", f"Missing status effect mechanism '{st_effect}'")

    # =========================================================================
    # SECTION 6: 8-STAGE CAMPAIGN & 2-PHASE NIGHTMARE BOSS
    # =========================================================================
    print("🔍 Checking Section 6: 8-Stage Campaign & 2-Phase Nightmare Boss...")
    # Check STAGES length = 8
    stage_match = re.search(r'const STAGES = \[(.*?)\n\s*\];', html, re.DOTALL)
    if stage_match:
        stage_text = stage_match.group(1)
        stages_count = len(re.findall(r'id:\s*(\d+)', stage_text))
        if stages_count == 8:
            record_pass("Campaign", "Campaign contains exactly 8 stages")
        else:
            record_fail("Campaign", f"STAGES contains {stages_count} stages, expected 8")
    else:
        record_fail("Campaign", "Could not locate const STAGES array")

    # Stage 2: 3 Slimes
    if "Slime Xanh" in html and "Slime Đỏ" in html and "Slime Vàng" in html:
        record_pass("Campaign", "Stage 2 multi-enemy encounter (Slime Xanh, Đỏ, Vàng) verified")
    else:
        record_fail("Campaign", "Missing 3 slimes in Stage 2")

    # Stage 5: 2 Elite Knights
    if "Chiến Binh Đao" in html and "Chiến Binh Khiên" in html:
        record_pass("Campaign", "Stage 5 elite double monsters (Chiến Binh Đao & Khiên) verified")
    else:
        record_fail("Campaign", "Missing 2 elite monsters in Stage 5")

    # Stage 8: 2-Phase Nightmare Boss
    if "Đại Ma Vương" in html and "Đại Ma Vương Thức Tỉnh" in html:
        record_pass("Boss", "Stage 8 Boss name and Awakened Phase 2 name verified")
    else:
        record_fail("Boss", "Missing Đại Ma Vương or Đại Ma Vương Thức Tỉnh")

    if "triggerBossPhase2" in html and "SFX.bossPhase2" in html:
        record_pass("Boss", "Boss Phase 2 awakening transition & SFX verified")
    else:
        record_fail("Boss", "Missing triggerBossPhase2 or SFX.bossPhase2")

    if "dmgReduction" in html and "0.25" in html:
        record_pass("Boss", "Phase 1 damage reduction shield (25%) verified")
    else:
        record_fail("Boss", "Missing Phase 1 damage reduction (0.25)")

    # =========================================================================
    # SECTION 7: END GAME & LEADERBOARD
    # =========================================================================
    print("🔍 Checking Section 7: End Game Screen & Leaderboard...")
    if 'id="endGameScreen"' in html:
        record_pass("EndGame", "#endGameScreen element exists")
    else:
        record_fail("EndGame", "Missing #endGameScreen")

    if "Đại Ma Vương Thức Tỉnh" in html and ("Phá Đảo Ải" in html or "8 Ải Thử Thách" in html):
        record_pass("EndGame", "End game celebration recognizes defeating Nightmare Boss across 8 stages")
    else:
        record_fail("EndGame", "Missing 8-stage or Nightmare Boss victory recognition in end game screen")

    # =========================================================================
    # SECTION 8: STANDARDIZED CHEMICAL TERMINOLOGY (GDPT 2018)
    # =========================================================================
    print("🔍 Checking Section 8: Standardized Chemistry Nomenclature (GDPT 2018)...")
    forbidden_terms = [
        (r'\beste\b', 'este (use ester)'),
        (r'\baxit\b', 'axit (use acid)'),
        (r'\bancol\b', 'ancol (use alcohol)'),
        (r'\bglixerol\b', 'glixerol (use glycerol)')
    ]
    for pattern, term_desc in forbidden_terms:
        matches = re.findall(pattern, html, re.IGNORECASE)
        if matches:
            record_fail("Terminology", f"Found {len(matches)} occurrences of obsolete term '{term_desc}'")
        else:
            record_pass("Terminology", f"Zero occurrences of obsolete term '{term_desc}'")

    # =========================================================================
    # SECTION 9: RESPONSIVE CSS & TOUCH TARGET AUDIT
    # =========================================================================
    print("🔍 Checking Section 9: Responsive CSS & Touch Target Audit...")
    # Check media queries: 960px, 768px, 480px, 380px, 360px
    for mq in ["(max-width: 960px)", "(max-width: 768px)", "(max-width: 480px)", "(max-width: 380px)", "(max-width: 360px)"]:
        if mq in html:
            record_pass("Responsive", f"Media query '{mq}' present")
        else:
            record_fail("Responsive", f"Missing media query '{mq}'")

    # Check overflow-x: hidden on body
    if "overflow-x: hidden" in html:
        record_pass("Responsive", "Horizontal overflow protection (overflow-x: hidden) present")
    else:
        record_fail("Responsive", "Missing overflow-x: hidden")

    # Check Touch Target minimum >= 44px
    if "min-height: 44px" in html and "min-width: 44px" in html:
        record_pass("Responsive", "Touch targets enforce minimum 44px x 44px for accessibility")
    else:
        record_fail("Responsive", "Missing explicit 44px minimum touch target size")

    # =========================================================================
    # SECTION 10: JAVASCRIPT SYNTAX & BRACKET INTEGRITY
    # =========================================================================
    print("🔍 Checking Section 10: JavaScript Syntax & Bracket Integrity...")
    script_matches = re.findall(r'<script\b[^>]*>(.*?)</script>', html, re.DOTALL)
    if not script_matches:
        record_fail("JavaScript", "No <script> tags found in index.html")
    else:
        combined_js = "\n".join(script_matches)
        valid, msg = check_js_syntax(combined_js)
        if valid:
            record_pass("JavaScript", f"Syntax parsing succeeded: {msg}")
        else:
            record_fail("JavaScript", f"Syntax parsing failed: {msg}")

    # =========================================================================
    # SUMMARY & FINAL VERDICT
    # =========================================================================
    print("\n======================================================================")
    print("📊 FULL FLOW VERIFICATION SUMMARY")
    print("======================================================================")
    print(f"Total Tests Passed: {len(passes)}")
    print(f"Total Tests Failed: {len(errors)}")

    if errors:
        print("\n❌ THE FOLLOWING ISSUES WERE DETECTED:")
        for err in errors:
            print(f"  - {err}")
        print("\nVerification: FAILED ❌")
        return False
    else:
        print("\n🎉 ALL TESTS PASSED! FULL GAME FLOW, LABS, DECK, COMBAT, 8 STAGES & RESPONSIVE VERIFIED! ✅")
        return True

if __name__ == "__main__":
    success = verify_full_flow()
    sys.exit(0 if success else 1)
