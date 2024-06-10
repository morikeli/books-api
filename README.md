# Books API

## Overview
This is an API that provide endpoints to add, delete, update or view book records.

## User instructions
Here is a list of endpoints to:
  - get a book (GET) 127.0.0.1:8000/books.

    Expected output - HTTP 302 (Content found)
    
  - get a book record using its ID GET 127.0.0.1:8000/books/{id}.
    
    Expected output - HTTP 200 (OK) if the book record exists else a HTTP 404 (Page not Found) will be returned.
    
  - add a book record (POST) 127.0.0.1:8000/books
    
    Expected output - HTTP 201 (Created) if the book record has been created successfully.
    
  - update a book record (PUT) 127.0.0.1:8000/books/{id}.

    Expected output - HTTP 205 (Reset content) if the book record is updated else a HTTP 404 (Page not Found) will be returned.
    
  - delete a book record (DELETE) 127.0.0.1:8000/books/{id}.

    Expected output - HTTP 204 (No content) if the book record is deleted else a HTTP 404 (Page not Found) will be returned.

## Developer instructions

Installation instructions

```(bash)
  $ cd Desktop
  $ git clone https://github.com/morikeli/books-api.git
  $ python3 -m venv .books-venv
  $ source .books-venv/bin/activate
  $ pip install -r requirements.txt
```
Once all packages are installed. You can access the website on your localhost by typing `python manage.py runserver` in your terminal.
Access the website using this url:
`127.0.0.1:8000`. 
