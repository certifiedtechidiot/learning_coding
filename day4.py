# ==============================================================================
# ⚔️ GAUNTLET Q07 / LEETCODE #443: Run-Length String Compression
# Author: Rehan Khan (@certifiedtechidiot)
# ==============================================================================
"""
Given a string `text`, perform basic run-length compression where consecutive
repeated characters are replaced by the character followed by the count of repetitions.

Examples:
- "aaabbc"        -> "a3b2c1"
- "wwwwaaadexxxxx" -> "w4a3d1e1x5"
- "aabcccccaaa"    -> "a2b1c5a3"
- "a"              -> "a1"
- ""               -> ""

CONSTRAINTS & RULES:
1. No external libraries: Do NOT use `collections.Counter` or `itertools.groupby`.
2. Must iterate through characters and track counts manually with raw loops.
3. Handle the edge case of empty string `""` -> return `""`.
4. Pay special attention to the LAST character group when the loop terminates!
"""
# aabbcc
def compress_string(text: str) -> str:
    if not text:
        return ""

    z = None
    counter = 0
    lst = []
    for i in text:
        if z == None:
            z = i
            counter += 1
        elif i == z:
            counter += 1
            z = i
        else:
            lst.append(f"{z}{counter}")
            z = i
            counter = 1
    lst.append(f"{z}{counter}")
    return "".join(lst)





    



# ==============================================================================
# 🧪 TEST SUITE (Run `python3 codingsession.py` in your terminal to verify!)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        ("aaabbc", "a3b2c1"),
        ("wwwwaaadexxxxx", "w4a3d1e1x5"),
        ("aabcccccaaa", "a2b1c5a3"),
        ("a", "a1"),
        ("abc", "a1b1c1"),
        ("", ""),
    ]

    print("Running tests for Q07: Run-Length String Compression...\n" + "-" * 55)
    all_passed = True

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = compress_string(input_str)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status}")
        print(f"  Input:    {repr(input_str)}")
        print(f"  Expected: {repr(expected)} | Got: {repr(result)}\n")

    if all_passed:
        print("🎉 ALL TESTS PASSED! Gauntlet Q07 UNLOCKED! 🔥")
    else:
        print("Keep refining your compression loop above!")
