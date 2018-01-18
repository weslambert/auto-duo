# auto-duo
Automatically configure a system to pull Duo authentication logs and prep them for Logstash JSON ingestion/processing.

`sudo git clone https://github.com/weslambert/auto-duo && cd auto-duo && sudo chmod +x install_duo && sudo ./install_duo`

Filebeat can be installed on the same host as the Duo script(s) -- just type `YES` when prompted by the `install_duo` script.
