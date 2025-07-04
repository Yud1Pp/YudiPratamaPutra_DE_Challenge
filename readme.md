# ML Data Engineer Challenge

**PT Synapsis Sinergi Digital**

## Deskripsi Singkat

Challenge ini bertujuan untuk membangun sistem AI berbasis computer vision guna mendeteksi pelanggaran penggunaan **Personal Protective Equipment (PPE)** oleh personil berdasarkan footage CCTV. PPE yang wajib dikenakan meliputi:

* Hard Hat
* Safety Vest
* Gloves
* Safety Glasses
* Steel-Toe Boots

---

## ✅ Checklist Fitur yang Telah Dikerjakan

| Fitur                           | Status | Keterangan Kendala                                |
| ------------------------------- | ------ | ------------------------------------------------- |
| Skema Labeling dan Pertimbangan | ✅ Done | -                                                 |
| Panduan Anotasi                 | ✅ Done | -                                                 |
| Dataset gambar Tanpa Anotasi    | ✅ Done | Seleksi dan kurasi manual dari SH17 dan Pinterest |
| Dataset gambar dengan Anotasi   | ✅ Done | Semua gambar dianotasi ulang dengan tool Roboflow |
| Dataset Preview Script          | ✅ Done | Sudah disertakan dengan penjelasan penggunaan     |
| Dataset Summary Statistics      | ✅ Done | Dihitung menggunakan script Python                |
| Dokumentasi Isu Teknis          | ✅ Done | Terdapat pada file `issues.pdf`              |

---

## 📁 Struktur Folder Repository

```
ML-PPE-Detection-Challenge/
│
├── Challenge1_AnnotationPlanning/
│   └── annotation_planning.pdf
│
├── Challenge2_DatasetSelection/
│   ├── images/  # Gambar yang telah dipilih
│   └── dataset_selection_note.pdf
│
├── Challenge3_DatasetLabelling/
│   ├── Labeled_Dataset/
│   │   ├── *.jpg
│   │   └── *.txt
│   ├── preview_dataset.py
│   └── issues.pdf
│
└── README.md
```

---

## 🚀 Cara Menjalankan Script

### 📌 Persiapan

Pastikan Anda memiliki Python dan library berikut:

* Python 3.7+
* OpenCV (`opencv-python`)
* Matplotlib

Instalasi (jika belum install):

```bash
pip install opencv-python matplotlib
```

### ▶️ Menjalankan Preview Bounding Box

Untuk melihat hasil anotasi pada gambar:

```bash
python preview_dataset.py
```

* Gambar ditampilkan secara acak.
* Jumlah gambar dapat diatur dengan variabel `num_samples` dalam script.

## 🛠️ Dokumentasi Isu

* Dataset SH17 memiliki banyak kelas yang tidak sesuai dengan skema labeling. Oleh karena itu, diputuskan untuk menyaring dan hanya menggunakan gambar yang relevan.
* Anotasi asli SH17 tidak dapat digunakan langsung sehingga dilakukan **anotasi manual ulang** menggunakan Roboflow.
* Banyak gambar tambahan dikumpulkan dari **Pinterest** dengan keyword pencarian spesifik untuk masing-masing PPE.
* Total 50 gambar dikumpulkan dan dianotasi ulang sesuai skema YOLO.

Detail isu selengkapnya berada pada file: `Challenge3_DatasetLabelling/issues_notes.md`

---