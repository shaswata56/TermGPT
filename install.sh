#!/bin/sh

sudo cp ./main.py /usr/bin/TermGPT
sudo cp ./personal_openai.env /usr/bin/personal_openai.env
sudo chmod +x /usr/bin/TermGPT

echo "Installation Successful!"
