# Machine Learning 

This folder contains everything related to Machine Learning. You can find the notebook for this project at `classification.ipynb`.

The saved model is available at the `/sm` directory

Tokenizer used is available as `tokenizer.json`

There are various CSV files in this folder. The details are as follows.

We referenced this paper for this project:
https://www.researchgate.net/publication/340961588_Multilabel_Text_Classification_in_News_Articles_Using_Long-Term_Memory_with_Word2Vec

## Running the notebook
You can run individual cell to train the notebook. All dependencies needed is installed when running the first cell.

## CSV Information
`raw_data/individual dataset` -> This folder contains the raw dataset acquired from the source.

`raw_data/LAPORAN LIST.xlsx` -> This folder contains the compilation of all individual dataset. 

`raw_data/laporan.csv` -> Labeled Report list in CSV form with delimiter character ";".

`cleaned_data/laporan.csv` -> Report text with the same label that has been cleaned, there's no capital alphabet or punctuation.

`cleaned_data/laporanencoded` -> Cleaned report text with every label with their own coloumn.