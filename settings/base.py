from api.models import Base

settings = {
    'TEMPLATES': {
        'ROOT_DIR': 'templates',
        # 'PACKAGE_DIRS': ['apistar']
    },
    "DATABASE": {
        "URL": "sqlite:///db.sqlite3",
        "METADATA": Base.metadata

    }
}
