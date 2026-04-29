from datetime import date

from app import create_app, db
from app.models import Competition


def build_sample_competitions():
    return [
            Competition(
                title="Republican Olympiad (Kazakhstan, Daryn)",
                description="National multi-stage olympiad organized by RSPC Daryn for school students in Kazakhstan (2025-2026 academic year materials and updates on official page).",
                category="Olympiad",
                deadline=date(2026, 4, 15),
                link="https://daryn.kz/respa/",
                difficulty_level="Intermediate",
            ),
            Competition(
                title="International Mathematical Olympiad (IMO 2026)",
                description="67th IMO in Shanghai, China. Official IMO board page lists dates and organizer details.",
                category="Olympiad",
                deadline=date(2026, 7, 10),
                link="https://www.imo-official.org/year_info.aspx?year=2026",
                difficulty_level="Advanced",
            ),
            Competition(
                title="International Olympiad in Informatics (IOI 2026)",
                description="IOI 2026 in Tashkent, Uzbekistan, with official dates announced on IOI resources.",
                category="Olympiad",
                deadline=date(2026, 8, 9),
                link="https://ioinformatics.org/",
                difficulty_level="Advanced",
            ),
            Competition(
                title="NASA International Space Apps Challenge",
                description="Global hackathon using NASA open data. 2025 challenge dates and registration milestones are published by NASA.",
                category="Hackathon",
                deadline=date(2025, 10, 5),
                link="https://www.earthdata.nasa.gov/events/2025-space-apps-challenge",
                difficulty_level="Beginner",
            ),
            Competition(
                title="Technovation Girls Challenge (2025-2026 Season)",
                description="Global student innovation and entrepreneurship program; official timeline includes registration and submission dates.",
                category="Research",
                deadline=date(2026, 4, 20),
                link="https://technovationchallenge.org/program-timeline",
                difficulty_level="Beginner",
            ),
        ]


def seed_competitions(reset=False):
    app = create_app()
    with app.app_context():
        db.create_all()

        if reset:
            Competition.query.delete()
            db.session.commit()

        if Competition.query.count() > 0:
            print("Database already has data. Skipping seed.")
            return

        db.session.bulk_save_objects(build_sample_competitions())
        db.session.commit()
        print("Seed complete: 5 competitions added.")


if __name__ == "__main__":
    seed_competitions(reset=False)
