from src.utils.DB.database import Session
from src.models.models import Users
from fastapi import Request
from fastapi.responses import JSONResponse
from src.middleware.jwt.jwtService import JWTService, JWTDecoder

db = Session()

async def vaildate_Token(req : Request):
    try:
        header = req.cookies.get('authorization')

        print("header : ",header)

        if(header == None):
            return JSONResponse(status_code=404, content="로그인을 진행해주세요.")

        [tokenType, token] = header.split(' ')

        print("tokenType : ",tokenType)
        print("token : ",token)

        if(tokenType != 'Bearer'):
            return JSONResponse(status_code=400, content="토큰이 타입이 일치하지 않습니다.")

        if(token == None):
            return JSONResponse(status_code=400, content="토큰이 존재하지 않습니다.")

        jwtService = JWTService(None, JWTDecoder())

        jwtVerify = jwtService.check_token_expired(token)
        
        userId = jwtVerify.get('id')

        findUser = db.query(Users).filter(Users.id == userId).first()

        print(req.__dict__)
        
    except Exception as err:
        print("에러가 발생하였습니다.")
        print(err)

    