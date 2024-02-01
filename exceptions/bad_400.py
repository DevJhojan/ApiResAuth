from fastapi import HTTPException, status
def http_400_bad_request(description:str):
    raise HTTPException(status_code=status.HTTP_400_DAD_REQUEST, detail=description)

def http_400_with_header(description:str):
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=description, headers={"WWW-Authenticate":"Bearer"})
