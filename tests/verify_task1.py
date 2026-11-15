"""
Verification script for Task 1: Epic Prologue Intro Overlay
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
                    # consume flags
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

def verify_task1(filepath="index.html"):
    print(f"Reading {filepath}...")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    errors = []

    # 1. Check prologueOverlay element
    if 'id="prologueOverlay"' not in content:
        errors.append("Missing id='prologueOverlay'")

    # 2. Check main buttons
    required_ids = [
        ("btnEnterWorld", "TIẾP TỤC BƯỚC VÀO THẾ GIỚI ➔"),
        ("btnSkipPrologue", "Bỏ Qua ⏩"),
        ("btnReplayPrologue", "Xem Lại Cốt Truyện 🎬 trên menuScreen"),
        ("btnHeaderPrologue", "Nút Cốt Truyện trên header"),
        ("prologueAudioTip", "Audio Tip hint"),
    ]
    for btn_id, desc in required_ids:
        if f'id="{btn_id}"' not in content:
            errors.append(f"Missing id='{btn_id}' ({desc})")

    # 3. Check storyline text content
    story_keywords = [
        "Vương Quốc Ester",
        "Vực Thẳm Hỗn Mang",
        "Đại Ma Vương",
        "biến dị",
        "thanh kiếm tri thức",
        "thủy phân",
        "xà phòng hóa",
        "Hiệp Sĩ"
    ]
    for kw in story_keywords:
        if kw not in content:
            errors.append(f"Story keyword '{kw}' missing from prologue content")

    # 4. Check SFX methods
    sfx_methods = ["prologueSynth", "prologueEnter", "prologueSkip"]
    for method in sfx_methods:
        if method not in content:
            errors.append(f"Missing SFX method: {method}")

    # 5. Check JS functions
    js_functions = ["openPrologue", "closePrologue", "playPrologueAudioOnFirstGesture"]
    for fn in js_functions:
        if f"function {fn}" not in content and f"{fn} =" not in content and f"{fn}(" not in content:
            errors.append(f"Missing JS function: {fn}")

    # 6. Check CSS styles
    css_selectors = [
        ".prologue-overlay",
        ".btn-skip-prologue",
        ".btn-prologue-enter",
        ".floating-crystal",
        "@media (max-width: 600px)"
    ]
    for sel in css_selectors:
        if sel not in content:
            errors.append(f"Missing CSS rule or selector: {sel}")

    # 7. Check for JavaScript basic syntax errors
    script_match = re.search(r'<script>(.*?)</script>', content, re.DOTALL)
    if script_match:
        raw_script = script_match.group(1)
        valid, msg = check_js_syntax(raw_script)
        if not valid:
            errors.append(f"JS syntax check error: {msg}")

    # 8. Check that newly added IDs in getElementById exist in HTML
    ids_in_html = set(re.findall(r'id=["\']([A-Za-z0-9_-]+)["\']', content))
    prologue_ids = ["btnEnterWorld", "btnSkipPrologue", "btnReplayPrologue", "btnHeaderPrologue", "prologueOverlay", "prologueAudioTip"]
    for pid in prologue_ids:
        if pid not in ids_in_html:
            errors.append(f"ID '{pid}' not found in HTML elements")

    if errors:
        print("❌ Verification FAILED with errors:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("✅ Task 1 Verification PASSED! All elements, scripts, styles, and story texts are present.")
        return True

if __name__ == "__main__":
    success = verify_task1()
    sys.exit(0 if success else 1)
