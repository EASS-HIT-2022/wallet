# Wallet
-   [Introduction](#introduction)
-   [Backend](#backend-build) 
-   [Frontend](#frontend-build)


# Introduction
- In Jewish life style- there are a lot of mitzvahot to do every day.


- In modern life- there a lot of tools in order to manage the busy day.


- We'll create a simpler way to combine both.
 

-A wallet that will try to consist available prayers beside financial transactions.


 As Rabbi Kook said:" **The old will be renewed, and the new- will be sanctified** "
 

# How to run the romote version(CLI)
 Clone project: `gh repo clone EASS-HIT-2022/wallet`


# Backend Build:
1. Open new terminal window
2. Right path: `cd ./wallet/backend`
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


# Frontend Build:
1. Open new terminal window, WHEN BACKEND ALREADY UP!
2. Right path: `cd ./wallet/frontend`
3. Create an image: `docker build . -t  remote-streamlit`

# Displaying:
4. Check the localhost:`docker run -p8501:8501 remote-streamlit`
5. Navigate to `http://localhost:8501`

6. New path: `cd ./wallet/frontend/app`
7. Display full GUI: `streamlit run ui.py`
8. Finish server process: `ctrl+c`(just when you want to finish!)



## Testing ##
1.  write `pytest`




 ###### Options to next steps:
 
 
https://github.com/Sefaria/Sefaria-Project/wiki/API-Documentation
 

https://www.hebcal.com/home/developer-apis
