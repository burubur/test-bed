import subprocess
import sys

def test_app():
    print("Testing app.py...")
    try:
        # Run app.py and capture output
        result = subprocess.run(['python3', 'app.py'], capture_output=True, text=True, timeout=5)
        if "The sum of 10 and 5 is: 15" in result.stdout:
            print("✅ app.py: Fixed!")
            return True
        else:
            print(f"❌ app.py: Bug still exists. Output: {result.stdout.strip()}")
            return False
    except Exception as e:
        print(f"❌ app.py: Execution failed: {e}")
        return False

def test_utils():
    print("Testing utils.py...")
    try:
        with open('utils.py', 'r') as f:
            content = f.read()
            # Check if the triplicate print is gone
            if 'print("[INFO] " + text)\n    print("[INFO] " + text)\n    print("[INFO] " + text)' in content:
                print("❌ utils.py: Redundancy still exists!")
                return False
            else:
                print("✅ utils.py: Refactored!")
                return True
    except Exception as e:
        print(f"❌ utils.py: Analysis failed: {e}")
        return False

if __name__ == "__main__":
    app_ok = test_app()
    utils_ok = test_utils()
    
    if app_ok and utils_ok:
        print("\n🎉 ALL TESTS PASSED")
        sys.exit(0)
    else:
        print("\n🚨 SOME TESTS FAILED")
        sys.exit(1)
