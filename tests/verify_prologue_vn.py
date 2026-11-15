# -*- coding: utf-8 -*-
"""
Verification script for Visual Novel Prologue Storyline:
- 3 visual novel scenes with corresponding images:
  * assets/prologue_1_peace.jpg (Khởi nguyên hoàng kim)
  * assets/prologue_2_chaos.jpg (Hiểm họa vực thẳm hỗn mang)
  * assets/prologue_3_hero.jpg (Lời sấm truyền & sứ mệnh hiệp sĩ)
- Step progression (Image -> Click -> Text -> Click -> Next Image...)
- Reuses classic story text dialogues
- Keyboard shortcuts and responsive styles
"""
import os
import re

def verify_prologue_vn():
    print("🎬 Verifying Visual Novel Prologue Implementation...")

    # 1. Check Image Assets exist in assets/
    required_images = [
        "assets/prologue_1_peace.jpg",
        "assets/prologue_2_chaos.jpg",
        "assets/prologue_3_hero.jpg"
    ]
    for img_path in required_images:
        assert os.path.exists(img_path), f"Missing image asset: {img_path}"
        assert os.path.getsize(img_path) > 100000, f"Image {img_path} is suspiciously small"
    print("  ✅ All 3 prologue visual novel images exist with valid file sizes.")

    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 2. Check Visual Novel HTML elements
    vn_elements = [
        'id="prologueOverlay"',
        'id="vnBackdrop"',
        'id="vnSlide0"',
        'id="vnSlide1"',
        'id="vnSlide2"',
        'id="vnTopBar"', # or vn-top-bar
        'id="vnChapterBadgeText"',
        'id="vnProgressDots"',
        'id="btnSkipPrologue"',
        'id="vnClickHint"',
        'id="vnDialogueBox"',
        'id="vnTag"',
        'id="vnTagIcon"',
        'id="vnTagLabel"',
        'id="vnSceneTitle"',
        'id="vnNarrativeText"',
        'id="vnCallout"',
        'id="vnPromptContinue"',
        'id="btnEnterWorld"'
    ]
    for el in vn_elements:
        if el.startswith('id="'):
            id_name = el.split('"')[1]
            assert f'id="{id_name}"' in html, f"Missing VN element with ID: {id_name}"
    print("  ✅ All Visual Novel UI structure elements exist.")

    # 3. Check PROLOGUE_VN_SCENES data array in JS
    assert "PROLOGUE_VN_SCENES" in html, "Must define PROLOGUE_VN_SCENES"
    assert "assets/prologue_1_peace.jpg" in html, "Scene 1 must use prologue_1_peace.jpg"
    assert "assets/prologue_2_chaos.jpg" in html, "Scene 2 must use prologue_2_chaos.jpg"
    assert "assets/prologue_3_hero.jpg" in html, "Scene 3 must use prologue_3_hero.jpg"
    assert "Vương Quốc Ester" in html, "Must preserve story text 'Vương Quốc Ester'"
    assert "Vực Thẳm Hỗn Mang" in html, "Must preserve story text 'Vực Thẳm Hỗn Mang'"
    assert "Đại Ma Vương" in html, "Must preserve story text 'Đại Ma Vương'"
    assert "thanh kiếm tri thức" in html, "Must preserve story text 'thanh kiếm tri thức'"
    print("  ✅ PROLOGUE_VN_SCENES data array and story text dialogues verified.")

    # 4. Check VN step progression logic
    assert "function renderVNStep" in html, "Must implement renderVNStep()"
    assert "function advanceVN" in html, "Must implement advanceVN()"
    assert "function handleVNOverlayClick" in html, "Must implement handleVNOverlayClick()"
    assert "function handleVNDialogueClick" in html, "Must implement handleVNDialogueClick()"
    assert "vnState" in html, "Must track vnState with sceneIndex and textVisible"
    print("  ✅ Visual Novel step progression logic verified.")

    # 5. Check Keyboard navigation & Replay
    assert 'e.code === "Space"' in html or 'e.key === " "' in html, "Must support Space key for next step"
    assert 'e.code === "Enter"' in html or 'e.key === "Enter"' in html, "Must support Enter key for next step"
    assert 'e.code === "Escape"' in html or 'e.key === "Escape"' in html, "Must support Escape key to skip"
    assert 'btnReplayPrologue' in html, "Must support replay from menu"
    assert 'btnHeaderPrologue' in html, "Must support replay from header"
    print("  ✅ Keyboard navigation and replay buttons verified.")

    # 6. Check CSS Visual Novel styling
    css_checks = [
        ".vn-backdrop",
        ".vn-bg-slide",
        ".vn-dialogue-box",
        ".vn-click-hint",
        ".btn-prologue-enter",
        ".btn-skip-prologue"
    ]
    for sel in css_checks:
        assert sel in html, f"Missing CSS selector {sel}"
    print("  ✅ Visual Novel CSS styling verified.")

    print("\n🎉 ALL VISUAL NOVEL PROLOGUE VERIFICATION CHECKS PASSED! 🎬✨")

if __name__ == "__main__":
    verify_prologue_vn()
