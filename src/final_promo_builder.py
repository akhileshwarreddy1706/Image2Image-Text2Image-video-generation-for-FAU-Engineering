"""
final_promo_builder.py

Creates the complete FAU Promotional Video with exact timing:
1. Title slide (1.5 sec)
2. Week 5 real T2I slideshow (4 images x 1s)
3. Week 4 I2I slideshow (all images, total 2.5s)
4. Dataset slideshow (6 images x 1s)
5. End slide (1.5 sec)
6. Merge everything into final_promo_video.mp4
"""

import os
import subprocess
from PIL import Image

def make_slideshow(image_paths, output_file, seconds_per_image, size=(512, 512)):
    print(f"[Slideshow] Building {output_file} using {len(image_paths)} images")

    if not image_paths:
        print(f"[Slideshow] ERROR: No images found for {output_file}")
        return

    temp_dir = "results/_temp_slides"
    os.makedirs(temp_dir, exist_ok=True)

    for f in os.listdir(temp_dir):
        os.remove(os.path.join(temp_dir, f))

    frames = []
    for idx, img_path in enumerate(image_paths):
        img = Image.open(img_path).convert("RGB").resize(size)
        frame_path = os.path.join(temp_dir, f"frame_{idx:03d}.png")
        img.save(frame_path)
        frames.append(os.path.abspath(frame_path))

    concat_file = os.path.join(temp_dir, "list.txt")
    with open(concat_file, "w") as f:
        for frame in frames:
            f.write(f"file '{frame}'\n")
            f.write(f"duration {seconds_per_image}\n")
        f.write(f"file '{frames[-1]}'\n")

    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_file,
        "-pix_fmt", "yuv420p",
        "-r", "25",
        output_file,
    ]

    subprocess.run(cmd, check=True)
    print(f"[Slideshow] Saved → {output_file}")

def make_title_slide():
    print("[Title] Creating title_slide.mp4")

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", "color=c=blue:s=512x512:d=1.5:r=25",
        "-vf",
        "drawtext=text='FAU Engineering Promotional Video':"
        "fontfile=/System/Library/Fonts/Helvetica.ttc:fontsize=30:fontcolor=white:"
        "x=(w-text_w)/2:y=(h-text_h)/2",
        "results/title_slide.mp4",
    ]

    subprocess.run(cmd, check=True)
    print("[Title] Done → results/title_slide.mp4")

def make_end_slide():
    print("[End] Creating end_slide.mp4")

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "lavfi",
        "-i", "color=c=navy:s=512x512:d=1.5:r=25",
        "-vf",
        "drawtext=text='Thank You - FAU Engineering':"
        "fontfile=/System/Library/Fonts/Helvetica.ttc:fontsize=28:fontcolor=white:"
        "x=(w-text_w)/2:y=(h-text_h)/2",
        "results/end_slide.mp4",
    ]

    subprocess.run(cmd, check=True)
    print("[End] Done → results/end_slide.mp4")

def collect_images(directory, max_images=None):
    valid_ext = (".jpg", ".jpeg", ".png")
    if not os.path.isdir(directory):
        return []

    imgs = [
        os.path.join(directory, f)
        for f in sorted(os.listdir(directory))
        if f.lower().endswith(valid_ext)
    ]
    if max_images:
        imgs = imgs[:max_images]
    return imgs

def merge_videos(video_list, output_path):
    print("\n[Merging] Combining all MP4 clips...")

    concat_file = "results/concat_list.txt"
    with open(concat_file, "w") as f:
        for vid in video_list:
            f.write(f"file '{os.path.abspath(vid)}'\n")

    cmd = [
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", concat_file,
        "-c", "copy",
        output_path,
    ]

    subprocess.run(cmd, check=True)
    print(f"[Merging] Final video saved → {output_path}")
    os.remove(concat_file)

def assemble_final_video():
    print("\n===== BUILDING FINAL PROMOTIONAL VIDEO =====")
    os.makedirs("results", exist_ok=True)

    make_title_slide()

    t2i_imgs = collect_images("results/week5_t2i_real")
    make_slideshow(t2i_imgs, "results/week5_real_slideshow.mp4", seconds_per_image=1)

    i2i_imgs = collect_images("results/week4_i2i")
    if len(i2i_imgs) > 0:
        seconds_per_i2i = 2.5 / len(i2i_imgs)
        make_slideshow(i2i_imgs, "results/week4_i2i_slideshow.mp4", seconds_per_image=seconds_per_i2i)

    dataset_imgs = collect_images("dataset/fau_images", max_images=6)
    make_slideshow(dataset_imgs, "results/dataset_slideshow.mp4", seconds_per_image=1)

    make_end_slide()

    final_order = [
        "results/title_slide.mp4",
        "results/week5_real_slideshow.mp4",
        "results/week4_i2i_slideshow.mp4",
        "results/dataset_slideshow.mp4",
        "results/end_slide.mp4",
    ]

    merge_videos(final_order, "results/final_promo_video.mp4")

    print("\n===== DONE! Open results/final_promo_video.mp4 =====")

if __name__ == "__main__":
    assemble_final_video()