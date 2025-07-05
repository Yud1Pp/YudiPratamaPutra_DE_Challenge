# ================================================================
# Deskripsi:
#   Script ini digunakan untuk menampilkan gambar dari dataset
#   anotasi YOLO lengkap dengan bounding box dan label kelasnya.
#
# Cara Menjalankan:
# 1. Pastikan struktur folder seperti berikut:
#    Challenge3/
#    ├── Labeled_Dataset/
#    │   ├── image1.jpg
#    │   ├── image1.txt
#    │   └── ...
#    └── preview_dataset.py
# 
# 2. Lalu pada terminal jangan lupa untuk masuk ke direktori Challenge3 dengan "cd Challenge3"
#
# 3. Pastikan library berikut sudah terinstal:
#    pip install opencv-python matplotlib
#
# 4. Jalankan script dengan perintah:
#    python preview_dataset.py
#
# 5. Ubah variabel `num_samples` untuk mengatur jumlah gambar
#    yang ingin ditampilkan secara acak dari folder dataset.
#
# ================================================================

# Import library yang diperlukan
import os
import cv2
import matplotlib.pyplot as plt
import random

# Folder berisi gambar dan file label (format YOLO)
dataset_dir = 'Labeled_Dataset'

# Jumlah gambar yang ingin ditampilkan (ubah sesuai kebutuhan)
num_samples = 5

# Daftar nama kelas sesuai class_id di YOLO label
class_names = [
    'gloves',
    'hard_hat',
    'person',
    'safety_glasses',
    'safety_vest',
    'steel_toe_boots'
]

# Fungsi untuk menampilkan gambar dan bounding box label
def show_image_with_labels(image_path, label_path):
    # Baca gambar
    image = cv2.imread(image_path)
    if image is None:
        print(f"Gagal membuka gambar: {image_path}")
        return
    
    # Konversi BGR ke RGB untuk matplotlib
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    h, w, _ = image.shape

    if not os.path.exists(label_path):
        print(f"Tidak ada label untuk {os.path.basename(image_path)}")
        return

    # Baca file label
    with open(label_path, 'r') as f:
        lines = f.readlines()

    # Proses setiap baris label
    for line in lines:
        # Pisahkan baris menjadi bagian-bagian
        parts = line.strip().split()
        class_id = int(parts[0])
        
        # variabel untuk koordinat bounding box
        x_center, y_center, bbox_width, bbox_height = map(float, parts[1:])

        # Konversi dari format YOLO ke pixel koordinat
        x1 = int((x_center - bbox_width / 2) * w)
        y1 = int((y_center - bbox_height / 2) * h)
        x2 = int((x_center + bbox_width / 2) * w)
        y2 = int((y_center + bbox_height / 2) * h)

        # Annotasi bounding box pada gambar
        label = class_names[class_id]
        color = (255, 0, 0)
        cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Tampilkan hasil anotasi
    plt.figure(figsize=(10, 8))
    plt.imshow(image)
    plt.title(os.path.basename(image_path))
    plt.axis('off')
    plt.show()

# Ambil semua file gambar di folder
files = os.listdir(dataset_dir)
image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]

# Random sample sebanyak num_samples supaya gambar yang ditampilkan acak
sampled_images = random.sample(image_files, min(num_samples, len(image_files)))

# Tampilkan gambar yang sudah dipilih secara acak
for img_file in sampled_images:
    img_path = os.path.join(dataset_dir, img_file)
    label_file = os.path.splitext(img_file)[0] + '.txt'
    label_path = os.path.join(dataset_dir, label_file)
    show_image_with_labels(img_path, label_path)
