import os
import shutil

# --- Pfade anpassen ---
jpeg_folder = "path goes here"
raw_source_folder = "path goes here"
raw_target_folder = "path goes here"

# Zielordner anlegen, falls er nicht existiert
# os.makedirs(raw_target_folder, exist_ok=True)

# Alle JPEG-Dateien im JPEG-Ordner durchgehen
for filename in os.listdir(jpeg_folder):
    if filename.lower().endswith(".jpg"):
        base_name = os.path.splitext(filename)[0]  # z.B. DSCF1234
        raw_filename = base_name + ".RAF"

        raw_source_path = os.path.join(raw_source_folder, raw_filename)
        raw_target_path = os.path.join(raw_target_folder, raw_filename)

        if os.path.exists(raw_source_path):
            shutil.copy2(raw_source_path, raw_target_path)
            print(f"Copied: {raw_filename}")
        else:
            print(f"RAW not found: {raw_filename}")

print("Done.")
