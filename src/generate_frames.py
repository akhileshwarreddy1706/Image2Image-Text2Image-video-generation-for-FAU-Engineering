# Week 2 placeholder implementation for frame generation

import os

def generate_frames(prompt="FAU Engineering Week 2 Demo",
                    num_frames=3,
                    output_dir="results/week2_frames"):
    """
    Week 2 requirement:
    - Create placeholder frames
    - Prepare pipeline structure for Week 3
    """
    os.makedirs(output_dir, exist_ok=True)

    print(f"[Week 2] Creating {num_frames} placeholder frames...")

    # Create dummy frame files to simulate output
    for i in range(num_frames):
        frame_path = os.path.join(output_dir, f"frame_{i}.txt")
        with open(frame_path, "w") as f:
            f.write(f"Placeholder frame {i} for prompt: {prompt}")

    print(f"[Week 2] Frames saved under {output_dir}")

if __name__ == "__main__":
    generate_frames()