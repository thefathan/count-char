from collections import Counter

with open('indonesian-words.txt', 'r') as file:
    string_indonesian_words = file.read().replace('\n', '').replace(' ', '')

with open('javanese-words.txt', 'r') as file:
    string_javanese_words = file.read().replace('\n', '').replace(' ', '')

class Bahasa:
  def __init__(self, words, panjang):
    self.words = words
    self.panjang = panjang

jawa = Bahasa(string_javanese_words, len(string_javanese_words))
indonesia = Bahasa(string_indonesian_words, len(string_indonesian_words))


# Cari huruf terbanyak saat ini
def getMaxOccuringChar(str):

	res = Counter(str)
	res = max(res, key = res.get)
	return res

# hitung huruf dalam string
def countChar(char, string):
    count = 0

    for i in string:
        if i == char:
            count = count + 1
    return count

# Cetak
def printHasil(bahasa_apa, berapa_teratas):
	print("\nUntuk", bahasa_apa, "\nSesuai dengan file yang dimasukkan, maka ", berapa_teratas, " kata terbanyak yang muncul: ")
	if bahasa_apa == "Indonesia":
		for i in range(berapa_teratas):
			print("Huruf terbanyak ke -", i+1, "adalah huruf ",getMaxOccuringChar(indonesia.words), "berjumlah", countChar(getMaxOccuringChar(indonesia.words), indonesia.words), "dengan persentase:", format((countChar(getMaxOccuringChar(indonesia.words), indonesia.words)/indonesia.panjang*100), ".2f"), "%")
			indonesia.words = indonesia.words.replace(getMaxOccuringChar(indonesia.words), '')
	elif bahasa_apa == "Jawa":
		for i in range(berapa_teratas):
			print("Huruf terbanyak ke -", i+1, "adalah huruf ",getMaxOccuringChar(jawa.words), "berjumlah", countChar(getMaxOccuringChar(jawa.words), jawa.words), "dengan persentase:", format((countChar(getMaxOccuringChar(jawa.words), jawa.words)/jawa.panjang*100), ".2f"), "%")
			jawa.words = jawa.words.replace(getMaxOccuringChar(jawa.words), '')
	else:
		print(bahasa_apa, "tidak ada di dalam database internal.")
	
	
# Main
print("Fathan Ananta Nur\n18219008\n")
printHasil("Indonesia", 5)
printHasil("Jawa", 5)
