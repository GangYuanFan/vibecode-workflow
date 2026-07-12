#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path

# Configuration
# Mandatory artifacts for a compliant project.
REQUIRED_ARTIFACTS = [
    "BLUEPRINT.md", 
    "DEBT.md", 
    "ARCHITECTURE.md", 
    "DECISIONS.md", 
    "PROGRESS.md", 
    "AI_RULES.md"
]
PHASE_TAG_PATTERN = re.compile(r"\[CURRENT_PHASE: \d+\]")
PONYTAIL_PATTERN = re.compile(r"ponytail:")

def check_artifacts():
    print("🔍 Checking for required artifacts...")
    missing = []
    for art in REQUIRED_ARTIFACTS:
        if not Path(art).exists():
            missing.append(art)
    
    if missing:
        print(f"❌ Missing artifacts: {', '.join(missing)}")
        return False
    print("✅ All required artifacts found.")
    return True

def scan_for_debt():
    print("🔍 Scanning code for unlogged ponytail shortcuts...")
    debt_found = False
    debt_file = Path("DEBT.md")
    
    # Files to scan (common code extensions)
    extensions = {".js", ".ts", ".py", ".cpp", ".h", ".go", ".rs", ".java", ".php"}
    
    for path in Path(".").rglob("*"):
        if path.suffix in extensions and "node_modules" not in str(path):
            try:
                content = path.read_text(errors="ignore")
                if PONYTAIL_PATTERN.search(content):
                    print(f"💡 Found ponytail shortcut in {path}")
                    debt_found = True
            except Exception as e:
                print(f"⚠️ Could not read {path}: {e}")

    if debt_found:
        if not debt_file.exists() or debt_file.stat().st_size == 0:
            print("❌ Ponytail shortcuts found but DEBT.md is empty or missing!")
            return False
        else:
            print("✅ Ponytail shortcuts found and DEBT.md exists.")
            return True
    else:
        print("✅ No ponytail shortcuts found in code.")
        return True

def verify_logs(log_path):
    print(f"🔍 Verifying phase tags in {log_path}...")
    try:
        content = Path(log_path).read_text()
        tags = PHASE_TAG_PATTERN.findall(content)
        if not tags:
            print("❌ No [CURRENT_PHASE: X] tags found in logs!")
            return False
        
        # Check for phase skipping (very basic check)
        phases = [int(t.split(":")[1].strip("]")) for t in tags]
        # Check if any phase jumps by more than 1 (ignoring 0)
        for i in range(len(phases)-1):
            if phases[i+1] - phases[i] > 1:
                print(f"⚠️ Warning: Phase jump detected from {phases[i]} to {phases[i+1]}")
        
        print(f"✅ Found {len(tags)} phase tags.")
        return True
    except Exception as e:
        print(f"❌ Error reading logs: {e}")
        return False

def main():
    # Usage: python vibecode-check.py [log_file]
    log_file = sys.argv[1] if len(sys.argv) > 1 else None
    
    success = True
    
    if not check_artifacts():
        success = False
    
    if not scan_for_debt():
        success = False
        
    if log_file:
        if not verify_logs(log_file):
            success = False
            
    if success:
        print("\n✨ Protocol Compliance: PASSED")
        sys.exit(0)
    else:
        print("\n🚨 Protocol Compliance: FAILED")
        sys.exit(1)

if __name__ == "__main__":
    main()
