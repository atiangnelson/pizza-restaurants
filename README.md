
# Pizza API

A simple RESTful API built with Flask to manage restaurants, pizzas, and their relationships.

---

## Setup Instructions

1. **Clone the Repository:**

```bash
git clone <your-repo-url>
cd pizza-api-challenge
```

2. **Create a Virtual Environment:**

```bash
pipenv install
pipenv shell
```

3. **Set the Flask App and Environment:**

```bash
export FLASK_APP=server
export FLASK_ENV=development
```

4. **Run the Server:**

```bash
flask run
```

---

## Database Setup

1. **Initialize Migrations:**

```bash
flask db init
```

2. **Create a Migration:**

```bash
flask db migrate -m "Initial migration"
```

3. **Apply the Migration:**

```bash
flask db upgrade
```

4. **Seed the Database:**

```bash
python -m server.seed
```
## Example Requests & Responses

### GET `/restaurants`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Mario's Pizza",
    "address": "123 Main Street"
  }
]
```

### GET `/restaurants/1`

**Response:**
```json
{
  "id": 1,
  "name": "Mario's Pizza",
  "address": "123 Main Street",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato, Mozzarella, Basil"
    }
  ]
}
```

### GET `/restaurants/100`

**Response:**
```json
{
  "error": "Restaurant not found"
}
```

### DELETE `/restaurants/1`

**Response:**
```json
{}
```

### GET `/pizzas`

**Response:**
```json
[
  {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  }
]
```

### POST `/restaurant_pizzas`

**Request:**
```json
{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 1
}
```

**Response:**
```json
{
  "id": 1,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  },
  "restaurant": {
    "id": 1,
    "name": "Mario's Pizza",
    "address": "123 Main Street"
  },
  "price": 15
}
```

### Invalid POST Example

**Request:**
```json
{
  "price": 50,
  "pizza_id": 1,
  "restaurant_id": 1
}
```

**Response:**
```json
{
  "errors": ["Price must be between 1 and 30"]
}
```

---

## Validation Rules

- **POST `/restaurant_pizzas`:**
  - `price` must be between 1 and 30
  - `pizza_id` and `restaurant_id` must exist

If validation fails, you’ll get:
```json
{ "errors": [ "..." ] }
```

---
