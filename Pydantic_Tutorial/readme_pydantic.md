# 🩺 Pydantic Tutorial: Data Validation & Settings Management

Welcome to the Pydantic Tutorial folder! This guide covers the essential concepts of using **Pydantic** for robust data validation in Python, specifically tailored for application in frameworks like FastAPI.

---

## 🚀 Overview

Pydantic is a library for data validation and settings management using Python type annotations. It enforces type hints at runtime and provides user-friendly errors when data is invalid.

## 📚 Key Concepts Covered

### 1. The `BaseModel` Class
The core of Pydantic is the `BaseModel`. By inheriting from this class, you can define the "schema" of your data.

```python
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int
```

### 2. Basic & Advanced Type Hinting
We explored various Python types that Pydantic uses to validate incoming data:
- **Primitive Types**: `str`, `int`, `float`, `bool`.
- **Default Values**: Fields can have default values (e.g., `married: bool = False`).
- **Complex Types**: Using the `typing` module:
    - `List[str]`: A list containing only strings.
    - `Dict[str, str]`: A dictionary with string keys and string values.
- **Optional Fields**: Using `Optional[T]` for values that can be `None`.

### 3. Special Pydantic Types (p3)
Pydantic provides specialized types for common data formats:
- **`EmailStr`**: Validates that a string is a valid email address.
    - *Note: Requires `pip install "pydantic[email]"`*
- **`AnyUrl`**: Validates strings as valid URLs.

### 4. Advanced Field Validation (p3)
Using the `Field` class and `Annotated`, you can add powerful constraints and metadata to your data:
- **Numeric Constraints**: `gt` (greater than), `ge` (greater or equal), `lt` (less than), `le` (less or equal).
- **String/List Constraints**: `max_length`, `min_length`.
- **Custom Metadata**: Adding descriptions or default values via `Field(default=...)`.
- **Modern Syntax**: Using `Annotated` for cleaner field definitions.

```python
from pydantic import Field
from typing import Annotated

class Patient(BaseModel):
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    allergies: Optional[List[str]] = Field(default=None, max_length=5)
```

### 5. Custom Field Validators (p4)
When built-in constraints aren't enough, `@field_validator` allows you to write custom logic for specific fields.
- **Data Transformation**: e.g., converting names to uppercase.
- **Complex Logic**: e.g., validating email domains or custom age ranges.
- **Execution Mode**: Using `mode='after'` or `mode='before'`.

```python
from pydantic import field_validator

@field_validator('name')
@classmethod
def name_validator(cls, value):
    return value.upper()
```

### 6. Model-Level Validators (p5)
Use `@model_validator` to validate logic that depends on multiple fields simultaneously.
- **Cross-field Validation**: e.g., requiring an emergency contact only if the patient is over a certain age.

```python
from pydantic import model_validator

@model_validator(mode='after')
def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
        raise ValueError('Patients older than 60 must have an emergency contact')
    return model
```

### 7. Computed Fields (p6)
Pydantic allows you to include properties in your model's output using the `@computed_field` decorator. 
- **Dynamic Calculation**: Useful for fields derived from other attributes, like calculating BMI from weight and height.
- **Serialized Output**: Properties decorated with `@computed_field` are included when converting the model to a dictionary or JSON.

```python
from pydantic import computed_field

class Patient(BaseModel):
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
```

### 8. Model Instances & Dictionary Unpacking
Create instances by unpacking dictionaries—perfect for processing JSON API payloads.

```python
patient_info = { 'name': 'Nitish', 'age': 30 }
patient = Patient(**patient_info)
```

---

## 📂 File Structure

- **`pydantic_p1_intro.py`**: Introduction to `BaseModel` and basic string/integer validation.
- **`pydantic_p2.py`**: Deep dive into advanced types like `List`, `Dict`, `Optional`, and default values.
- **`pydantic_p3.py`**: Advanced validation using `EmailStr`, `AnyUrl`, and the `Field` class for constraints.
- **`pydantic_p4_field_Validator.py`**: Custom field-level validation logic using `@field_validator`.
- **`pydantic_p5_model_validator.py`**: Cross-field model-level validation using `@model_validator`.
- **`pydantic_p6_computed_fields.py`**: Using `@computed_field` for dynamically calculated attributes.

## 🛠️ Installation & Usage

### ⚙️ Dependencies
To use email validation, make sure to install:
```bash
pip install "pydantic[email]"
```

### 🏃 Running the Scripts
Run any tutorial script using the Python interpreter:
```bash
python pydantic_p6_computed_fields.py
```
