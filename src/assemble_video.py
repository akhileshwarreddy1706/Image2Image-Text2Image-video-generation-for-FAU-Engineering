"""
assemble_video.py

Universal video assembly tool for Weeks 3, 4, and 5.
Automatically detects frame prefixes (t2i_*, i2i_*, fau_week5_real_*)
so it works on ANY computer with ANY filenames.

Primary:
- Uses ffmpeg to produce MP4.
Fallback:
- Uses GIF if ffmpeg is missing or fails.
"""

import os
import subprocess
import imageio.v2 as imageio
import re

def detect_prefix(frame_dir: str) -> str:
    """
    Detect prefix by removing only the FINAL numeric component.
    Examples:
        t2i_0.png  → t2i_
        i2i_2.png  → i2i_
        fau_week5_real_01.png → fau_week5_real_
    """
    for f in sorted(os.listdir(frame_dir)):
        if f.lower().endswith(".png"):
            name = f.split(".")[0]  # remove extension
            # remove ONLY the trailing digits using regex
            prefix = re.sub(r"\d+$", "", name)
            return prefix
    return "frame_"


def frames_to_video(frame_dir: str, output_file: str, fps: int = 2):
    """
    Convert frames in frame_dir into a video (MP4 or GIF fallback).
    """
    print(f"\n[Video] Assembling frames from: {frame_dir}")

    # collect frames
    frames = sorted(
        os.path.join(frame_dir, f)
        for f in os.listdir(frame_dir)
        if f.lower().endswith(".png")
    )

    if not frames:
        print(f"[Video] No PNG frames found in: {frame_dir}")
        return

    # detect the prefix dynamically
    prefix = detect_prefix(frame_dir)
    print(f"[Video] Detected prefix → '{prefix}'")

    # ffmpeg expects %d pattern
    # detect if filenames use 2-digit numbering
    first_frame = frames[0]
    if re.search(r"\d{2}\.png$", first_frame):
         # use padded 2-digit format for ffmpeg
        frame_pattern = os.path.join(frame_dir, f"{prefix}%02d.png")
    else:
        # normal 1-digit
        frame_pattern = os.path.join(frame_dir, f"{prefix}%d.png")

    # attempt MP4
    try:
        print("[Video] Attempting MP4 creation via ffmpeg...")

        cmd = [
            "ffmpeg",
            "-y",
            "-framerate", str(fps),
            "-i", frame_pattern,
            "-pix_fmt", "yuv420p",
            output_file,
        ]

        subprocess.run(cmd, check=True)
        print(f"[Video] MP4 saved → {output_file}")
        return

    except Exception as e:
        print("[Video] ⚠ ffmpeg failed → using GIF fallback.")
        print("        Error:", e)

    # GIF fallback
    gif_output = output_file.replace(".mp4", ".gif")
    print(f"[Video] Creating GIF instead → {gif_output}")

    images = [imageio.imread(f) for f in frames]
    imageio.mimsave(gif_output, images, duration=1.0 / fps)

    print(f"[Video] GIF saved → {gif_output}")


def assemble_final_video():
    """
    Creates Week 4 T2I, Week 4 I2I, and Week 5 real T2I demo videos.
    """

    print("\n===== FINAL VIDEO ASSEMBLY (WEEK 4 + WEEK 5) =====")

    frames_to_video(
        frame_dir="results/week4_t2i",
        output_file="results/week4_t2i_demo.mp4",
        fps=2,
    )

    frames_to_video(
        frame_dir="results/week4_i2i",
        output_file="results/week4_i2i_demo.mp4",
        fps=2,
    )

    frames_to_video(
        frame_dir="results/week5_t2i_real",
        output_file="results/week5_real_demo.mp4",
        fps=1,
    )

    print("\n[FINAL] All demo videos generated successfully.")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "assemble":
        assemble_final_video()
    else:
        # Week 3 default
        frames_to_video(
            frame_dir="results/week3_frames",
            output_file="results/week3_demo.mp4",
            fps=2,
        )