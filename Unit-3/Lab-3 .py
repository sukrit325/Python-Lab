def count_frequencies(text):
  """Counts word frequencies in a text string."""
  words = text.lower().split()
  cleaned_words = [w.strip(".,!?\"'()[]{}:;") for w in words if w.strip()]

  frequency_dict = {}
  for word in cleaned_words:
    frequency_dict[word] = frequency_dict.get(word, 0) + 1

  return frequency_dict


if __name__ == "__main__":
  sample_text = (
      "Python is a powerful programming language. Python is widely used in data"
      " science, web development, and automation. Programming with python is"
      " fun."
  )

  freqs = count_frequencies(sample_text)
  print("\n--- Word Frequency Count ---")
  for word, count in sorted(freqs.items(), key=lambda x: x[1], reverse=True):
    print(f"'{word}': {count}")