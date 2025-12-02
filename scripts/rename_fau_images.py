import os
import shutil

src_folder = "temp_uploads"
dst_folder = "dataset/fau_images"

os.makedirs(dst_folder, exist_ok=True)

# Get all images in upload folder
images = sorted([
    f for f in os.listdir(src_folder)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

# Ensure exactly 16
print("Found", len(images), "images")
if len(images) != 16:
    raise ValueError(f"Expected 16 images, found {len(images)}")

for idx, img_name in enumerate(images, start=1):
    ext = img_name.split(".")[-1].lower()
    new_name = f"fau_{idx:02d}.{ext}"
    
    src = os.path.join(src_folder, img_name)
    dst = os.path.join(dst_folder, new_name)

    shutil.copy(src, dst)
    print(f"Copied: {src} -> {dst}")

print("\nDataset created successfully!")