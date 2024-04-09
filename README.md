# image_processing_microservice

image_processing_microservice/
│
├── app/
│   ├── __init__.py
│   ├── main.py               
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── crud.py
│   │   └── schemas.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── image_utils.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   └── image.py
│   │   ├── dependencies.py
│   │   └── routers.py
│   └── tests/
│       ├── __init__.py
│       ├── test_auth.py
│       ├── test_image.py
│       └── test_utils.py
│
├── .env
├── Dockerfile
├── requirements.txt
└── run.py
