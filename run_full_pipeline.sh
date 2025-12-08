#!/bin/bash

echo "===== FAU Generative Pipeline (Week 4 & 5) ====="

echo "▶ Running Week 4 - Improved I2I Refinement"
python src/i2i_week4_refiner.py

echo "▶ Running Week 5 - Real SD-Turbo T2I with FAU Branding"
python src/t2i_week5_real_generator.py

echo "▶ Building Final Promotional Video"
python src/final_promo_builder.py

echo "===== COMPLETED: Full Pipeline Finished Successfully ====="