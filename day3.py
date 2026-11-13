# ==============================================================================
# ⚔️ THE 17TH BIRTHDAY CRUCIBLE — QUESTION 01 (Gauntlet Q06 / LeetCode #125)
# Problem: Valid Palindrome
# Author: Rehan Khan (@certifiedtechidiot)
# ==============================================================================
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward
and backward. Alphanumeric characters include letters and numbers.

Given a string s, return True if it is a palindrome, or False otherwise.

CONSTRAINTS & RULES:
1. No string reversal shortcuts: Do NOT use `s[::-1]`.
2. Must use two-pointer technique (left and right moving towards center).
3. Ignore spaces, punctuation, symbols (e.g. ',', ':', '!', etc.).
4. Case-insensitive ('A' == 'a').
"""

def is_palindrome(s: str) -> bool:
    z=[]
    z_reverse=[]
    table=True
    for i in s:
        if i.isalnum():
           z.append(i.lower())
    for q in range(len(z)-1,-1,-1):
        z_reverse.append(z[q])

    for i in range(len(z)):
        if z[i]!=z_reverse[i]:
            table=False
    return table




    
is_palindrome("reh ; ' an")


# ==============================================================================
# 🧪 TEST SUITE (Run `python3 codingsession.py` in your terminal to verify!)
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("ab_a", True),
        ("Was it a car or a cat I saw?", True),
    ]

    print("Running tests for Q06: Valid Palindrome...\n" + "-" * 50)
    all_passed = True

    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = is_palindrome(input_str)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"Test {i}: {status}")
        print(f"  Input:    {repr(input_str)}")
        print(f"  Expected: {expected} | Got: {result}\n")

    if all_passed:
        print("🎉 ALL TESTS PASSED! Crucible Rep 1 / 50 UNLOCKED! 🔥")
    else:
        print("Keep refining your two-pointer logic above!")
