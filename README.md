# Mitzva_wallet

# Introduction
- In Jewish life style- there are a lot of mitzvahot to do every day.


- In modern life- there a lot of tools in order to manage the busy day.


- We'll create a simpler way to combine both.


- A wallet that consists prayers beside money. 


 As Rabbi Kook said:" **The old will be renewed, and the new- will be sanctified** "
 

# How to run the romote version(CLI)
1. Clone project: `gh repo clone EASS-HIT-2022/Mitzva_wallet`
2. Right path: `cd ./wallet_backend`
3. Create an image: `docker build . -t  remote-fastapi`
4. Run image: `docker run -ti -p8888:8080  remote-fastapi`
5. Finish server process: `ctrl+c`(just when you want to finish!)

## Display HTTP Respones:
Way no.1- CLI:
1. Open new terminal
2. write `curl localhost:8888`

Way no.2- FastAPI Swagger:
1. Open browser
2. Navigate to `http://localhost:8888/docs`

## Excepted responses with exemples:

**get_root** response:  {"Hello World": "demo-backend"}
**clock** response: {"clock": "Mon Apr 25 21:28:52 2022","req.zone": "string"}
**pay** response:{"id_from": 1,"balance_from": 20,"id_to": 2,"balance_to": 180,"amount": 80
}



## Testing ##
1.  `pytest`




 ###### Options to next steps:
 
 
https://github.com/Sefaria/Sefaria-Project/wiki/API-Documentation
 

https://www.hebcal.com/home/developer-apis
