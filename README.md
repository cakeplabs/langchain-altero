# langchain-altero

Berbagai paket Python utilitas yang digunakan dalam tutorial LangChain Bahasa Indonesia.

Paket-paket ini menyediakan fungsionalitas tambahan yang mungkin tidak nyaman saat menggunakan LangChain.

## Overview

`langchain_altero` is a localized version of the [`langchain-teddynote`](https://github.com/teddylee777/langchain-teddynote) library, designed to be fully open-source under the AGPL-3.0 license. This library has been adapted to better suit the needs of our specific audience while retaining the core functionality of the original `langchain-teddynote` package.

### Output streaming

Menyediakan fungsi `stream_response` untuk output streaming.

```python
from langchain_teddynote.messages import stream_response
from langchain_openai import ChatOpenAI

# Membuat sebuah objek
llm = ChatOpenAI(
    temperatur = 0.1, # kreativitas (0.0 ~ 2.0)
    model_name = "gpt-4o-mini", # nama model
    api_key=api_key # 
)
answer = llm.stream("Tolong beritahu saya 10 tempat terindah di Korea dan alamatnya!")

# hanya untuk output streaming
stream_response(jawaban)

# jika Anda ingin mendapatkan jawaban yang outputnya sebagai return value
# final_answer = stream_response(answer, return_output=True)
```
Output
```
1.**Bali**
    - **Alamat:** Bali, Indonesia
    - Deskripsi: Terkenal dengan pantainya yang indah, budaya yang kaya, dan pemandangan alam yang menakjubkan.
```

## License

Proyek ini dilisensikan di bawah Lisensi AGPL-3.0 - lihat file [LICENSE](./LICENSE) untuk detail lebih lanjut.