from fastapi import APIRouter, status

router = APIRouter()

@router.get('/',status_code=status.HTTP_200_OK)
async def list_users():
    return{
        'user': [
            {
                'id': 1,
                'email':'rogerio@gmail.com'
            },
            {
                'id': 2,
                'email':'rolf@gmail.com'
            },
            {
                'id': 3,
                'email':'rodolfo@gmail.com'
            },
            
        ]
    }