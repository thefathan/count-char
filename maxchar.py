with open('textsample.txt', 'r') as file:
    string = file.read().replace('\n', '').replace(' ', '')

ASCII_SIZE = 256
panjangtext = len(string)

# Cari huruf terbanyak saat ini
def getMaxOccuringChar(str):

	count = [0] * ASCII_SIZE
	max = -1
	c = ''

	for i in str:
		count[ord(i)]+=1

	for i in str:
		if max < count[ord(i)]:
			max = count[ord(i)]
			c = i
	return c

# hitung huruf dalam string
def countChar(char):
    count = 0

    for i in string:
        if i == char:
            count = count + 1
    return count

# Cetak
print("Sesuai dengan file yang dimasukkan, maka: ")
for i in range(5):
    print("Huruf terbanyak ke -", i+1, "adalah huruf ",getMaxOccuringChar(string), "berjumlah", countChar(getMaxOccuringChar(string)), "dengan persentase:", format((countChar(getMaxOccuringChar(string))/panjangtext*100), ".2f"), "%")
    string = string.replace(getMaxOccuringChar(string), '')
