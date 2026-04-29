import os
import sys
import importlib.util

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

try:
    from app import create_app, db
    from app.models import Competition
except ModuleNotFoundError:
    app_init = os.path.join(BASE_DIR, "app", "__init__.py")
    if not os.path.exists(app_init):
        raise RuntimeError(
            f"Could not locate app package at {app_init}. "
            f"Project files in base dir: {os.listdir(BASE_DIR)}"
        )

    spec = importlib.util.spec_from_file_location(
        "app",
        app_init,
        submodule_search_locations=[os.path.join(BASE_DIR, "app")],
    )
    if spec is None or spec.loader is None:
        raise RuntimeError("Failed to build import spec for app package.")

    app_module = importlib.util.module_from_spec(spec)
    sys.modules["app"] = app_module
    spec.loader.exec_module(app_module)

    from app import create_app, db
    from app.models import Competition
from seed import build_sample_competitions


app = create_app()


with app.app_context():
    db.create_all()
    if Competition.query.count() == 0:
        db.session.bulk_save_objects(build_sample_competitions())
        db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)
