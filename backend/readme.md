
# How to run the romote version(CLI)
1. Clone project: `gh repo clone EASS-HIT-2022/wallet`
2. [Build Backend](#backend-build)


# Backend Build✅:
1. Open new terminal window
2. Right path: `cd ./wallet/backend`
3. Create an image: `docker build . -t  remote-fastapi`
4. Run image: `docker run -ti -p8888:8080  remote-fastapi`
5. Finish server process: `ctrl+c`(just when you want to finish!)

## Display HTTP Respones💻:
⚡Way no.1- CLI:
   1. Open new terminal
   2. write `curl localhost:8888`

⚡Way no.2- FastAPI Swagger:
   1. Open browser
   2. Navigate to `http://localhost:8888/docs`

## Excepted responses with exemples:

**get_root** response:    {"Hello World": "demo-backend"}

**clock** response:       {"clock": "Mon Apr 25 21:28:52 2022","req.zone": "string"}

**pay** response:         {"id_from": 1,"balance_from": 20,"id_to": 2,"balance_to": 180,"amount": 80
}

* Finish server process: `ctrl+c`💀

## Testing :📌##
1.  run `pytest` on CLI

# Screenshots(click to watch)📷:

https://user-images.githubusercontent.com/84973766/171572624-2541b4bd-a7ff-4a8b-86c3-4e0b6833ee92.mp4


**Remember!** Backend❤️Frontend

