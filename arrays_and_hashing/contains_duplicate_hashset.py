def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

nums = (1,2,3,4,5,6,7,1)

print(f"{containsDuplicate(nums)}")

# in this question we have used hash set that is a very imp concept
# ⚡ O(1) average lookup time (very fast search)
# 🔁 Automatically removes duplicates
# 🧠 Easy duplicate detection (if num in set)
# ⏹️ Early exit possible (stops as soon as duplicate found)
# 📦 Efficient for membership checking
# 🔄 No need for nested loops (avoids O(n²))
# 🏗️ Foundation for many DSA problems
#  ⚙️ Easy to use (built-in in Python)

# Disadvantages (quick)
# ❌ Uses extra memory (O(n))
# ❌ Unordered (no indexing)


# 🚀 Set Functions (Quick Notes)
# ➕ Add
# add(x) → add single element
# update(iterable) → add multiple elements

# ❌ Remove
# remove(x) → removes (error if not present)
# discard(x) → removes (no error) ✅
# pop() → removes random element
# clear() → removes all elements

# 🔍 Check
# x in set → check if element exists
# len(set) → number of elements