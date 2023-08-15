# 설명
FastAPI를 이용해서 CRUD를 구현하는 방법을 알아본다. 

# 사용
## APIRouter를 이용한 라우팅
API Routing은 fastapi가 제공하는 `APIRouter`를 이용해서 구현할 수 있다. 
```python
# 라이브러리 import 
from fastapi import APIRouter

# 변수 선언 및 할당
todo_router = APIRouter()

# 사용
@todo_router.get("/todo")
async def retrieve_todos() -> dict: 
```

APIRouter는 uvicorn에서는 사용할 수 없기 때문에, app 클래스에 router 정보를 추가해준다. 
```python
from fastapi import FastAPI
from todo import todo_router

app = FastAPI()

app.include_router(todo_router)
```

## pydantic을 모델링
요청 데이터에 대해서 올바른 값이 들어왔는지를 확인하기 위해서 요청 데이터를 모델링 할 필요가 있다. 

`BaseModel` 을 이용해서 모델 클래스를 선언해주는 방법으로 처리할 수 있다. 
```python
# 모델 선언
from pydantic import 
class Todo(BaseModel):
    id: int
    item: str

# 선언된 모델 사용
from model import Todo

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
```

## Path를 이용한 PathVariable 설정
`Path`를 이용해서 PathVariable을 구현할 수 있다. 
- PathVariable 구현
- 입력 값과 구분할 수 있는 기능 제공
- swagger 같은 문서를 위한 설명 추가
- 값의 validation을 추가할 수 있다. 

```python
from fastapi import Path

# todo_id를 path variable로 사용
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.", le=1000)) -> dict: 
```

## 문서화 
기본적으로 문서화 기능을 제공한다.  

endpoint
- Swagger: /docs
- ReDoc: /redoc

## 응답 모델 사용
모델을 생성하고, router에 연결해준다. 

```python
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict: 
```

## 에러 발생 및 응답
fastapi가 제공하는 `HTTPException`을 사용한다. 

```python
# library 추가
from fastapi import HTTPException, status

# 에러 발생 메서드 추가
async def raise_not_found_exception():
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist.",
    )
```