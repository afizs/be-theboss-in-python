{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 105. Generate Subtitles for YouTube Video"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import youtube_dl\n",
    "\n",
    "ydl_opts = {\n",
    "    'format': 'bestaudio/best',\n",
    "    'postprocessors': [{\n",
    "        'key': 'FFmpegExtractAudio',\n",
    "        'preferredcodec': 'mp3',\n",
    "        'preferredquality': '192',\n",
    "    }],\n",
    "    'outtmpl': '%(id)s.%(ext)s',\n",
    "}\n",
    "with youtube_dl.YoutubeDL(ydl_opts) as ydl:\n",
    "    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'upload_url': 'https://cdn.assemblyai.com/upload/c0afa8a7-09d5-4fe5-8fb6-4a22be40ce12'}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from config import api_key\n",
    "filename = \"BaW_jenozKc.mp3\"\n",
    "def read_file(filename, chunk_size=5242880):\n",
    "    with open(filename, 'rb') as _file:\n",
    "        while True:\n",
    "            data = _file.read(chunk_size)\n",
    "            if not data:\n",
    "                break\n",
    "            yield data\n",
    "\n",
    "headers = {'authorization': api_key}\n",
    "response = requests.post('https://api.assemblyai.com/v2/upload',\n",
    "                        headers=headers,\n",
    "                        data=read_file(filename))\n",
    "\n",
    "print(response.json())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "🟢 Hope you like this program! 📚  \n",
    "🟡 Follow → @itsafiz"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'upload_url': 'https://cdn.assemblyai.com/upload/c0afa8a7-09d5-4fe5-8fb6-4a22be40ce12'}\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from config import api_key\n",
    "filename = \"BaW_jenozKc.mp3\"\n",
    "def read_file(filename, chunk_size=5242880):\n",
    "    with open(filename, 'rb') as _file:\n",
    "        while True:\n",
    "            data = _file.read(chunk_size)\n",
    "            if not data:\n",
    "                break\n",
    "            yield data\n",
    "\n",
    "headers = {'authorization': api_key}\n",
    "response = requests.post('https://api.assemblyai.com/v2/upload',\n",
    "                        headers=headers,\n",
    "                        data=read_file(filename))\n",
    "\n",
    "print(response.json())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "transcript_id = 'remn3gxlay-66a1-450f-adca-f899954f69c0'\n",
      "Getting the transcription result ....\n",
      "Getting the transcription result ....\n",
      "('This is a test video for you to BL. For more information, contact PH. '\n",
      " 'Ihagsphihag Dot.')\n"
     ]
    }
   ],
   "source": [
    "from pprint import pprint\n",
    "from time import sleep\n",
    "\n",
    "audio_url = 'https://cdn.assemblyai.com/upload/c0afa8a7-09d5-4fe5-8fb6-4a22be40ce12'\n",
    "endpoint = \"https://api.assemblyai.com/v2/transcript\"\n",
    "\n",
    "headers = {\n",
    "    'authorization': api_key, \n",
    "    'content-type': 'application/json'\n",
    "}\n",
    "\n",
    "body = { 'audio_url': audio_url}\n",
    "\n",
    "# 1. Submitting Files for Transcription\n",
    "\n",
    "res = requests.post(endpoint, json=body, headers=headers)\n",
    "transcript_id = res.json().get('id')\n",
    "print(f'{transcript_id = }')\n",
    "\n",
    "# 2. Getting the Transcription Result\n",
    "\n",
    "endpoint_full = f\"https://api.assemblyai.com/v2/transcript/{transcript_id}\"\n",
    "status = 'processing'\n",
    "while status != 'completed':\n",
    "    print('Getting the transcription result ....')\n",
    "    sleep(5)\n",
    "    res_text = requests.get(endpoint_full, headers=headers)\n",
    "    status = res_text.json().get('status')\n",
    "data = res_text.json().get('text')\n",
    "pprint(data[:1000])"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  },
  "vscode": {
   "interpreter": {
    "hash": "aee8b7b246df8f9039afb4144a1f6fd8d2ca17a180786b69acc140d282b71a49"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
