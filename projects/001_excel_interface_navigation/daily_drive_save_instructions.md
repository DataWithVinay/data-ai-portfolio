# Daily Drive Saving Instructions — Day 01

## ChatGPT cannot directly create files in your Google Drive from this chat.
Use this flow:

1. Download this ZIP from ChatGPT.
2. Upload it to:
   `DataWithVinay_Content_Factory/01_Daily_Content/2026-06-20_day01_excel_interface_navigation/`
3. Extract it in Drive or on your computer.
4. Upload/extract contents into the same Drive folder.

## Colab Drive Connection

Open Google Colab and run:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Then use this output folder:

```python
BASE_DIR = "/content/drive/MyDrive/DataWithVinay_Content_Factory/07_Datasets/day01_excel_interface_navigation"
```

Run the generated notebook/code:
- `day01_dataset_generator.ipynb`
- or `dataset_generation_colab_code.py`

## GitHub Upload

Upload these into:

```text
data-ai-portfolio/projects/001_excel_interface_navigation/
```

Recommended public files:
- README.md
- business_problem.md
- learning_notes.md
- data_dictionary.md
- datasets/*.csv
- scripts/dataset_generation_colab_code.py
- linkedin/linkedin_post.md
- linkedin/image_prompts.md
- notes/pdf_revision_notes.md
```
