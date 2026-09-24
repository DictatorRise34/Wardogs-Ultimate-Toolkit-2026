"""
WARDOGS Ultimate Assistant — Lightweight launcher stub.
Full tool build is distributed via the Releases tab.
"""

BANNER = r"""
 __      __            _   _
 \ \    / /           | | | |
  \ \  / /_ _ _ __  __| | | | ___   __ _ ___
   \ \/ / _` | '__/ _` | | |/ _ \ / _` / __|
    \  / (_| | | | (_| | | | (_) | (_| \__ \
     \/ \__,_|_|  \__,_|_|_|\___/ \__, |___/
                                   __/ |
                                  |___/
"""

FEATURES = [
    ("📦 Resources", "Unlimited Resources / Credits", "Ctrl+Num 1 / Ctrl+Num 2"),
    ("🔧 Utility",   "Toggle All / Panic Key",        "Ctrl+Num 3 / Ctrl+Num 4"),
    ("⚡ Movement",  "Speed Hack / Super Jump",       "Num * / Num /"),
    ("🗺️ Radar",     "Radar Hack",                    "Num -"),
    ("🧱 Wallhack",  "Wallhack / Glow ESP",           "Num 0 / Num +"),
    ("👁️ ESP",       "Player / Vehicle / Item ESP",   "Num 7 / Num 8 / Num 9"),
    ("🔫 Weapons",   "Ammo / Reload / Recoil / OHK",  "Num 3 – Num 6"),
    ("🛡️ Survival",  "Unlimited Health / God Mode",   "Num 1 / Num 2"),
]


def main() -> None:
    print(BANNER)
    print("[INFO] WARDOGS Ultimate Assistant — launcher stub")
    print("─" * 58)
    for category, feature, hotkey in FEATURES:
        print(f"{category:<16} | {feature:<34} | {hotkey}")
    print("─" * 58)
    print("📦 Full build is distributed via the Releases tab.")


if __name__ == "__main__":
    main()