package main

func uniqueMorseRepresentations(words []string) int {
	letters := []string{".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."}
	m := make(map[string]int)

	for _, word := range words {
		s := ""
		for _, char := range word {
			s += letters[char-'a']
		}
		m[s]++
	}
	return len(m)
}
