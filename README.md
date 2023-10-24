# Anime-GAN
Convert photorealistic images to Anime images

## Set up
1. Make sure you have python installed. I used python `3.10` Visit [Python Downloads](https://www.python.org/downloads/) to get python.
2. Clone this repository
```
git clone https://github.com/omkarbhale/anime-gan
```
3. Create a virtual environment and install requirements
```
python -m venv venv                 <- Create venv
venv\Scripts\activate.bat           <- Use this venv
pip install -r requirements.txt     <- Install requirements
```
4. Start the web server: While using this venv, start the server
```
python server.py
```
5. To test the functionality, you may use index,html

## Did i make it?
This converter is based on the original [Hugging Face web demo](https://huggingface.co/spaces/akhaliq/AnimeGANv2), created by [@ak92501](https://twitter.com/ak92501/) using the AI model created by [@bryandlee](https://github.com/bryandlee/animegan2-pytorch), which uses training techniques developed by [Xin Chen](https://github.com/TachibanaYoshino/AnimeGANv2). I created this site so that users can convert their image to an anime/cartoon style without uploading their images to a server - it's completely free. The conversion process is done in your browser (using your device's CPU/GPU) so your images remain private.

Have fun! :)
