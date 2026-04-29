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
