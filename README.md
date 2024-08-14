# langchain-altero

Various utility Python packages used in LangChain Bahasa Indonesia tutorials.

They provide additional functionality that may be inconvenient while using LangChain.

## Overview

`langchain_altero` adalah versi lokal dari library [`langchain-teddynote`](https://github.com/teddylee777/langchain-teddynote), yang dirancang untuk menjadi sumber terbuka di bawah lisensi AGPL-3.0. Pustaka ini telah diadaptasi agar lebih sesuai dengan kebutuhan audiens khusus kami sambil mempertahankan fungsionalitas inti dari paket `langchain-teddynote` yang asli.

### Output streaming

Menyediakan fungsi `stream_response` untuk output streaming.

```python
from langchain_teddynote.messages import stream_response
from langchain_openai import ChatOpenAI

# Membuat sebuah objek
llm = ChatOpenAI(
    temperatur = 0.1, # kreativitas (0.0 ~ 2.0)
    model_name = "gpt-4o-mini", # nama model
    api_key=api_key # api key openai
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
