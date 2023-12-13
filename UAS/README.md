# UAS spk_web

## Install requirements

    pip install -r requirements.txt

## Run the app
to run the web app simply  use

    python main.py

## Usage
Install postman 
https://www.postman.com/downloads/

get laptop list
<img src='img/Screenshot SPK UAS(2).png' alt='laptop list'/>

get recommendations saw
<img src='img/Screenshot SPK UAS(9).png' alt='recommendations saw'/>

get recommendations wp
<img src='img/Sreenshot SPK UAS(10).png' alt='recommendations wp'/>

### TUGAS UAS
Implementasikan model yang sudah anda buat ke dalam web api dengan http method `POST`

INPUT:
{
    "harga": 1, 
    "ram": 2, 
    "kapasitas_baterai": 5, 
    "processor": 3, 
    "penyimpanan_internal": 4
}

OUTPUT (diurutkan / sort dari yang terbesar ke yang terkecil):

post recommendations saw
<img src='img/Sreenshot SPK UAS(11).png' alt='recommendations saw'/>

post recommendations wp
<img src='img/Sreenshot SPK UAS(12).png' alt='recommendations wp'/>
