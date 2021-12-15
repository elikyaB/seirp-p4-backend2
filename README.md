# Notare - Notes App

This is the backend for the Notare App, using Masonite through Heroku to form the API for the [React frontend.](https://github.com/elikyaB/seirp-p4-frontend2)

## Dependencies

- Python v3.10
- PostgreSQL 14
- Masonite 3.0.13

## Models

#### Note Schema
- title: String
- body: String

## Route Table

| Route | URL | Description |
| ----- | --- | ----------- |
| Home | `/` | Masonite Default Welcome Page |
| Index | `/notes` | GET request, returns all notes |
| Create | `/notes` | POST request, uses request body to add product to user cart |
| Update | `/notes/:id` | PUT request, updates specified note |
| Destroy | `/notes/:id` | DELETE request, removes specified note |
| Show | `/notes/:id` | GET request, shows the specified note |
