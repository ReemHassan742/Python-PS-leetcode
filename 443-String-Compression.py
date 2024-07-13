class Solution:
  def compress(self, chars: List[str]) -> int:
    track = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0

      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[track] = letter
      track += 1

      if count > 1:
        for c in str(count):
          chars[track] = c
          track += 1

    return track
        