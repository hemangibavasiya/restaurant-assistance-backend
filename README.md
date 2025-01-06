# restaurant-assistance-backend
Application to avoid awkward situations in front of the random public while asking for a waiter

Backend Repository Structure

restaurant-assistance-backend/
├── app/ 
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py               # Application configuration (DB URI, JWT settings)
│   │   ├── dependencies.py         # Common dependencies (DB session, auth handling)
│   │   ├── exceptions.py           # Custom exception handlers
│   │   ├── logger.py               # Logger configuration
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── superadmin.py   # Super Admin-related endpoints
│   │   │   │   ├── restaurant.py   # Restaurant-related endpoints
│   │   │   │   ├── waiter.py       # Waiter-related endpoints
│   │   │   │   ├── customer.py     # Customer (guest) endpoints
│   │   │   │   ├── auth.py         # Authentication endpoints
│   │   │   ├── routers.py          # Router definitions for all modules
│   │   │   ├── schemas.py          # Pydantic models for request/response validation
│   ├── db/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py             # Base class for ORM models
│   │   │   ├── superadmin.py       # Super Admin models
│   │   │   ├── restaurant.py       # Restaurant models
│   │   │   ├── waiter.py           # Waiter models
│   │   │   ├── customer.py         # Customer-related models
│   │   │   ├── request.py          # Customer requests models
│   │   ├── session.py              # DB session setup
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py         # JWT and user authentication logic
│   │   ├── qr_service.py           # QR code generation logic
│   │   ├── notification_service.py # Real-time notifications (WebSocket handling)
│   │   ├── payment_service.py      # Payment handling logic
│   │   ├── logging_service.py      # Activity logging for requests
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── qr_code.py              # Utility for generating QR codes
│   │   ├── validation.py           # Input validation helpers
│   │   ├── common.py               # Reusable utility functions
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_superadmin.py      # Unit tests for super admin features
│   │   ├── test_restaurant.py      # Unit tests for restaurant features
│   │   ├── test_waiter.py          # Unit tests for waiter features
│   │   ├── test_customer.py        # Unit tests for customer features
├── .env                            # Environment variables (DB credentials, JWT secret)
├── .gitignore                      # Git ignore file
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation


Detailed Breakdown

Core Components
  config.py: Stores configurations such as database connection URLs, JWT secrets, and WebSocket configurations.
  dependencies.py: Centralizes common dependency injection for API routes (e.g., DB sessions).
  exceptions.py: Defines custom exceptions (e.g., unauthorized access, resource not found).

API Layer
  endpoints/: Contains role-specific API logic. Each role has its own file (e.g., superadmin.py, restaurant.py).
  routers.py: Centralized router to mount all endpoints under /api/v1.

Database Models
  base.py: Base class for all SQLAlchemy models.
  Individual Model Files: Encapsulates the schema and relationships for each entity (e.g., superadmin.py, restaurant.py).

Services
  Authentication Service: Handles user authentication, password hashing, and token generation.
  QR Service: Generates and manages QR codes for tables.
  Notification Service: Implements WebSocket-based real-time notifications.
  Payment Service: Manages payment calculations and histories.
  Logging Service: Captures waiter activity and resolved requests.

Utilities
  Modular functions for QR code generation, validation, and reusable utilities for API responses.

Testing
  Unit tests for each role to ensure API endpoints behave as expected.
  Can be run using pytest.

Key Tools for Integration
  Database: PostgreSQL
  Real-Time Communication: WebSockets
  Authentication: OAuth2 + JWT
  QR Code Generation: Python qrcode library
  Testing: pytest, coverage
  Environment Management: python-decouple (for .env variables)
  Frontend: Flutter-based applications for admin and waiters, with web app for customers.
