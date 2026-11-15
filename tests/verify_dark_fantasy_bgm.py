# -*- coding: utf-8 -*-
"""
Verification suite for:
1. Dark Fantasy BGM Synthesizer (Web Audio API Engine).
2. Continuous playback across the entire game (start on user gesture and loop seamlessly).
3. Volume Control Slider and Mute/Unmute Toggle with localStorage persistence.
4. Responsive UI & CSS styling on Desktop and Mobile.
"""
import re

def test_dark_fantasy_bgm():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    print("🎵 Verifying Dark Fantasy BGM Engine, Continuous Loop & Volume Control...")

    # 1. Check DarkFantasyBGM definition & methods
    assert "const DarkFantasyBGM = {" in html, "DarkFantasyBGM object must be defined"
    assert "isPlaying:" in html, "Must have isPlaying state"
    assert "volume:" in html, "Must have volume property"
    assert "setVolume(val)" in html, "Must have setVolume method"
    assert "start()" in html, "Must have start method"
    assert "stop()" in html, "Must have stop method"
    assert "schedule()" in html, "Must have lookahead scheduler method"
    assert "playStep(" in html, "Must have playStep sequencer"

    # 2. Check 4 Cinematic Layers
    assert "playBassDrone(" in html, "Must have deep drone & cello layer"
    assert "playDungeonPulse(" in html, "Must have subterranean war drum / heartbeat pulse"
    assert "playGothicPluck(" in html, "Must have gothic lute/harp/music box plucking layer"
    assert "playChoirSwell(" in html, "Must have ethereal choir swell layer"

    # 3. Check D Minor Harmonic scale and 8-bar progression
    assert "CHORDS:" in html, "Must define harmonic chord progression"
    assert "ARP_PATTERNS:" in html, "Must define arpeggio melodic patterns"

    # 4. Check UI elements in HTML
    assert 'id="audioControlBar"' in html, "Must have audioControlBar element"
    assert 'id="btnSound"' in html, "Must have btnSound toggle button"
    assert 'id="bgmVolumeSlider"' in html, "Must have bgmVolumeSlider range slider"
    assert 'id="volNum"' in html, "Must have volNum percentage display"

    # 5. Check CSS styling for audio bar & volume slider
    assert ".audio-control-bar" in html, "CSS for .audio-control-bar must exist"
    assert ".volume-slider-box" in html, "CSS for .volume-slider-box must exist"
    assert "#bgmVolumeSlider::-webkit-slider-thumb" in html, "Custom thumb styling must exist"
    assert "header.menu-open .header-actions" in html, "Mobile header actions must support audio bar"

    # 6. Check continuous playback triggers
    assert "function tryStartBGMOnUserGesture()" in html, "tryStartBGMOnUserGesture function must exist"
    assert 'document.addEventListener("click", tryStartBGMOnUserGesture' in html, "Must listen on click"
    assert 'document.addEventListener("touchstart", tryStartBGMOnUserGesture' in html, "Must listen on touchstart"
    assert 'document.addEventListener("keydown", tryStartBGMOnUserGesture' in html, "Must listen on keydown"
    assert 'document.addEventListener("visibilitychange"' in html, "Must handle visibility change"

    # 7. Check Volume slider and localStorage persistence
    assert 'localStorage.getItem("esterQuest_bgmVolume")' in html, "Must load saved volume from localStorage"
    assert 'localStorage.setItem("esterQuest_bgmVolume"' in html, "Must save volume to localStorage"
    assert 'bgmVolumeSlider.addEventListener("input"' in html, "Must listen to input event on volume slider"

    # 8. Check window global export
    assert "window.DarkFantasyBGM = DarkFantasyBGM;" in html, "Must export DarkFantasyBGM globally"

    print("🎉 ALL DARK FANTASY BGM VERIFICATION CHECKS PASSED! ⚔️🎵")

if __name__ == "__main__":
    test_dark_fantasy_bgm()
