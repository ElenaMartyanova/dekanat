import os

import psycopg2
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME", "virtual_dean"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "admin123"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432")
}


def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)


def init_database():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Admin (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Category (
            id SERIAL PRIMARY KEY,
            code TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Question (
            id SERIAL PRIMARY KEY,
            category_id INTEGER NOT NULL REFERENCES Category(id) ON DELETE CASCADE,
            created_by_admin_id INTEGER REFERENCES Admin(id) ON DELETE SET NULL,
            updated_by_admin_id INTEGER REFERENCES Admin(id) ON DELETE SET NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Translation (
            id SERIAL PRIMARY KEY,
            question_id INTEGER NOT NULL REFERENCES Question(id) ON DELETE CASCADE,
            language TEXT NOT NULL,
            question_text TEXT NOT NULL,
            answer_text TEXT NOT NULL,
            UNIQUE(question_id, language)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS UnansweredQuery (
            id SERIAL PRIMARY KEY,
            query_text TEXT NOT NULL,
            language TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL,
            status TEXT NOT NULL DEFAULT 'new',
            processed_question_id INTEGER REFERENCES Question(id) ON DELETE SET NULL,
            processed_by_admin_id INTEGER REFERENCES Admin(id) ON DELETE SET NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Feedback (
            id SERIAL PRIMARY KEY,
            question_id INTEGER REFERENCES Question(id) ON DELETE SET NULL,
            query_text TEXT,
            feedback_text TEXT,
            rating INTEGER CHECK (rating IS NULL OR rating BETWEEN 1 AND 5),
            language TEXT NOT NULL,
            created_at TIMESTAMP NOT NULL,
            status TEXT NOT NULL DEFAULT 'new',
            processed_by_admin_id INTEGER REFERENCES Admin(id) ON DELETE SET NULL
        )
    """)

    cursor.execute("""
        ALTER TABLE Question
        ADD COLUMN IF NOT EXISTS created_by_admin_id INTEGER REFERENCES Admin(id) ON DELETE SET NULL
    """)

    cursor.execute("""
        ALTER TABLE Question
        ADD COLUMN IF NOT EXISTS updated_by_admin_id INTEGER REFERENCES Admin(id) ON DELETE SET NULL
    """)

    cursor.execute("""
        ALTER TABLE UnansweredQuery
        ADD COLUMN IF NOT EXISTS processed_question_id INTEGER REFERENCES Question(id) ON DELETE SET NULL
    """)

    cursor.execute("""
        ALTER TABLE UnansweredQuery
        ADD COLUMN IF NOT EXISTS processed_by_admin_id INTEGER REFERENCES Admin(id) ON DELETE SET NULL
    """)

    cursor.execute("""
        ALTER TABLE Feedback
        ADD COLUMN IF NOT EXISTS question_id INTEGER REFERENCES Question(id) ON DELETE SET NULL
    """)

    cursor.execute("""
        ALTER TABLE Feedback
        ADD COLUMN IF NOT EXISTS processed_by_admin_id INTEGER REFERENCES Admin(id) ON DELETE SET NULL
    """)

    categories = [
        ("migration",), ("medical",), ("housing",), ("documents",), ("study",),
        ("general",), ("library",), ("military",), ("graduation",), ("activities",),
        ("international",), ("it_support",), ("transfer",), ("discipline",),
        ("practice",), ("attestation",), ("psychological_service",),
        ("disciplinary_commission",), ("scholarships",), ("first_year",),
        ("employment",), ("foreign_site_faq",)
    ]

    cursor.executemany("""
        INSERT INTO Category (code)
        VALUES (%s)
        ON CONFLICT (code) DO NOTHING
    """, categories)

    admin_username = os.getenv("ADMIN_USERNAME", "admin")
    admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
    admin_password_hash = generate_password_hash(admin_password)

    cursor.execute("""
        INSERT INTO Admin (username, password_hash)
        VALUES (%s, %s)
        ON CONFLICT (username) DO NOTHING
    """, (admin_username, admin_password_hash))

    connection.commit()
    cursor.close()
    connection.close()

    print("База данных PostgreSQL успешно создана.")


if __name__ == "__main__":
    init_database()