import requests


def stopwords():
    # Baca file 'indonesia_stopwords.txt' dari URL GitHub untuk mendapatkan stopwords Bahasa Indonesia.
    file_url = "https://raw.githubusercontent.com/teddylee777/langchain-teddynote/main/assets/korean_stopwords.txt"

    # Dapatkan file terminologi dari internet.
    response = requests.get(file_url)
    response.raise_for_status()  # Naikkkan pengecualian jika permintaan HTTP gagal.

    # Dapatkan data teks dari respons.
    stopwords_data = response.text

    # Pisahkan data teks menjadi beberapa baris.
    stopwords = stopwords_data.splitlines()

    # Hapus karakter spasi ekstra (seperti karakter baris baru) dari setiap baris.
    return [word.strip() for word in stopwords]
